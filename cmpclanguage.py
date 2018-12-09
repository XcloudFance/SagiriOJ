# -*- coding: UTF-8 -*-
import os
import subprocess
import sys
import time
class cl:
    def __init__(self):
        self.filename=""
    def compiletest(self):
        s=-1
        s=os.system("gcc "+sys.path[0]+"\\"+self.filename+" -o "+sys.path[0]+"\\demo.exe")
        while(s==-1):
            time.sleep(0.1);
        if(os.path.exists(sys.path[0]+"\\demo.exe")):
            return True#没有error返回true
        else:
            return False
    def run(self):
       a=-1
       a=os.system(sys.path[0]+"\\demo.exe")
       while(a==-1):
           time.sleep(0.1)
    def fileerrortest(self,files):
        if(os.path.exists(sys.path[0]+"\\"+files+".out")):#判断文件是否存在

            return True#没有error返回true
        else:
            return False
    def runtimetest(self,files):
        if(os.path.exists(sys.path[0]+"\\"+files+".out")):
           fd=open(files+".out",'r')
           if(fd.read()==""):
               
               fd.close()
               return False#有error返回false
           else:
               fd.close()
               return True
   
if(__name__=='__main__'):
    print(sys.path[0])
    test=cplus()
    test.filename="hello.c"
    print(test.compiletest())
    test.run()
    print(test.fileerrortest("hello"))
    print(test.runtimetest("hello"))
