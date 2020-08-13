from IPy import IP
import re


def ip_parsing(ip):
    try:
        ips = []
        if not re.findall(r'[a-zA-Z]|-|/', ip):     # 如果没有字母就匹配是否为一个正确的ip地址
            if re.findall(r'\b(?:25[0-5]\.|2[0-4]\d\.|[01]?\d\d?\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b', ip):
                ips.append(ip)
            else:
                print('\033[1;31m[!]host格式错误，E.g：192.168.0.1或192.168.0.0/24或192.168.0.0-255或xxx.com\033[0m')
        elif '-' in ip:                         # 解析c段   E.g: 192.168.0.1-255
            ip1 = ip.split('-')
            ip2 = ip1[0].split('.')
            ip3 = int(ip2[3])
            for i in range(int(ip1[1]) - ip3 + 1):
                ips.append('.'.join(ip2[:3]) + '.' + str(ip3))
                ip3 += 1
        elif '/' in ip:                         # 解析c段   E.g: 192.168.0.0/24
            ip = IP(ip)
            for i in ip:
                ips.append(str(i))
        else:
            ips.append(ip)
    except:
        print('\033[1;31m[!]host格式错误，E.g：192.168.0.1或192.168.0.0/24或192.168.0.0-255或xxx.com\033[0m')
    return ips