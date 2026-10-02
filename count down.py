import time
count = int (input("Enter the counter value: "))

for i in range(count,0,-1):
    print(i)
    time.sleep(1)

print("Happy Birthday!")
