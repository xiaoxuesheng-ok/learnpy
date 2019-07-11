# 导入第三方模块

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


# 自定义发送邮件的函数

'''
   配置发邮件所需的基本信息
   my_sender  #配置 发件人邮箱地址
   my_pass    #配置 发件人邮箱密码, 设置保护之后，QQ邮箱这块需要填写授权码，不填写 密码了。
   to_user    #配置 收件人邮箱地址
   my_nick    #配置 发件人昵称
   to_nick    #配置 收件人昵称
   mail_msg   #配置 邮件内容
'''

def mail(my_sender,my_pass,to_user,my_nick,to_nick,mail_msg) :

    # 必须将右键内容做一次MIME转换   -- 这里是发送 含 链接的邮件
    msg=MIMEText(mail_msg,'html','utf-8')

    # 配置发件人姓名和邮箱地址
    msg['From'] = formataddr([my_nick,my_sender])

    # 配置收件人姓名和邮箱地址
    msg['To'] = formataddr([to_nick,to_user])

    # 配置邮件主题（标题）
    msg['Subject'] = "发送邮件测试"

    # 配置python 与 邮件的SMTP服务器的连接通道（如果不是QQ邮箱，SMTP服务器是需要修改的）
    server=smtplib.SMTP_SSL("smtp.qq.com", 465)

    # 模拟登录
    server.login(my_sender,my_pass)


    # 邮件内容的发送
    server.sendmail(my_sender,[to_user,],msg.as_string())

    # 关闭连接通道
    server.quit()


my_sender = "1975034502@qq.com"
my_pass = ""  # 密码或者授权码
to_user = ['1975034502@qq.com','893358985@qq.com']
my_nick = "feng-g"
to_nick = ["123","小学生"]

for i in range(2):

    # 邮件测试
    mail_msg = """
    <p>尊敬的{}：</p>
    <p>您好，非常抱歉打扰到您，这是一份Python的邮件测试，看见后可以忽略。</p>
    <p><a herf="https://www.baidu.com">百度</p>
    """.format(to_nick[i])

    #
    mail(my_sender,my_pass,to_user[i],my_nick,"my_fiend",mail_msg)

    # 如果收件人邮箱自己给自己起名字了，那么发件的时候to_nick在收件人姓名那块还是显示人家自己的。
