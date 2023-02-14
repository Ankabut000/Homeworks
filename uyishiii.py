import datetime as data

### Enter your own
n = input().split('.')

# Example
# n = "01.01.2000 00:00".split('.')

day,month = int(n[0]),int(n[1])
a = n[2].split()
yil = int(a[0])
b = a[1].split(':')
hour,minut = int(b[0]),int(b[1])

data_string =  data.datetime(yil,month,day,hour,minut)

time = data.datetime.strftime(data_string, "%d %B %Y year %H hour %M minute")
print(time)






