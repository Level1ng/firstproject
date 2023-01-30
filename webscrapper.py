import requests
from bs4 import BeautifulSoup
import smtplib
from mypassword_gmail import password

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import datetime
now = datetime.datetime.now()

content = ''

def extract_news(url):
    print("Extracting Hacker News Strories....")
    cnt = ''
    cnt += ('<b>HN Top Strories:</b>\n' + '<br>'+'-'*50+'<br>')
    soup = BeautifulSoup(content, 'html.parser')
    print(soup.prettify())
    # for i,tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
    #     cnt += ((str(i+1)+' :: '+tag.text+"\n" +'<br>') if tag.text!='More' else '')
    #     print(i)
    #     #print(tag.prettify) find_all('span',attrs={'class':'sitestr'})

    return(cnt)

# cnt = extract_news('https://news.ycombinator.com/')
# content += cnt
# content += ('<br>-------------------<br>')
# content += ('<br><br>End of Message')

#lets send the email

soup = BeautifulSoup('https://news.ycombinator.com/','html.parser')
print(soup)
print("Composing Email.....")

# SERVER = 'smtp.gmail.com'
# PORT = 587 # your port number 
# FROM = 'ardiyantoit@gmail.com' #your fraom email id
# TO = 'limardiyanto@gmail.com' #your to email id

# #fp = open(file_name,'rb')
# #create a text/plain messsage
# #msg = MIMEText('')
# msg = MIMEMultipart()

# #msg.add_Header('Content-Disposition','attachment','filename=empty.txt')
# msg['Subject'] = 'Top News Stories HN [Automated Email]' + ' ' + str(now.day) + '-' + str(now.year)
# msg['From'] = FROM
# msg['To'] = TO
# msg.attach(MIMEText(content,'html'))
# #fp.close()

# print("Initiating Server......")

# server = smtplib.SMTP(SERVER,PORT)
# #server = smtplib.SMTP_SSL('smtp.gmail.com',465)
# server.set_debuglevel(1)
# server.ehlo()
# server.starttls()
# #server.ehlo
# server.login(FROM,password)
# server.sendmail(FROM, TO, msg.as_string())

# print('Email Sent.....')

# server.quit()

#Closing