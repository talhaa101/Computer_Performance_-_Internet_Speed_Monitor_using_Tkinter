import psutil
import math
import speedtest
print('Physical Cores :' , psutil.cpu_count(logical=False))
print('Logical Processors :',psutil.cpu_count())

#while (1) :
#   print(psutil.cpu_percent(1)) # it gives me cpu usages %


#print('Total System memory is: ',psutil.virtual_memory()) # it will give all memory info


print('Total System memory is:', math.floor(psutil.virtual_memory().total / 1_000_000_000), 'GB')
print('Total Available memory is:', math.floor(psutil.virtual_memory().available / 1_000_000_000), 'GB')
print('Total percent memory used is:', psutil.virtual_memory().percent, '%')
print('Used Memory is:', math.floor(psutil.virtual_memory().used / 1_000_000_000), 'GB')
print('Free Memory is:', math.floor(psutil.virtual_memory().free / 1_000_000_000), 'GB')


# getting the netword speed 

sp = speedtest.Speedtest()

download_speed = round(sp.download() / 1_000_000, 2)  # in Mbps
upload_speed = round(sp.upload() / 1_000_000, 2)      # in Mbps
ping = round(sp.results.ping, 2)                      # in ms

print('Download Speed:', download_speed, 'Mbps')
print('Upload Speed:', upload_speed, 'Mbps')
print('Ping is:', ping, 'ms')
