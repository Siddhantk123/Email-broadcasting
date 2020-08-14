import pandas as pd
import smtplib as sm
from email.mime.multipart import MIMEMultipart  #for file sending
from email.mime.text import MIMEText #for text sending
from email.mime.image import MIMEImage #for sending an image


#reading email from files
email_col=pd.read_csv('book.csv',usecols=['Email'])
print(email_col)

#converting dataframe to list  testing

#list= email_col.values.tolist()[0][0]
#print(list)

#making proper list, final(after testing)

a=0
q=0
list1=[]
s=" "
list= email_col.values.tolist()
while(a <len(list)):
    number= email_col.values.tolist()[a][0]  #type integer
    a=a+1
    number=str(number)
    #print(number)
    list1.append(number)
#print(list1)





try:
    #object of smtp
    server=sm.SMTP("smtp.gmail.com",587)
    server.starttls() #for secure connection
    #login
    server.login("mishra.siddhant003@gmail.com","minkal@123")
    from_="mishra.siddhant003@gmail.com"
    to_=list1  #email id of recever in a list
    message=MIMEMultipart("alternatives")
    message['Subject']="This is a testing of bulk message plz ignore it."
    message['from']="mishra.siddhant003@gmail.com"

#creating the text in the form of HTML
    html='''
    <html>
        <head>
            <title>can u please ignore?</title>
        </head>
        <body>
            <h1>this is simply to inform you</h1>
            <p>You are dealing with siddhant</p>
            <button><a href="http://siddhantmishra.co.in/">Know Me?</a></button>
         
        </body>
    </html>

         '''

    text=MIMEText(html,"html")
    message.attach(text)
    #send the message
    server.sendmail(from_, to_, message.as_string())
    print("message has been sent..")

     


    
except Exception as e:
    print(e)
    print("error")
