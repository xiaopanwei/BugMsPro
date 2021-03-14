import smtplib  # 负责发送邮件
from email.mime.text import MIMEText  # 构造文本
from email.mime.image import MIMEImage  # 构造图片
from email.mime.multipart import MIMEMultipart  # 将多个集合对象集合起来
from email.header import Header
import datetime
import warnings
warnings.filterwarnings('ignore')
# 输入发件人昵称、收件人昵称、主题，正文，附件地址,附件名称生成一封邮件
def create_email(sender_name, receiver_name, email_Subject, email_text):
    #生成一个空的带附件的邮件实例
    message = MIMEMultipart()
    #将正文以text的形式插入邮件中(参数1：正文内容，参数2：文本格式，参数3：编码方式)
    message.attach(MIMEText(email_text, 'plain', 'utf-8'))
    #生成发件人名称
    message['From'] = sender_name
    #生成收件人名称
    message['To'] = receiver_name
    #生成邮件主题
    message['Subject'] = email_Subject
    #返回邮件
    return message
def send_email(sender, password, receiver, msg, mail_host = "smtp.qq.com"):
    # 一个输入邮箱、密码、收件人、邮件内容发送邮件的函数
    try:
        #找到你的发送邮箱的服务器地址，已加密的形式发送
        server = smtplib.SMTP_SSL(host='smtp.qq.com')  # 发件人邮箱中的SMTP服务器
        server.connect(host=mail_host, port=465)
        server.ehlo()
        #登录你的账号
        server.login(sender, password)  # 括号中对应的是发件人邮箱账号、邮箱密码
        #发送邮件
        server.sendmail(sender, receiver, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号（是一个列表）、邮件内容
        print("邮件发送成功" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        # 关闭SMTP对象
        server.quit()
    except Exception as e:
        print(str(e))
        print('邮件发送失败'+ datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))



def sendemail(receiver_name,body_content):
    sender = "1500683214@qq.com"
    sender_name = "肖盼伟<1500683214@qq.com>"
    # 邮箱授权码,注意这里不是邮箱密码！！
    mail_license = "vumpckclzomjhijh"
    # 邮件主题
    subject_content = """你有未解决的Bug"""
    # 邮件正文
    message = create_email(sender_name=sender_name, receiver_name=receiver_name, email_Subject=subject_content,
                           email_text=body_content)
    send_email(sender=sender, password=mail_license, receiver=receiver_name, msg=message)
