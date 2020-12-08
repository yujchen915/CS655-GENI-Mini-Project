import requests
import matplotlib
import os
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from datetime import datetime
def changeDelay():
    delays = [0, 100, 200, 300, 400, 500]
    seconds_delay = []
    
    for i in range(6):
        delay = delays[i]
        str_dalay = "delay is: " + str(delay)
        print(str_dalay)

        if i!= 0:
            if i!= 1:
                os.system("sudo tc qdisc del dev eth0 root netem")
                print("sudo tc qdisc del dev eth0 root netem")
            st = "sudo tc qdisc add dev eth0 root netem delay " + str(delay) + "ms"
            print(st)
            os.system(st)

        print("Sending request...")
        print("Start time:")
        start = datetime.now()
        print(start)
        for k in range(50):
            req = requests.get("http://www.google.com")
        print("Requests completed.")
        print("End time:")
        end = datetime.now()
        print(end)

        time_send = (end-start).total_seconds()
        seconds_delay.append(time_send)
        str_time = "It takes " + str(time_send) + " seconds to finish sending the requests."
        print(str_time)
        print("\n")
    os.system("sudo tc qdisc del dev eth0 root netem")

    fig = plt.figure()
    plt.plot(delays, seconds_delay, 'ro')
    #plt.ylim(0, 100)
    plt.savefig("withoutCache_time_vs_delay.png")

def changePacketLoss():
    loses = [0, 0.02, 0.04, 0.06, 0.08, 0.1]
    seconds_loss = []
    for i in range(6):
        lose = loses[i]*100
        str_lose = "lose is: " + str(lose)
        print(str_lose)
        if i != 0:
            if i != 1:
                os.system("sudo tc qdisc del dev eth0 root netem")
                print("sudo tc qdisc del dev eth0 root netem")
            st = "sudo tc qdisc add dev eth0 root netem loss " + str(lose) + "%"
            print(st)
            os.system(st)

        print("Sending request...")
        print("Start time:")
        start = datetime.now()
        print(start)
        for k in range(50):
            req = requests.get("http://www.google.com")
        print("Requests completed.")
        print("End time:")
        end = datetime.now()
        print(end)

        time_send = (end-start).total_seconds()
        seconds_loss.append(time_send)
        str_time = "It takes " + str(time_send) + " seconds to finish sending the requests."
        print(str_time)
        print("\n")
    os.system("sudo tc qdisc del dev eth0 root netem")

    fig = plt.figure()
    plt.plot(loses, seconds_loss, 'ro')
    plt.savefig("withoutCache_time_vs_loss.png")

def changeBandwidth():
    bandwidths = [100,150,200,250,300]
    seconds_band = []
    for i in range(5):
        bandwidth = bandwidths[i]
        str_bandwidth = "bandwidth is: " + str(bandwidth)
        print(str_bandwidth)
        if i != 0:
           #os.system("sudo tc qdisc del dev eth0 root tbf rate")
            #print("sudo tc qdisc del dev eth0 root tbf rate")
            os.system("sudo tc qdisc del dev eth0 root netem")
            print("sudo tc qdisc del dev eth0 root netem")
        st = "sudo tc qdisc add dev eth0 root netem rate " + str(bandwidth) + "kbit"
        print(st)
        os.system(st)

        print("Sending request...")
        print("Start time:")
        start = datetime.now()
        print(start)
        for k in range(50):
            req = requests.get("http://www.google.com")
        print("Requests completed.")
        print("End time:")
        end = datetime.now()
        print(end)

        time_send = (end-start).total_seconds()
        seconds_band.append(time_send)
        str_time = "It takes " + str(time_send) + " seconds to finish sending the requests."
        print(str_time)
        print("\n")
    #os.system("sudo tc qdisc del dev eth0 root tbf rate")
    os.system("sudo tc qdisc del dev eth0 root netem")

    fig = plt.figure()
    plt.plot(bandwidths, seconds_band, 'ro')
    plt.savefig("withoutCache_time_vs_bandwidth.png")


if __name__ == '__main__':
    changeDelay()
    changePacketLoss()
    changeBandwidth()
