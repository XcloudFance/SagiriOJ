import os
import sys
class Task:
       def __init__(self):
              os.system('JUDGE.exe')
       def read(self):
              s=open("file.out","r")
              a=s.read()
              a=a.replace("s",'')
              a=a.replace("KB",'')
              a=a.replace("retV: ",'')
              b=a.split('\n')
              c=[]
              c.append(float(b[0]))
              c.append(int(b[1])/1024)
              c.append(int(b[2]))
              return c
              
