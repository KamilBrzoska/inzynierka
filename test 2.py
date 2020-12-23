import time
try:
    while True:
        print("Heavy task!")
        time.sleep(2)
except KeyboardInterrupt:
    print("KeyboardInterrupt has been caught.")