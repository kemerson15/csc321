import netifaces 

def get_interfaces():
    print ("Interfaces:", netifaces.interfaces())

get_interfaces()

def get_mac(interface: str):
    print ("MAC Address:", netifaces.ifaddresses(interface)
           [netifaces.AF_LINK])

get_mac('{BDB2620A-6BB4-4B99-9310-13158AC941B2}')

def get_ips(interface: str):
    try:
        print ("IPv4:", {netifaces.ifaddresses(interface)
                [netifaces.AF_INET][0]['addr']})
    except KeyError:
        print ("IPv6:", {netifaces.ifaddresses(interface)
               [netifaces.AF_INET6][0]['addr']})
    else: 
        print ('No IP addresses.')

get_ips('{BDB2620A-6BB4-4B99-9310-13158AC941B2}')

def get_netmask(interface: str):
    print ("IPv4 Netmask:", {netifaces.ifaddresses(interface)
           [netifaces.AF_INET][0]['netmask']})
    
    print ("IPv6 Netmask:", {netifaces.ifaddresses(interface)
          [netifaces.AF_INET6][0]['netmask']})

get_netmask('{D45D6B56-F09B-11E9-AA57-806E6F6E6963}')

def get_network(interface: str):
    print ("IPv4 Network:", {netifaces.ifaddresses(interface)
           [netifaces.AF_INET][0]['broadcast']})

    print ("IPv6 Network:", {netifaces.ifaddresses(interface)
           [netifaces.AF_INET6][0]['broadcast']})

get_network('{4A28ABA0-EDCD-4549-8F0A-99E86305190C}')