#!/usr/bin/python
# -*- coding: utf-8 -*-


import psutil
import time
import socket
import datetime
import math
import os
import json


def status(interval=0.5):
    c = psutil.cpu_percent(interval)
    while c > 0:
        if c > 90:
            return "status is alarm"
        elif c >=70:
            return " status is High Load"
        else:
            return"status is OK"

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

def changeTime(allTime):
    day = 24*60*60
    hour = 60*60
    min = 60
    if allTime <60:
        return  "%d sec"%math.ceil(allTime)
    elif  allTime > day:
        days = divmod(allTime,day)
        return "%d days %s"%(int(days[0]),changeTime(days[1]))
    elif allTime > hour:
        hours = divmod(allTime,hour)
        return '%d hours %s'%(int(hours[0]),changeTime(hours[1]))
    else:
        mins = divmod(allTime,min)
        return "%d mins %d sec"%(int(mins[0]),math.ceil(mins[1]))


def gettimeSpend():
    op = datetime.datetime.fromtimestamp(psutil.boot_time())   #get boot time
    ti = datetime.datetime.fromtimestamp(time.time())       #get now time
    min = (ti - op).total_seconds()
    m = round(min)
    timec = changeTime(m)
    return timec


def getDisks():
    par = psutil.disk_usage('/')
    #d = par.percent

    disk["mem_utilization"] = par.percent
    disk["mem.total"] = par.used / 1024 / 1024
    disk["mem.used"] = par.total / 1024 / 1024
    return disk


def getcpu(interval=0.5):
    #c = "CPU_utilization : " + str(psutil.cpu_percent(interval))
    hz = os.popen('cat  /proc/cpuinfo | grep MHz | uniq').read()
    c =psutil.cpu_percent(interval)
    cpu["cpu_utilization"] = c
    cpu["cpu_frequency"] = hz
    return cpu

def getRam():  #get system RAM
    mem = psutil.virtual_memory()
    #r=mem.percent

    Ram["mem_utilization"] = mem.percent
    Ram["mem.total"] = mem.total / 1024 / 1024
    Ram["mem.used"] = mem.used / 1024 / 1024


    return json.dumps(Ram)


def bytes2human(n):
    """
    #>>> bytes2human(10000)
    '9.8 K'
    # >>> bytes2human(100001221)
    '95.4 M'
    """
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.2f %s' % (value, s)
    return '%.2f B' % (n)


def getNetwork():
    tot_after = psutil.net_io_counters()
    #N = "total bytes:                     sent: %-10s     received: %s" % (bytes2human(tot_after.bytes_sent
    net["network_uplink"] =bytes2human(tot_after.bytes_sent)
    net["network_downlink"] = bytes2human(tot_after.bytes_recv)
    return net



def main():
    ma["status"] = status()
    ma["ip"] = get_host_ip()
    ma["spendtime"]=gettimeSpend()
    sta= json.dumps(ma)



    #r = 'mem:' + getRam()
    return sta


if __name__ == '__main__':
    Ram = {}
    cpu={}
    ma= {}
    disk={}
    net={}

    print 'notes:'+main()
    print 'cpu'+str(getcpu())
    print 'disk'+ str(getDisks())
    print 'mem:' + getRam()
    print'network'+str(getNetwork())
