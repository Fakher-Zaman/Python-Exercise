import datetime

x = datetime.datetime.now()
print(x)

x = datetime.datetime(2023, 1, 1)
print(x)

print("---> strftime(): ")
print(x.strftime("%m"))
print(x.strftime("%y"))
print(x.strftime("%Y"))
print(x.strftime("%M"))
print(x.strftime("%D"))
print(x.strftime("%a"))
print(x.strftime("%H"))
print(x.strftime("%I"))
print(x.strftime("%p"))
print(x.strftime("%S"))
print(x.strftime("%f"))
print(x.strftime("%Z"))
# Further Functions see from Python Myths (Image)
