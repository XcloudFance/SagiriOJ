
import  urllib.request
import  json
class Hikoto:
       def load(self):
              type_="b"
              out=""
              while(type_!="a"):
                     url = r'https://v1.hitokoto.cn/?c=a'

                     res = urllib.request.urlopen(url)

                     html = res.read().decode('utf-8')
                     read=json.loads(html)
                     type_=read['type']
                     out=read['hitokoto']+" ——"+read['from']
              return out
if(__name__=="__main__"):
       hitokoto=Hikoto()
       print(hitokoto.load())
