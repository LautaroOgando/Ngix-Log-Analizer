import re
from collections import Counter

ip_adresses_counter = Counter()
path_counter = Counter()
status_counter = Counter()

ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
path_pattern = r"[A-Z]+ (/.+?) HTTP/\d\.\d"
status_pattern = r"HTTP/1.1\" (\d{3})"


with open("ngnix.log") as f:
    count_ip_adresses = 0
    for i in f:
        match_ip = re.search(ip_pattern,i)
        match_path = re.findall(path_pattern,i)
        match_status = re.findall(status_pattern,i)
        if match_ip:
            ip_adresses_counter[match_ip.group()] += 1 
        if match_path:
            path_counter[match_path[0]] += 1
        if match_status:
            status_counter[match_status[0]] += 1
            

print("\n Top Five IP Adresses: \n")
for ip,count in ip_adresses_counter.most_common(5):
    print(f" {ip} - {count} requests\n")
    
print("\n Top Five Paths: \n")
for path,count in path_counter.most_common(5):
    print(f" {path} - {count} requests\n")  
    
print("\n Top Five Status: \n")
for status,count in status_counter.most_common(5):
    print(f" {status} - {count} requests\n")
  



                    
       


