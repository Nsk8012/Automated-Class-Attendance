import os
import webbrowser
import time

link = "https://www.google.com"

alarm = "16:00:00"

Current_time = time.strftime("%H:%M:%S")

while (Current_time != alarm):
    print("Just Wait")
    Current_time = time.strftime("%H:%M:%S")
    time.sleep(1)

if (Current_time == alarm):
    print("Opening WebPage")
    webbrowser.open(link)
