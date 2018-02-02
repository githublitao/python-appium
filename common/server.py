#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Created on 2017年9月30日

@author: li tao
"""
import subprocess
import logging
import os
import requests
import time

from common import Path, runtime


def start_server():
    cmd = 'taskkill /F /IM node.exe'
    logging.info(cmd)
    os.system(cmd)
    logging.info('启动appium服务')
    try:
        cd = 'start /b appium -a 127.0.0.1 -p 4723 --bootstrap-port 9517 --session-override --command-timeout 600'
        logging.info(cd)
        subprocess.call(cd, shell=True, stdout=open(Path.log_path()+runtime.test_start_time()+'appium.log', 'w'),
                        stderr=subprocess.STDOUT)
        appium_server_url = 'http://localhost:4723/wd/hub/'
        logging.info(appium_server_url)
        time.sleep(5)
        response = requests.get(appium_server_url)
        print(response.status_code)
        if response.status_code is 404:
            logging.info('appium服务启动成！！')
        else:
            raise Exception
    except Exception as a:
        logging.error('启动appium服务失败 %s' % a)


def stop_server():
    logging.info('关闭appium服务')
    try:
        cmd = 'taskkill /F /IM node.exe'
        logging.info(cmd)
        os.system(cmd)
        logging.info('关闭appium服务成功！！！')
    except Exception as e:
        logging.error('关闭appium服务失败！！！\n%s' % e)