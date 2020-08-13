from concurrent.futures import ThreadPoolExecutor
import threading
from fingerprint.service import get_service
from scapy.all import *


def scan(host, port):
    pkt = IP(dst=host) / TCP(dport=port, flags='S')
    result = sr1(pkt, timeout=1, verbose=0)             # timeout响应超时时间
    if result is not None:
        if result['TCP'].flags == 'SA' or 'A':
            send_1 = sr1(IP(dst=host) / TCP(dport=port, flags="R"), timeout=1, verbose=0)
            service = get_service(port)
            # lock.acquire()
            print(host + ':' + str(result['TCP'].sport) + ' open ' + service)
            # lock.release()
            return True


def runscan(host, port):
    for num in range(2):        # 验证2次
        if scan(host, port):
            break


def PortScan(host, ports):
    results = []
    executor = ThreadPoolExecutor(max_workers=1000)
    for port in ports:
        online_port = executor.submit(runscan, host, port)
        results.append(online_port)
    executor.shutdown()
    return results


lock = threading.Lock()
