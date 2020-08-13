from scapy.all import *

def ftp_banner(ip, port): 
    source_port = random.randint(1024, 65535)
    init_sn = random.randint(1, 65535*63335)
    try:
        result_raw_synack = sr1(IP(dst=ip)/TCP(dport=port,sport=source_port,flags=2,seq=init_sn), verbose = False)
        sc_sn = result_raw_synack.payload.seq + 1
        cs_sn = result_raw_synack.payload.ack
        banner = sr1(IP(dst=ip)/TCP(dport=port,sport=source_port,flags=16,seq=cs_sn,ack=sc_sn), verbose = False)
        return banner.payload.load.decode().strip()
    except:
        return banner.payload.load


if __name__ == '__main__':
	print(ftp_banner('84.232.109.53', 22))
