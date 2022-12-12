#!/usr/bin/env python3
import scapy.all as scapy
import subprocess
import sys
import argparse
import platform
import time
import traceback
    
    
def checking_packet(packet):
       
    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
        try:

            authentic_mac_address = scapy.getmacbyip(packet[scapy.ARP].psrc)
            packet_mac_address=packet[scapy.ARP].hwsrc
            
            if(authentic_mac_address != packet_mac_address):
                print("ALERT ARP spoofing Attack detected!!!")
                print("ACTION:- Closing the Network Connection")
                closing_connection(arguments.interface)
                sys.exit()

        except Exception:
            print(traceback.format_exc())



def closing_connection(interface):
    subprocess.call("ifconfig " + interface +  " down", shell=True)
    print("Connection will restored in 15 sec")
    time.sleep(15)
    restore_connection(interface)


def restore_connection(interface):
    subprocess.call("ifconfig " + interface +  " up", shell=True)
    print("Connection restored.")
    print("In case the attacker try again to attack your system, we will again close your connection to protect your informaton.")
    
    scapy.sniff(iface=arguments.interface, store=False, prn=checking_packet)
        


# Getting the network information detail
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--interface", dest="interface", help="Please provide value for network interface.")
(arguments)= arg_parser.parse_args()
if not arguments.interface:
    arg_parser.error("please specify the network interface")

# Checking for the given interface
scapy.sniff(iface=arguments.interface, store=False, prn=checking_packet)
    
