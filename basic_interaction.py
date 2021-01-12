import nmap3
import json
import os
nmap = nmap3.Nmap()

allHostsAsus = nmap.nmap_list_scan("192.168.50.0/24")
allHostsAsus = json.dumps(allHostsAsus, indent=4)

nmap_online_hosts = os.popen("nmap -sn 192.168.50.0/24").read()

nmof = nmap_online_hosts.split()

print(f"""
=======================
Nmap Version {nmof[2]}
=======================

{nmof[14]}
- IP: {nmof[15]}
- Latency: {nmof[19]})

""")