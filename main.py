import os



os.system("clear")
ip_addr = input("What IP Do you want to assign?\n")
netmask = input("What Netmask in CIDR (bitcount) ?\n")
gateway = input("Gateway?\n")
dns = input("DNS?\n")

#print(f"{ip_addr} : {netmask} : {gateway} : {dns}")
netplan_block_1 = """
network:
    version: 2
    renderer: networkd
    ethernets:
        ens32:
            dhcp4: no
            addresses: """

#print(netplan_block_1)
string = netplan_block_1 + "[" + ip_addr + "/" + netmask + "]\n            gateway4: " + gateway + "\n" + "            nameservers:\n                addresses: [" + dns + "]\n"
#print(string)
os.system("echo " + '"' + string + '"' + " > newfile.txt")
