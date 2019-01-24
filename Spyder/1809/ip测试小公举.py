import csv
import time
import requests
from user_agent import UserAgent
"""检查ip池中可以使用的ip，并将其保存为csv文件"""
url = "http://httpbin.org/get"
ip_sea = []
user_agent = UserAgent()
with open('ip_sea.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for m in range(5):
        time.sleep(0.3)
        m = int(m)
        ip = user_agent.check_ip(m)
        headers = user_agent.choice()
        proxies = {'http': "http://" + ip}
        try:
            res = requests.get(url, proxies=proxies, headers=headers, timeout=3)
            if res.status_code == 200:
                ip_sea.append(ip)
                writer.writerow([m, ip])
            print(m, 'yes', ip)
        except EnvironmentError as f:
            print(m, 'no', ip)
