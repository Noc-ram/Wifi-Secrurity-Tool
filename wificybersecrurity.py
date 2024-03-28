import scapy.all as scapy

def scan_network():
    arp_request = scapy.ARP(pdst="192.168.1.1/24")  # Anpassen des IP-Bereichs je nach Netzwerk
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    devices_list = []
    for element in answered_list:
        device_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        devices_list.append(device_dict)
    return devices_list

def main():
    print("Welcome to the WLAN Security Tool.")
    input("Press Enter to see devices in the network...")
    
    devices = scan_network()
    print("Devices in the network:")
    print("IP\t\t\tMAC Address")
    print("-----------------------------------------")
    for device in devices:
        print(device["ip"] + "\t\t" + device["mac"])

if __name__ == "__main__":
    main()
