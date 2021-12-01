from datetime import datetime, timedelta

def IsChristmasSave(file):
    with open(file, "r", encoding="utf8") as f:
        time_arr = f.read().splitlines()
        sum_t = timedelta(hours=0, minutes=0, seconds=0)
        for i in time_arr:
            t = datetime.strptime(i, "%H:%M:%S")
            t2 = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
            sum_t += t2
        if sum_t <= timedelta(hours=24):
            print("Санта может спасти Рождство!")
        else:
            print("Санта не может спасти Рождество:(")



IsChristmasSave("time.txt")