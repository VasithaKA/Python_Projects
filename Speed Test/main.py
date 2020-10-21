# Python program to test Internet speed

from speedtest import Speedtest
import itertools
import threading
import time
import sys


def animate(message="Loading... "):
    t = threading.currentThread()
    for c in itertools.cycle(['| ', '/ ', '- ', '\\ ']):
        if getattr(t, "done", False):
            break
        sys.stdout.write('\r' + message + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r')


st = Speedtest()
print("Testing from " +
      st.results.client['isp'] + " (" + st.results.client['ip'] + ")...")
print("Selecting best server based on ping...")
servername = st.get_best_server()
print("Hosted by " + servername['sponsor'] + " ("+servername['name']+") [" + str(
    round(servername['d'], 2)) + " km]: " + str(servername['latency']) + " ms\n")
print("Testing download speed...")
thread = threading.Thread(target=animate, args=("Downloading... ",))
thread.start()
downSpeed = st.download()
thread.done = True
time.sleep(0.1)
print("Download Speed:", round(downSpeed/10**6, 2), "Mbps\n")
print("Testing upload speed...")
thread = threading.Thread(target=animate, args=("Uploading... ",))
thread.start()
upSpeed = st.upload()
thread.done = True
time.sleep(0.1)
print("Upload Speed:", round(upSpeed/10**6, 2), "Mbps")
