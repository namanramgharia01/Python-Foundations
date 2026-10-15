# Countdown Timer
import time

start_number = int(input("Enter countdown start: "))
for i in range(start_number, 0, -1):
    print(i)
    time.sleep(1)  

print("HAPPY NEW YEAR!")