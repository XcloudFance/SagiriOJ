import os
import sys
import time
print("SagiriOpenJudge正在进行对拍!")

#此过程必须在测试完程序后生成数据开始执行
def ansjudge(programname,i):
    fa=open(programname+i+".in","r+")
    fs=open(programname+i+".out","r+")
    fd=open(".\\评测数据\\"+programname+"\\"+"sCoding.in","w+")
    fd.write(str(fa.read())+"\n"+str(fs.read()))
    fs.close()
    fd.close()
    fa.close()
    res=os.system("cd "+sys.path[0]+"\\评测数据\\"+programname+" && "+"sCoding.exe\n")
    while(res==-1):
        time.sleep(0.08)
    fs=open(".\\评测数据\\"+programname+"\\"+"sCoding.out","r")
    s=fs.read()
    fs.close()
    
    if(s=="1" or s=="1\n"):
        return 1
    else:
        return 0
    
    
