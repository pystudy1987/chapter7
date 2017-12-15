# !/usr/bin/python3
# -*- coding:utf-8 -*-

'''
获取当前目录下的所有文件并返回文件列表


'''


import os

def run(**args):
    print("[*] In dirlister module.")
    files = os.listdir(".")
    
    return str(files)
