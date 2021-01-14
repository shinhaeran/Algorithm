customers = ["10/01 23:20:25 30", "10/01 23:25:50 26", "10/01 23:31:00 05", "10/01 23:33:17 24", "10/01 23:50:25 13", "10/01 23:55:45 20", "10/01 23:59:39 03", "10/02 00:10:00 10"]
from datetime import datetime,timedelta
a = customers[0].split()
print(a)
s = a[0]+' ' +a[1]
time1 = datetime.strptime(s,"%m/%d %H:%M:%S")
print(time1+ timedelta(minutes=int(a[2])))
# print(time1)

