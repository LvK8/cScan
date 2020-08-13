import re


def get_service(port):
    with open('./fingerprint/nmap-services', 'r', encoding='utf-8') as f:
        data = f.readlines()
        f.close()
        for i in data:
            pattern = re.compile(r"%d/tcp" % port)
            result = pattern.findall(i)
            if result:
                return i.split()[0]