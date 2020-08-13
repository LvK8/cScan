import subprocess
from concurrent.futures import ThreadPoolExecutor
import re
from ipParsing import ip_parsing
from scapy.all import *


# icmp检验主机存活
def ping_scan(ip):
    p = subprocess.Popen(['ping', ip, '-n', '1'],
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         shell=True)
    out = p.stdout.read().decode('gbk')
    regex = re.compile(r'TTL=(\d)')
    result = regex.findall(out)
    if result:
        print('[+]' + ip + ' is online')
        return ip


def run_ping_scan(ip):
    for i in range(3):
        if ping_scan(ip):
            return ip


# TCP SYN检验主机存活
def tcp_syn(ip):
    pkt = IP(dst=ip) / TCP(dport=80, flags='S')
    result = sr1(pkt, timeout=1, verbose=0)         # timeout响应超时时间
    if result:
        send_1 = sr1(IP(dst=ip) / TCP(dport=80, flags="R"), timeout=1, verbose=0)
        print('[+]' + ip + ' is online')
        return ip


def run_tcp_syn(ip):
    for i in range(3):
        if tcp_syn(ip):
            return ip


def HostScan(flag, ips):
    results, result = [], []
    executor = ThreadPoolExecutor(max_workers=1000)
    ips = ip_parsing(ips)
    if flag == 'icmp':
        for i in ips:
            livingIp = executor.submit(run_ping_scan, i)
            results.append(livingIp.result())
    elif flag == 'tcp':
        for i in ips:
            livingIp = executor.submit(run_tcp_syn, i)
            results.append(livingIp)
    executor.shutdown()
    for i in results:
        try:
            if i.result() is not None:
                result.append(i.result())
        except:
            pass
    return result
