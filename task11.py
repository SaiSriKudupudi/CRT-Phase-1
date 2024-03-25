tp = int(input("enter ticket price:"))
if tp>250 and tp<300:
    print("recliners")
elif tp>200 and tp<250:
    print("platinum")
elif tp>=150 and tp<200:
    print("gold")
elif tp>100 and tp<150:
    print("silver")
else:
    print("balcony")
