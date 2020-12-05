import requests
from datetime import datetime

#transfer datetime object into sum of seconds, which will be used in plotting
def getSecond(time):
    ftr = [3600, 60, 1]
    return sum([a * b for a, b in zip(ftr, map(int, time.strftime("%H:%M:%S").split(':')))])

if __name__ == '__main__':
    proxies = {
        "http": "http://10.10.1.2:8080",
        "https": "http://10.10.1.2:8080",
    }

    print("time before sending requests")
    time1 = datetime.now();
    print(time1)
    for i in range(100):
        r = requests.get("http://www.bu.edu", proxies=proxies)
    print(" time after sending requests completed")
    time2 = datetime.now();
    print(time2)
    timeBetween = getSecond(time2) - getSecond(time1)
    s = "to finish the requests it takes " + str(timeBetween) + " seconds"
    print(s)