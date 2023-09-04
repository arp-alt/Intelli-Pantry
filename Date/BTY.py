#cmd command : tesseract.exe Can_2.png output -l eng
#need internet to run program
#Modules
from datetime import datetime
import datetime as dt
from openpyxl import load_workbook  
from openpyxl import Workbook
import pandas as pd
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from pathlib import Path

#Set the current date at midnight to avoid confusion when subtracting. 
today= dt.datetime.combine(dt.date.today(), dt.datetime.min.time())

#Date read
with open ('C:\\Users\\Sam\\Downloads\\Date\\output.txt','r')as d:  
     lines=d.readline()
     lines_2=d.readlines()
lines_2=[i.replace('\n','') for i in lines_2]
lines_3=lines_2[0]
date_format='%y %m %d'
date_obj=datetime.strptime(lines_3, date_format)
print('Date read before being stored in excel',date_obj)

#Store in excel
workbook = Workbook()

worksheet = workbook.active

worksheet.append([date_obj])

worksheet.insert_rows(idx=1, amount=1)

workbook.save('/Users/Sam/Downloads/insert_row.xlsx')


#Read from  excel
xl = pd.ExcelFile('insert_row.xlsx')
df = xl.parse('Sheet')
Best_Before_date=df['Date'][0]
print('Date read after being stored in excel',Best_Before_date)


# #Find difference
print('Current date',today)
difference = Best_Before_date - today
print('Difference of the days', difference.days,'days')

#initialize everything 
filename = 'Can_2.png'
message = MIMEMultipart()
message['from'] = 'intelli.pantry@gmail.com'
message['to'] = 'samisnoice52@gmail.com'
message['subject'] = 'Product about to Expire!'
message.attach(MIMEText('Finish your product as soon as possible'))
message.attach(MIMEImage(Path('Can_2.png').read_bytes()))

#compare dates then send e-mail
for n in range (1):
    if difference.days >= 4:
        print('No need to send Email becuase difference is more than 4.')
        break

    elif difference.days == 3:
        message = MIMEMultipart()
        message['from'] = 'intelli.pantry@gmail.com'
        message['to'] = 'samisnoice52@gmail.com'
        message['subject'] = 'Product about to Expire in three days!'
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login('intelli.pantry@gmail.com','kfraugexodaeutxz')
            message.attach(MIMEText('Finish your product as soon as possible. It will expire in three days.'))
            message.attach(MIMEImage(Path('Can_2.png').read_bytes()))
            smtp.send_message(message)
            print('Email Sent...')

    elif difference.days == 2:
        message = MIMEMultipart()
        message['from'] = 'intelli.pantry@gmail.com'
        message['to'] = 'samisnoice52@gmail.com'
        message['subject'] = 'Product about to Expire in two days!'
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login('intelli.pantry@gmail.com','kfraugexodaeutxz')
            message.attach(MIMEText('Finish your product as soon as possible. It will expire in two days.'))
            message.attach(MIMEImage(Path('Can_2.png').read_bytes()))
            smtp.send_message(message)
            print('Email Sent...')

    elif difference.days == 1:
        message = MIMEMultipart()
        message['from'] = 'intelli.pantry@gmail.com'
        message['to'] = 'samisnoice52@gmail.com'
        message['subject'] = 'Product about to Expire in one day!'
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login('intelli.pantry@gmail.com','kfraugexodaeutxz')
            message.attach(MIMEText('Finish your product as soon as possible. It will expire in one day.'))
            message.attach(MIMEImage(Path('Can_2.png').read_bytes()))
            smtp.send_message(message)
            print('Email Sent...')
        
    elif difference.days == 0:
        message = MIMEMultipart()
        message['from'] = 'intelli.pantry@gmail.com'
        message['to'] = 'samisnoice52@gmail.com'
        message['subject'] = 'Product has expired,Throw it away!'
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login('intelli.pantry@gmail.com','kfraugexodaeutxz')
            message.attach(MIMEText('Your product has expired, Throw it away as soon as possible.'))
            message.attach(MIMEImage(Path('Can_2.png').read_bytes()))
            smtp.send_message(message)
            print('Email Sent...')
    else:
        break










    
       
    

