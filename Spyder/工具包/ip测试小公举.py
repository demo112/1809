import csv
import time
import requests
from user_agent import UserAgent


class IpSea(object):
    def work_on(self):
        """检查ip池中可以使用的ip，并将其保存为csv文件"""
        url = "http://httpbin.org/get"
        ip_sea = []
        user_agent = UserAgent()
        len = user_agent.ip_lens()
        print("共有%s个代理" % len)
        with open('ip_sea.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            for m in range(len):
                time.sleep(0.3)
                m = int(m)
                ip = user_agent.check_ip(m)
                headers = user_agent.choice_headers()
                proxies = {'http': "http://" + ip}
                try:
                    res = requests.get(url, proxies=proxies, headers=headers, timeout=3)
                    if res.status_code == 200:
                        ip_sea.append(ip)
                        ip, port = ip.split(':')
                        writer.writerow([ip, port])
                    print(m, 'yes', ip)
                except EnvironmentError:
                    print(m, 'no', ip)
        print('有效数量：', len(ip_sea))


if __name__ == "__main__":
    ipsea = IpSea()
    ipsea.work_on()
