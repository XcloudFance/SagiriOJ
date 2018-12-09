#该程序为防御类，将扫描到一些不该出现的关键词就直接爆0
class Defender:
       def findsof(self,text1):
              br=["shutdown","system","Sleep","sleep","Shutdown","SHUTDOWN","main[-1u]={1};"]
              for i in br:
                     if(text1.find(i)!=-1):
                            return 0
              if(text1.find("freopen")==-1):
                     return 0
              
              return 1
