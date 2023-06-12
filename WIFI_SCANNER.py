import nmap

#Author DarkLime

def scan_Network ():
    # Scan the network for all devices and print the info
    nm = nmap.PortScanner()
    
    # Default IP range for the network network
    #ip_Range = "192.168.5.1/24" example
    ip_Range = input("Enter the IP range to scan example(192.168.5.1/24): ")
    
    nm.scan(hosts=ip_Range, arguments='-sn') #Scan all the TCP ports in the IP range

    for host in nm.all_hosts():# gets all the hosts that are up and running in the network
        if 'mac' in nm[host]['addresses']:
            ip = nm[host]['addresses']['ipv4']
            mac = nm[host]['addresses']['mac']
            vendor = nm[host]['vendor'][mac]
            # Print the info of the devices in the network 
            print("IP:",ip)
            print("MAC:",mac)
            print("Vendor:",vendor)
# Run the function
scan_Network()


