import requests
import matplotlib
import time
import os
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from datetime import datetime

#transfer datetime object into sum of seconds, which will be used in plotting
def getSecond(time):
    ftr = [3600, 60, 1]
    return sum([a * b for a, b in zip(ftr, map(float, time.strftime("%H:%M:%S").split(':')))])

if __name__ == '__main__':
    proxies = {
        "http": "http://10.10.1.2:8080",
        "https": "http://10.10.1.2:8080",
    }
    delays = [0, 100, 200, 300, 400, 500]
    seconds = []
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
        print(" time before sending requests")
        time1 = datetime.now()
        time_1 = time.time()
        print(time1)
        for i in range(50):
            r = requests.get("http://www.bu.edu", proxies=proxies)
        print(" time after sending requests completed")
        time2 = datetime.now()
        time_2 = time.time()
        print(time2)
        # timeBetween = getSecond(time2) - getSecond(time1)
        timeBetween = time_2 - time_1
        seconds.append(timeBetween)
        sBetween = "to finish the requests it takes " + str(timeBetween) + " seconds"
        print(sBetween)
        print("\n")
    os.system("sudo tc qdisc del dev eth0 root netem")

    print("painting\n")
    fig = plt.figure()
    plt.ylim(0, 1)
    plt.plot(delays, seconds, 'ro')
    plt.savefig("withCache_timeCost_vs_delay.png")

    loss = [0, 2, 4, 6, 8]
    seconds_loss = []

    os.system("sudo tc qdisc add dev eth0 root netem delay 0ms")
    for t in range(5):
        los = t * 2
        sLoss = "loss is: " + str(los) + "%"
        print(sLoss)
        if t != 0:
            if t != 1:
                os.system("sudo tc qdisc del dev eth0 root netem")
                print("sudo tc qdisc del dev eth0 root netem")
            s = "sudo tc qdisc add dev eth0 root netem loss " + str(los) + "%"
            print(s)
            os.system(s)
        print(" time before sending requests")
        time1 = datetime.now()
        time_1 = time.time()
        print(time1)
        for i in range(50):
            r = requests.get("http://www.bu.edu", proxies=proxies)
        print(" time after sending requests completed")
        time2 = datetime.now()
        time_2 = time.time()
        print(time2)
        # timeBetween = getSecond(time2) - getSecond(time1)
        timeBetween = time_2 - time_1
        seconds_loss.append(timeBetween)
        sBetween = "to finish the requests it takes " + str(timeBetween) + " seconds"
        print(sBetween)
        print("\n")
    os.system("sudo tc qdisc del dev eth0 root netem")

    fig = plt.figure()
    plt.ylim(0, 1)
    plt.plot(loss, seconds_loss, 'ro')
    plt.savefig("withCache_timeCost_vs_loss.png")

    bandwidths = [100, 150, 200, 250, 300]
    seconds_band = []
    os.system("sudo tc qdisc add dev eth0 root netem loss 0%")
    for t in range(5):
        bandwidth = bandwidths[t]
        sBand = "bandwidth is: " + str(bandwidth) + "%"
        print(sBand)
        if t != 0:
            if t != 1:
                os.system("sudo tc qdisc del dev eth0 root netem")
                print("sudo tc qdisc del dev eth0 root netem")
            s = "sudo tc qdisc add dev eth0 root netem rate " + str(bandwidth) + "kbit"
            print(s)
            os.system(s)
        print(" time before sending requests")
        time1 = datetime.now()
        time_1 = time.time()
        print(time1)
        for i in range(50):
            r = requests.get("http://www.bu.edu", proxies=proxies)
        print(" time after sending requests completed")
        time2 = datetime.now()
        time_2 = time.time()
        print(time2)
        # timeBetween = getSecond(time2) - getSecond(time1)
        timeBetween = time_2 - time_1
        seconds_band.append(timeBetween)
        sBetween = "to finish the requests it takes " + str(timeBetween) + " seconds"
        print(sBetween)
        print("\n")
    os.system("sudo tc qdisc del dev eth0 root netem")

    fig = plt.figure()
    plt.plot(bandwidths, seconds_band, 'ro')
    plt.ylim(0, 1)
    plt.savefig("withCache_timeCost_vs_bandwidth.png")