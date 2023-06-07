'''
Descripttion: your project
version: 1.0
Author: JiangFeng
Date: 2023-06-05 13:37:46
LastEditors: JiangFeng
LastEditTime: 2023-06-07 19:04:11
'''
import smtplib
import argparse
from email.mime.text import MIMEText
import logging


class Mail(object):
    def __init__(self, send_by: str, password: str, send_to: list or str,
                 mail_host='smtp.qq.com', port=465) -> None:
        self.send_by = send_by
        self.send_to = send_to
        self.passwd = password
        
        # 服务器端口，465或者587
        if port in [465, 587]:
            self.port = port
        else:
            raise ValueError("Unexpected port {} is given, but we only support port 465 or 587.".format(port))
        
        if mail_host == 'smtp.qq.com':
            self.mail_host = mail_host
        else:
            raise NotImplementedError("We don't support send email with {},\
                and we will support this soon.".format(mail_host))
        
    
    def send_email(self, subject: str, message: str):
        
        message = MIMEText(message,'plain','utf-8')
        message["From"] = self.send_by
        message['To'] = self.send_to
        message['Subject'] = subject
        
        try:
            smpt = smtplib.SMTP_SSL(self.mail_host, self.port, 'utf-8')
            smpt.login(self.send_by, self.passwd)
            smpt.sendmail(self.send_by, self.send_to, message.as_string())
            print("Success send email to {} with subject {}.".format(
                self.send_to, subject
            ))
        except:
            print("Wrong when send email")


def get_arg():
    parser = argparse.ArgumentParser(description='An simple tool for easy AI training.')
    parser.add_argument('--send_by', help='your qq email', type=str,
                        default="1308093945@qq.com")
    parser.add_argument('--send_to', help='target email address', type=str,
                        required=True)
    parser.add_argument('--password', help='your authorization code, and you can change the default for easy use.', 
                        default="", type=str)
    parser.add_argument('--subject', help='subject of your email', type=str, default="Test")
    parser.add_argument('--message', help='message of your email', type=str, default="Hello World")
    args = parser.parse_args()
    return args


def main():
    args = get_arg()
    send_by = args.send_by
    password = args.password
    send_to = args.send_to
    subject = args.subject
    message = args.message
    # send_email(send_by, password, send_to, subject,message, True)
    # send_email(send_by, password, send_to, subject,message, False)
    email = Mail(send_by, password, send_to)
    email.send_email(subject, message)
    email.send_email(message, subject)

if __name__ == "__main__":
    main()