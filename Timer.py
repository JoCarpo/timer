import time, sys, beepy

print("----------Timer----------")
s = int(input("How many seconds: "))
m = int(input("How many minutes: "))
h = int(input("How many hours: "))

sys.stdout.write(f"\r{h}:{m}:{s}")
sys.stdout.flush()
time.sleep(1)
sys.stdout.write("\r            ")

while True:
    if h > 0 or m > 0 or s > 0:
        if s > 0:
            s -= 1
            sys.stdout.write(f"\r{h}:{m}:{s}")
            time.sleep(1)
            sys.stdout.write("\r            ")
            sys.stdout.flush()
        elif m > 0:
            m -= 1
            s = 59
            sys.stdout.write(f"\r{h}:{m}:{s}")
            time.sleep(1)
            sys.stdout.write("\r            ")
            sys.stdout.flush()
        else:
            h -= 1
            m = 59
            s = 59
            sys.stdout.write(f"\r{h}:{m}:{s}")
            time.sleep(1)
            sys.stdout.write("\r            ")
            sys.stdout.flush()
    else:
        print("\rFinished")
        beepy.beep(6)
        break