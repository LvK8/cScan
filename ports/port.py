import os


def deal(port):
    if '-' in port:
        port = port.split('-')
        result = []
        for i in range(int(port[0]), int(port[1])+1):
            result.append(str(i))
        result = ','.join(result) + ','
    else:
        result = port + ','
    return result


def portsDeal(flag):
    result = ''
    filePath = './ports'
    # if flag in os.listdir(filePath):
    if flag == 'default':
        FILE = 'top1000.txt'
    elif flag == 'top100':
        FILE = 'top100.txt'
    elif flag in os.listdir(filePath):
        FILE = flag
    else:
        print('[!] The file for ports may not exist')
        return ''
    with open(filePath + '/' + FILE) as f:
        data = f.read()
        data = data.split(',')
        for port in data:
            result += deal(port)
        return result.strip(',')

# print(portsDeal('default'))