import hostScan
import portScan
import argparse
import time
from ports.port import portsDeal


def main():
    parser = argparse.ArgumentParser(description='HOST AND CSCAN')
    parser.add_argument('-i', '--icmp', type=str, help='-i ip, ICMP scan for host')
    parser.add_argument('-ts', '--tcp', type=str, help='-ts ip, TCP SYN scan for host')
    parser.add_argument('-p', '--port', type=str, help='-p port, scan host port; E.g:-p 80,8080,3306 or -p default')
    args = parser.parse_args()
    if args.port:
        args.port = ''.join(args.port.split())          # 去除输入端口空格
    if args.port in ['default', 'top100']:                 # 从文件中获得端口
        args.port = portsDeal(args.port)
    if args.icmp:
        print('\033[1;34m[*]hostScan is running\033[0m\n')
        start = time.time()
        result1 = hostScan.HostScan('icmp', args.icmp)
        end = time.time()
        print('\n\033[1;34m[*]hostScan end time: %s \033[0m' % (end-start))
        if args.port:
            ports = args.port.split(',')        # '80,443,8080' > ['80', '443', '8080']
            ports = list(map(int, ports))       # ['80', '443', '8080'] > [80, 443, 8080]
            print('\n\033[1;34m[*]portScan is running\033[0m\n')
            start = time.time()
            for i in result1:
                portScan.PortScan(i, ports)
            end = time.time()
            print('\n\033[1;34m[*]portScan end time: %s\033[0m\n' % (end-start))
    elif args.tcp:
        print('\033[1;34m[*]hostScan is running\033[0m\n')
        start = time.time()
        result1 = hostScan.HostScan('tcp', args.tcp)
        end = time.time()
        print('\n\033[1;34m[*]hostScan end time: %s \033[0m' % (end-start))
        if args.port:
            ports = args.port.split(',')        # '80,443,8080' > ['80', '443', '8080']
            ports = list(map(int, ports))       # ['80', '443', '8080'] > [80, 443, 8080]
            print('\n\033[1;34m[*]portScan is running\033[0m\n')
            start = time.time()
            for i in result1:
                portScan.PortScan(i, ports)
            end = time.time()
            print('\n\033[1;34m[*]portScan end time: %s\033[0m\n' % (end-start))


if __name__ == '__main__':
    main()
