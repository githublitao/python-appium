#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Created on 2017年8月22日

@author: li tao
"""
from Report import configemail
from common import Path, log
import smtplib
import email.MIMEMultipart
import email.MIMEText
import os.path  
import mimetypes  
import email.MIMEImage
import logging


@log.deco(u'发送邮件')
# test_time    测试时间
def send_email(test_time):
    address = configemail.ConfigEmail()
    # 发件人地址
    From = address.get_sender()
    # 收件人地址，多个收件人用逗号隔开
    To = address.get_addressee()
    # 附件名
    file_name = Path.report_path()+test_time+'.html'
    
    server = smtplib.SMTP(address.get_smtp())
    # 仅smtp服务器需要验证时
    server.login(address.get_login(), address.get_authorization_code())
  
    # 构造MIMEMultipart对象做为根容器 
    main_msg = email.MIMEMultipart.MIMEMultipart()  
  
    # 构造MIMEText对象做为邮件显示内容并附加到根容器  
    text_msg = email.MIMEText.MIMEText("Nidone测试报告", charset="utf-8")
    main_msg.attach(text_msg)  
  
    # 构造MIMEBase对象做为文件附件内容并附加到根容器 
    ctype, encoding = mimetypes.guess_type(file_name)
    if ctype is None or encoding is not None:  
        ctype = 'application/octet-stream'
    maintype, subtype = ctype.split('/', 1)
    file_msg = email.MIMEImage.MIMEImage(open(file_name, 'rb').read(), subtype)
    logging.info(ctype, encoding)
    # 设置附件头
    basename = os.path.basename(file_name)
    # 修改邮件头
    file_msg.add_header('Content-Disposition', 'attachment', filename=basename)
    main_msg.attach(file_msg)  
  
    # 设置根容器属性  
    main_msg['From'] = From  
    main_msg['To'] = To  
    main_msg['Subject'] = "Nidone测试报告 "  
    main_msg['Date'] = email.Utils.formatdate()
  
    # 得到格式化后的完整文本 
    fulltext = main_msg.as_string()
  
    # 用smtp发送邮件  
    try:  
        server.sendmail(From, To, fulltext)
    finally:  
        server.quit()  



