import json
import random
jsonfilename = "fpcdata.json"

def getjsondata(jsonfilename):
    with open(jsonfilename,"r",encoding="utf8") as file:
        temp = file.read()
        if temp == '':
            print("no data")
            return {}
        else:
            data = json.loads(temp)
            return data

def setjsondata(jsonfilename,data):
    with open(jsonfilename,"w",encoding="utf8") as file:
        json.dump(data, file)
        
def addjsondata(data,key,name,num,date):
    if key in data:
        return False
    else:
        temp={"name":name,"num":num,"date":date}
        data[key]=temp
        return True
if __name__ == '__main__':
    data = getjsondata(jsonfilename)

    i=0
    while(i==10):
        key='10000'+str(random.randint(1000,9999))
        num='10029363'+str(random.randint(1000,9999))
        date='20210331'+str(random.randint(10,20))+str(random.randint(10,59))+str(random.randint(10,59))
        if addjsondata(data,key,"顾客",num,date):
            print(data)
            i=i+1
            #setjsondata(jsonfilename,data)
        else:
            print("have"+"10245")

    if addjsondata(data,"100008152","顾客","num","date"):
        print(data)
        i=i+1
        #setjsondata(jsonfilename,data)
    else:
        print("have"+"10245")

    setjsondata(jsonfilename,data)