from scapy.all import *

packet = IP(dst="8.8.8.8")/ICMP()  # Create an IP packet with ICMP
# packet.show()

packet.ttl = 128
packet[IP].src = "192.168.1.1"

ls(packet)

packet = IP(dst="8.8.8.8")/TCP()/Raw("Hello")

send(packet)