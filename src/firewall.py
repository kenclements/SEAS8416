from scapy.all import IP, TCP, UDP, ICMP
from sud import NetfilterQueue

# Define your filtering rules here
ALLOWED_PORTS = {80, 443}  # Only allow HTTP and HTTPS traffic
BLOCKED_IPS = {"192.168.1.100"}  # Example of IP addresses to block

def process_packet(packet):
    """
    Callback function to process each packet intercepted by the firewall.
    """
    scapy_packet = IP(packet.get_payload())  # Convert raw packet to scapy packet

    # Block specific IP addresses
    if scapy_packet.src in BLOCKED_IPS:
        print(f"Blocked packet from {scapy_packet.src}")
        packet.drop()
        return

    # Handle TCP traffic
    if scapy_packet.haslayer(TCP):
        tcp_layer = scapy_packet.getlayer(TCP)
        if tcp_layer.dport not in ALLOWED_PORTS:
            print(f"Blocked TCP packet to port {tcp_layer.dport}")
            packet.drop()
            return

    # Handle UDP traffic (optional)
    if scapy_packet.haslayer(UDP):
        udp_layer = scapy_packet.getlayer(UDP)
        print(f"UDP Packet to port {udp_layer.dport}")

    # Handle ICMP traffic (optional)
    if scapy_packet.haslayer(ICMP):
        print(f"ICMP Packet type {scapy_packet.getlayer(ICMP).type}")

    # If the packet passes all rules, accept it
    packet.accept()

def main():
    # Create a NetfilterQueue object
    nfqueue = NetfilterQueue()
    try:
        # Bind to queue number 1 and set the callback function
        nfqueue.bind(1, process_packet)
        print("Firewall running...")
        nfqueue.run()
    except KeyboardInterrupt:
        print("\nFirewall stopped.")
    finally:
        nfqueue.unbind()

if __name__ == "__main__":
    main()
