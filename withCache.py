import requests
from datetime import datetime
import matplotlib.pyplot as plt
import os

#transfer datetime object into sum of seconds, which will be used in plotting
def getSecond(time):
    ftr = [3600, 60, 1]
    return sum([a * b for a, b in zip(ftr, map(int, time.strftime("%H:%M:%S").split(':')))])

if __name__ == '__main__':
    delays = [0, 100, 200, 300, 400, 500]
    seconds = []
    proxies = {
        "http": "http://10.10.1.2:8080",
        "https": "http://10.10.1.2:8080",
    }
    for t in range(6):
        delay = t * 100
        sDelay = "delay is: " + str(delay)
        print(sDelay)
        if t != 0:
            if t != 1:
                os.system("sudo tc qdisc del dev eth0 root netem")
                print("sudo tc qdisc del dev eth0 root netem")
            s = "sudo tc qdisc add dev eth0 root netem delay " + str(delay) + "ms"
            print(s)
            os.system(s)
        print("time before sending requests")
        time1 = datetime.now();
        print(time1)
        for i in range(100):
            r = requests.get("http://www.bu.edu", proxies=proxies)
        print(" time after sending requests completed")
        time2 = datetime.now();
        print(time2)
        timeBetween = getSecond(time2) - getSecond(time1)
        seconds.append(timeBetween)
        s = "to finish the requests it takes " + str(timeBetween) + " seconds"
        print(s)
    os.system("sudo tc qdisc del dev eth0 root netem")
    fig = plt.figure()
    plt.plot(delays, seconds, 'ro')
    plt.savefig("withCache_timeCost_vs_delay.png")