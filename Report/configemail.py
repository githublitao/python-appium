#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Created on 2017年8月22日

@author: li tao
"""
import configparser
from common import Path, log, creat_case
from Exception import Custom_exception


class ConfigEmail:
    #   读取邮件发送配置信息
    @log.deco(u'邮件信息初始化')
    def __init__(self):
        config = configparser.ConfigParser()
        config.read(Path.scan_files(prefix='email_address'))
        try:
            # 发件人地址
            self.Sender = config['email_address']['Sender']
            # 收件人地址，多个收件人用逗号隔开
            self.Addressee = config['email_address']['Addressee']
            # 第三方smtp，例如网易的，smtp.163.com
            self.smtp = config['email_address']['smtp']
            # 授权登录账号
            self.login = config['email_address']['login']
            # 授权码
            self.AuthorizationCode = config['email_address']['AuthorizationCode']
        except Exception as e:
            creat_case.exception_handling(e, "邮件信息初始化")
            raise Custom_exception.MailInitializationError

    def get_sender(self):
        return self.Sender

    def get_addressee(self):
        return self.Addressee

    def get_smtp(self):
        return self.smtp

    def get_login(self):
        return self.login

    def get_authorization_code(self):
        return self.AuthorizationCode
