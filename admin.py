def judge(code):
    if code.find("//System.Call.Accepted()")!=-1:
        return 1
    return 0
#print(judge("//System.Call.Accepted(123)"))