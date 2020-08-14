import pandas as pd
import requests
import re
#reading the data from csv using pandas library 
df=pd.read_csv("book.csv")
#print(df)


#reading any desired column from CSV file
df1=pd.read_csv('book.csv',usecols=['Phone number'])   #this will return a dataframe
#print(df1)
#print(type(df1))

#converting dataframe to list  testing

#list= df1.values.tolist()[0][0]
#print(list)

#making proper list, final(after testing)
a=0
q=0
list1=[]
s=" "
list= df1.values.tolist()
print("my list is")
print(list)

while(a <len(list)):
    number= df1.values.tolist()[a][0]  #type integer
    a=a+1
    number=str(number)
    #print(number)
    list1.append(number)
#print(list1)


# now write the script for message broadcasting for cell phone

p=s.join(list1)
#print(p)
p=re.sub("[ ]", ",", p) #replacing all spaces with comma
#print(p)




import requests
b=0
url = "https://www.fast2sms.com/dev/bulk"



payload = "sender_id=FSTSMS&message=This%20is%20a%20test%20message&language=english&route=p&numbers="+p
headers = {
    'authorization': "bRrVkUTwhKHPFYD2BjE80X4WaINcSOxZAiy9LfsGlzpdoqnmMuTNx12opHuVZ07UfMFai8LAItzjeDgr",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }
   

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)












