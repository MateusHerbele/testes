  GNU nano 7.2                                          teste.py                                                    
import socket

sck = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
sck.bind(("172.17.0.2", 0)) 
sck.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1) # Include IP headers

try:
    while True:
        print("Package " + sck.recvfrom(65565))

except KeyboardInterrupt:
    print("Terminating process...")
    socket.close()
