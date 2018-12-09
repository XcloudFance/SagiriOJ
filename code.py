import json
class usersave:
    def __init__(self):
        self.dicts={}
        self.username = ""
        self.code = ""
        fs = open("./json/user.json","r+")
        self.dicts = json.loads(fs.read())
        fs.close()
    def update(self):
        self.dicts[self.username] = self.code
    def save(self):
        try:
            fs = open("./json/user.json","w+")
            fs.write(json.dumps(self.dicts))
            fs.close()
            return True
        except:
            return False
if(__name__=='__main__'):
    user=usersave()
    print(user.dicts)
