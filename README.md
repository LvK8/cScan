# :older_man: cScan
![](https://img.shields.io/badge/python-3.7%2B-green)&emsp;&emsp;![](https://img.shields.io/badge/version-v1.0-orange)

:hourglass: C段存活主机探测、端口扫描工具
:bulb: 其他功能与性能速度正在优化中。。。
## :rocket: Install
```
git clone https://github.com/LvK8/cScan.git
pip install -r requirement.txt
```

## :rainbow: Usage
* 查看帮助
```
python cscan.py -h
```
>usage: cscan.py [-h] [-i ICMP] [-ts TCP] [-p PORT]
>
>SCAN FOR HOSTS AND PORTS
>
>optional arguments:
  -h, --help            show this help message and exit
  -i ICMP, --icmp ICMP  -i ip, ICMP scan for host
  -ts TCP, --tcp TCP    -ts ip, TCP SYN scan for host
  -p PORT, --port PORT  -p port, scan host port; E.g:-p 80,8080,3306 or -p default
* C段主机探测
icmp方式
```
python cscan.py -i 192.168.0.0/24   //IMCP

python cscan.py -ts 192.168.0.0/24  //TCP SYN
```
* 端口扫描
```
python cscan.py -ts 192.168.0.1 -p default
```
**default**扫描top1000端口
快速探测可以使用top100
当然也可以使用**逗号分隔**，列如：-p 80,443,8080
如果上述都不能满足需要，可以**自定义**ports文件中的端口文件，然后在主文件中添加您在ports文件夹中增加的文件名
由于scapy会使python线程阻塞，所以**不建议**扫描太多的端口
## :statue_of_liberty: ToDo List
* 对性能进行优化，提高速度与准确率
* 新扩展功能、自定义功能更加人性化
* 更多的扫描方式，提升准确率隐蔽性
