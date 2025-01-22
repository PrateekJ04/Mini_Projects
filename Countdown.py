import time
time1=int(input("Enter time in seconds:  "))

for i in range(time1,0,-1):
    seconds=i%60
    minutes=int(i/60)%60
    hours=int(i/3600)%60
    print(f"Time left {hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Your wait is over, Times up !!!!!")