#!/usr/bin/python

import subprocess
import json
import os
def executecontainer(container,cmd):
    a=str("docker exec -ti "+ container +" sh -c "+"'"+ cmd+"'")
    print(a)
    os.system(a)
    print("ok")
strings = subprocess.Popen("docker container ls", shell=True, stdout=subprocess.PIPE).stdout.readlines()

for i in range(1,len(strings)):
    pstring = strings[i].split()
    d=dict()
    d["ID"]=pstring[0]
    d["Name"]=pstring[1]
    if(d["Name"]=='zabbix/zabbix-server-pgsql:ubuntu-4.4-latest'):
        l=d["ID"]
executecontainer(l,"apt update")
executecontainer(l,"apt install python -y")
executecontainer(l,"apt install python3 -y")
executecontainer(l,"apt install python-pip -y")
executecontainer(l,"apt install python3-pip -y")
executecontainer(l,"pip install -r /usr/lib/zabbix/externalscripts/requirements.txt")
executecontainer(l,"pip install bs4")
executecontainer(l,"pip3 install -r /usr/lib/zabbix/externalscripts/requirements.txt")
executecontainer(l,"pip3 install bs4")
executecontainer(l,"pip3 install pyTelegramBotAPI")