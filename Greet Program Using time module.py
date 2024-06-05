import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
timestamp=int(time.strftime('%H'))
print(timestamp)
timestamp=time.strftime('%M')
print(timestamp)
timestamp=time.strftime('%S')
print(timestamp)

#here time module is built-in so, no need of pip
#strft is a function used to manage time which gives hour and minute