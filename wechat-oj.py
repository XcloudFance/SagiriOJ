#该微信OJ基于itchat,代码著作权归蔡弘毅所有
import itchat
import threading
import os
import sys
import json
from Hikoto import *
itchat.auto_login(True)
#批量添加题目从文件内

def jsonchange(filename):
       fs=open(filename,"r")
       formatted=fs.read()
       fs.close()
       return json.loads(formatted)
       
userlist={"233":"233"}
runqueue={}
oj={0:False}
titleplus={"1000":"add","1001":"domino","1002":"decompose"}
useroj={}
def found(senduser,code):
       global useroj
       sed=senduser
       temp=""
       for i in sed:
              temp+=str(i)
       #print(useroj)
       print(useroj)
       print(temp)
       if(useroj[temp]==0):
              fs=open("./link.ini","r")
              s=fs.read().split("|")
              print(s)
              fs.close()
              fs=open("./"+s[0]+".cpp","w+")
              fs.write(code)
              fs.close()
              os.system("del result.txt")
              os.system("ojtest.py")
             
              while(True):
                     if(os.path.exists("./result.txt")):
                            fs=open("./result.txt","r")
                            itchat.send(fs.read(),senduser)
                            fs.close()
                            oj[0]= False
                            break      
              
def find(senduser,title):
       s=""
       global titleplus
       global runqueue
       for i in senduser:
              s+=i
       global useroj
       global oj
       em=0
       for i in oj:
              if(oj[i]==False):
                     sed=senduser
                     temp=""
                     for j in sed:
                            temp+=str(j)
                     print(senduser)
                     useroj=useroj.fromkeys(senduser)
                     useroj[temp]=i
                     print("OJ0开始测评!")
                     fs=open("./link.ini","w+")
                     fs.write(titleplus[title]+"|cpp")
                     fs.close()
                     oj[i]=True
                     em=1
                     break
       if(em==0):
              itchat.send("OJ已经全部被占用!请稍等片刻[捂脸]")
              '''
                     排队队列的实现比较困难，需要一个线程来监控队列是否为空，如果不为空就检测OJ是否有为false的字典，如果有就进行found编译，暂时不开放此功能以防bug
              '''
              sed=[senduser]
              temp=""
              for i in sed:
                     temp+=str(i)
                
       
       #print(oj,s)
# 注册消息响应事件，消息类型为itchat.content.TEXT，即文本消息
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
       
       global userlist
       global runqueue
       titletemp={1000:"c1000 a+b problem",1001:"c1001 domino",1002:"c1002 decompose"}
       #titletemp=jsonchange("titletemp.json")
       title={}
       #title=jsonchange("title.json")
       
       senduser=msg['FromUserName']
       print(msg['FromUserName'],msg['Text'])
       if(msg['Text']=="启动OJ"):
              hitokoto=Hikoto()
              itchat.send(hitokoto.load(),senduser)
              f=sys.path[0]+"\\emm.jpg"
              itchat.send_image(f,toUserName=senduser)
              if(not senduser in userlist):
                    itchat.send("[奸笑]CloudOpenJudge -石光正在启动!(design by 蔡弘毅)\n========================请输入指令:1查看现有题目\n2.提交代码评测\n",senduser)
                    userlist= userlist.fromkeys([senduser],0)
              else:
                     itchat.send("COJ提示:你刚刚已经启动过OJ了哦",senduser)
                            
       if(senduser in userlist and userlist[senduser]==1):
                     for i in titletemp:
                            if(str(i)==msg['Text']):
                                   fs=open("./评测数据/"+titleplus[str(i)]+"/"+titleplus[str(i)]+".txt","r+")
                                   itchat.send(fs.read(),senduser)
                                   fs.close()
                                   userlist[senduser]=0
       if(senduser in userlist and userlist[senduser]==4):
             itchat.send("正在编译![奸笑]",senduser)
             ta = threading.Thread(target=found, args=(senduser,msg["Text"])).start()
             userlist[senduser]=0
       if(senduser in userlist and userlist[senduser]==3):
              tempa=[]
              test=""
           
              for j in senduser:
                     test+=j
              print([senduser])
              userlist[senduser]=4
              itchat.send("请输入您要评测的代码",senduser)
         
              ta = threading.Thread(target=find, args=([senduser],msg['Text'])).start()
       if(senduser in userlist and userlist[senduser]==0 and msg['Text']=="2"):
              
              itchat.send("OJ提示:已经进入评测队列的高并发处理!请稍等随后返回的评测结果",senduser)
              userlist[senduser]=3
              itchat.send("请输入题号",senduser)
              

       if(senduser in userlist and msg['Text']=="1" ):
                     
                     temp=""
                     for tit in titletemp:
                            temp+=titletemp[tit]+"\n"
                     itchat.send(temp,senduser)
                     userlist[senduser]=1
       print(userlist)
      

'''@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def text_reply(msg):
    itchat.send(u'@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])'''
#coding=utf8

#想给谁发信息，先查找到这个朋友,name后填微信备注即可,deepin测试成功
#users = itchat.search_friends(name='木木')
#获取好友全部信息,返回一个列表,列表内是一个字典
#print(users)
# 绑定消息响应事件后，让itchat运行起来，监听消息

itchat.run()
