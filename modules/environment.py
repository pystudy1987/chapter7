# !/usr/bin/python3
# -*- coding:utf-8 -*-

'''
获取环境变量
'''


import os

def run(**args):
    print("[*] In environment module.")
    return str(os.environ)
