#pragma comment(lib,"Psapi.lib")
 
#include <iostream>
#include <time.h>
#include <windows.h>
#include <psapi.h>
#include <tlhelp32.h>
#include <future>
using namespace std;
 
int getExitCode(HANDLE& hProcess) {
	DWORD exitCode = 0;
	GetExitCodeProcess(hProcess, &exitCode);
	return exitCode;
}
 
bool killProcess(PROCESS_INFORMATION& processInfo) {
	DWORD processId = processInfo.dwProcessId;
	PROCESSENTRY32 processEntry = { 0 };
	processEntry.dwSize = sizeof(PROCESSENTRY32);
	//��ϵͳ�ڵ����н�����һ������
	HANDLE handleSnap = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
 
	//����ÿ���������еĽ���
	if (Process32First(handleSnap, &processEntry)) {
		BOOL isContinue = TRUE;
 
		//��ֹ�ӽ���
		do {
			if (processEntry.th32ParentProcessID == processId) {
				HANDLE hChildProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, processEntry.th32ProcessID);
				if (hChildProcess) {
					TerminateProcess(hChildProcess, 1);
					CloseHandle(hChildProcess);
				}
			}
			isContinue = Process32Next(handleSnap, &processEntry);
		} while (isContinue);
 
		HANDLE hBaseProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, processId);
		if (hBaseProcess) {
			TerminateProcess(hBaseProcess, 1);
			CloseHandle(hBaseProcess);
		}
	}
	if (getExitCode(processInfo.hProcess) == STILL_ACTIVE)  {
		return false;
	}
	return true;
}
 
int getCurrentMemoryUsage(HANDLE& hProcess){
	int  currentMemoryUsage = 0;
	PROCESS_MEMORY_COUNTERS pmc;
 
	if (!GetProcessMemoryInfo(hProcess, &pmc, sizeof(pmc))) {
		return 0;
	}
	currentMemoryUsage = pmc.PeakWorkingSetSize >> 10;
 
	if (currentMemoryUsage < 0) {
		currentMemoryUsage = INT_MAX >> 10;
	}
	return currentMemoryUsage;
}
 
int getMaxMemoryUsage(PROCESS_INFORMATION& processInfo, int memoryLimit) {
	int maxMemoryUsage = 0;
	int currentMemoryUsage = 0;
	do {
		currentMemoryUsage = getCurrentMemoryUsage(processInfo.hProcess);
		if (currentMemoryUsage > maxMemoryUsage) {
			maxMemoryUsage = currentMemoryUsage;
		}
		if (memoryLimit != 0 && currentMemoryUsage > memoryLimit) {
			killProcess(processInfo);
		}
		Sleep(200);
	} while (getExitCode(processInfo.hProcess) == STILL_ACTIVE);
 
	return maxMemoryUsage;
}
 
int main(){
 	freopen("file.out","w",stdout); 
	SECURITY_ATTRIBUTES sa;
	sa.nLength = sizeof(sa);
	sa.lpSecurityDescriptor = NULL;
	sa.bInheritHandle = TRUE;
 
	HANDLE hInput = CreateFile("input.txt", GENERIC_READ, 0, &sa, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);
	if (hInput == INVALID_HANDLE_VALUE){
		cout << "error: hInput" << endl;
		return 0;
	}
 
	HANDLE hOutput = CreateFile("output.txt", GENERIC_WRITE, 0, &sa, CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);
	if (hOutput == INVALID_HANDLE_VALUE){
		cout << "error: hOutput" << endl;
		return 0;
	}
 
	STARTUPINFO si = { 0 };
	PROCESS_INFORMATION pi = { 0 };
	si.cb = sizeof(STARTUPINFOW);
	si.dwFlags = STARTF_USESTDHANDLES;
	si.hStdInput = hInput;
	si.hStdError = hOutput;
	si.hStdOutput = hOutput;
 
	//CREATE_SUSPENDED���½��̵����̻߳�����ͣ��״̬��������ֱ������ResumeThread����������ʱ������
	if (CreateProcess(NULL, "DEMO", NULL, NULL, TRUE, CREATE_SUSPENDED, NULL, NULL, &si, &pi)){
 
		clock_t start, end;
 
		//�����̣߳��������ʹ���ڴ棻ref(pi)����pi������
		auto future = async(launch::async, getMaxMemoryUsage, ref(pi), 1048576);
		//�����߳�
		ResumeThread(pi.hThread);
		start = clock();
		WaitForSingleObject(pi.hProcess, INFINITE);
		end = clock();
		cout << (float)(end - start) / CLOCKS_PER_SEC << "s" << endl;
		//��ֹ����
		killProcess(pi);
		cout << future.get() << "KB" << endl;
		
 		cout << "retV: " << getExitCode(pi.hProcess);
 		
		CloseHandle(hInput);
		CloseHandle(hOutput);
	}
	else{
		cout << "��������ʧ��!" << endl;
		HANDLE hProcess = GetCurrentProcess();
		TerminateProcess(hProcess, 0);
	}
 
	return 0;
}
