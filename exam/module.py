#-*- coding:utf-8 -*-

import math
import calendar
from Tkinter import *
import sys
import os
import string
import webbrowser


# math
print math.pi

# calnedar
calendar.prmonth(2013, 7)

# widget
widget = Label(None, text='thanks!')
widget.pack()

# sys
sys.ps1 = '^^;'
print 'hello'

# 현재 경로 가져오기
print os.getcwd()

# 해당 경로의 파일 리스트 가져오기
print os.listdir(os.getcwd())

# 첫글자 대문자
print string.capitalize('test')

url = 'http://www.python.org/'
webbrowser.open(url)