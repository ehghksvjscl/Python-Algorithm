hour , minute = map(int,input().split())

def strange_alarm_clock(h,m):
    if m > 44:
        print(f"{h} {m-45}")
    elif h <= 23 and h > 0:
        print(f"{h-1} {60-(45-m)}")
    else:
        print(f"23 {60-(45-m)}")

strange_alarm_clock(hour,minute)