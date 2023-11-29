from scapy.all import *
import argparse

parser = argparse.ArgumentParser(description='ICMP TTL spoofer')
parser.add_argument('ttl', type=int, help='TTL value to use in ICMP responses')

args = parser.parse_args()

def icmp_responder(packet):
    if packet.haslayer(ICMP):
        print(f"Recibido ICMP Echo Request de {packet[IP].src} con ID {packet[ICMP].id}, SEQ {packet[ICMP].seq} , TYPE {packet[ICMP].type} y TTL {packet[IP].ttl}")
        ip_layer = IP(src=packet[IP].dst, dst=packet[IP].src, ttl=args.ttl)
        icmp_layer = ICMP(type=0, id=packet[ICMP].id, seq=packet[ICMP].seq)
        data = packet[Raw].load if packet.haslayer(Raw) else b''
        response = ip_layer / icmp_layer / data
        print(f"Enviando ICMP Echo Reply a {packet[IP].src} con ID {packet[ICMP].id}, SEQ {packet[ICMP].seq} , TYPE {packet[ICMP].type} y TTL {packet[IP].ttl}")
        send(response, verbose=False)

#Listen for ICMP packets
sniff(filter="icmp", prn=icmp_responder)
