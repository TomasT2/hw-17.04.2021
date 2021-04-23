def time(a):
    while a > 1440:
        a-=1440
    min=a%60
    hour=a//60
    print("часов: ", hour,", минут: ", min )