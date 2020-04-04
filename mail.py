#coding: utf-8
 
from email.mime.text import MIMEText
import smtplib
 
mail_content = "暴力破解失败，字典已遍历完毕."
count = 1

"""
腾讯企业邮箱：
发送服务器：smtp.exmail.qq.com SSL端口 465
接收服务器：imap.exmail.qq.com SSL端口 993

腾讯QQ邮箱：
发送服务器：smtp.qq.com SSL端口 465|587
接收服务器：imap.qq.com SSL端口 993
接收服务器：pop.qq.com SSL端口 995

谷歌邮箱（若邮箱开启二次验证，切记去生成一个应用专用密码）：
发送服务器：smtp.gmail.com SSL端口 465
接收服务器：imap.gmail.com SSL端口 993

网易126邮箱：
发送服务器：smtp.126.com SSL端口 465
接收服务器：imap.126.com SSL端口 993
接收服务器：pop.126.com SSL端口 995
"""


def send():
    try:
        # 第一个参数：邮件的内容；第二个参数：邮件内容的格式，普通的文本，可以使用:plain,如果想使内容美观，可以使用:html；第三个参数：设置内容的编码，这里设置为:utf-8
        content = MIMEText(mail_content + str(count), 'plain', 'utf-8')
        receivers = "xxxx@vip.qq.com,xxxx@163.com"
        sender = str("xxxxx@163.com")
        # 设置邮件的接收者，多个接收者之间用逗号隔开
        content['To'] = receivers
        # 邮件的发送者,最好写成str("这里填发送者")，不然可能会出现乱码
        content['From'] = sender
        # 邮件的主题
        content['Subject'] = "字典遍历完毕" + str(count)

        ##############使用qq邮箱的时候，记得要去开启你的qq邮箱的smtp服务；##############
        # 方法：
        # 1）登录到你的qq邮箱；
        # 2）找到首页顶部的【设置】并点击；
        # 3）找到【账户】这个选项卡并点击，然后在页面中找到“SMTP”相关字样，找到【开启】的超链接，点击后会告诉你开启方法（需要发个短信），然后按照指示操作，最终会给你一个密码，这个密码可以用于在代码中当作邮箱密码
        ###########################################################################
        # 第一个参数：smtp服务地址（你发送邮件所使用的邮箱的smtp地址，在网上可以查到，比如qq邮箱为smtp.qq.com） 第二个参数：对应smtp服务地址的端口号
        smtp_server = smtplib.SMTP_SSL("smtp.163.com", 465) 
        # 第一个参数：发送者的邮箱账号 第二个参数：对应邮箱账号的密码/授权码
        smtp_server.login(sender, "xxxxx") 
        #################################

        # 第一个参数：发送者的邮箱账号；第二个参数是个列表类型，每个元素为一个接收者；第三个参数：邮件内容
        smtp_server.sendmail(sender, receivers.split(','), content.as_string()) 
        smtp_server.quit() # 发送完成后加上这个函数调用，类似于open文件后要跟一个close文件一样

        return True
        
    except Exception as e:
        print(e)
        exit