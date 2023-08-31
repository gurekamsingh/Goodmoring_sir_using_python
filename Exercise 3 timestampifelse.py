import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
currenttime = int(time.strftime("%H"))
print(currenttime)
if currenttime >= 12 and currenttime<15:
    print("Good afternoon")
elif currenttime < 12 or currenttime == 24:
    print('Good morning')
elif currenttime >= 15 and currenttime < 18:
    print("Good evening")
else:
    print("Good night")

