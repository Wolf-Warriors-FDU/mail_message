'''
Descripttion: your project
version: 1.0
Author: JiangFeng
Date: 2023-06-05 13:37:46
LastEditors: JiangFeng
LastEditTime: 2023-06-05 13:47:58
'''
import smtplib
from email.mime.text import MIMEText
import sys
 

mail_host = 'smtp.qq.com' # QQ邮箱提供的SMTP服务器
port = 465 # 服务器端口，不要修改
send_by = '*****@qq.com' # QQ邮箱账号
password = '****' # 开启QQ邮箱STMP后获得授权码
send_to = '****@****' # 目标邮箱

def send_email(title, content, send_self=False):
      message = MIMEText(content,'plain','utf-8')
      message["From"] = send_by
      message['To'] = send_by if send_self else send_to
      message['Subject'] = title
      try:
          smpt = smtplib.SMTP_SSL(mail_host, port, 'utf-8')
          smpt.login(send_by,password)
          smpt.sendmail(send_by, send_to,message.as_string())
          print("Success!")
      except:
          print("Fail")
def main():
    title = sys.argv[1]
    content = sys.argv[2]
    send_email(title, content, True)
    send_email(title, content, False)
if __name__ == "__main__":
    main()