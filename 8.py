#import
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

#reading from file
with open ("data(1).txt","r") as file:
    data = [float(i) for i in file.read().split("\n")]
#with open ("data.txt")
with open ("settings.txt","r") as settings:
    content = [float(i) for i in settings.read().split("\n")]
    time = content[0]
    du = content[1]

#making voltage from binary to volts
time_data = []
for i in range(len(data)):
    data[i] *= du
    time_data.append(time/len(data)*i)
    time_data[i] = round(time_data[i],1)
#making size of graph
fig, ax = plt.subplots(figsize=(16,9), dpi=400)

#making title for graph
plt.title("Процесс зарядки и разрядки коденсатора")

#making graph
ax.plot(time_data, data, lw = 1, c = "b", marker = "o", ms = 5, markerfacecolor = "green", markevery = 100, label = "V(t)")
#ax.plot(time_data,data,ms=1)
ax.scatter(time_data,data,s=1)

    #adding some settings to graph

#adding labels to graph
plt.ylabel('Напряжение, В')
plt.xlabel('Вермя, с')

#calculating charge_time
charge_time = time_data[np.argmax(data)]
print(charge_time)

#calculating uncharging_time 
uncharge_time = time_data[len(data)-1] - charge_time

#adding legend
blue_line = plt.Line2D([], [], color='blue', marker='o',markersize=5, label='V(t)')
ax.legend(handles=[blue_line])

#adding grid
plt.grid()

#changing lim
plt.xlim([0, max(time_data)+5])
plt.ylim([0, max(data)+0.1])

#changing ticks
ax.set_xticks(np.arange(0,151,30))

#text
charge_time_text = "Время зарядки " + str(charge_time)
uncharge_time_text = "Время разрядки " + str(uncharge_time)

#adding text
plt.text(100,2,charge_time_text)
plt.text(100,1.9,uncharge_time_text)

ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())

ax.tick_params(which='major', length=7)
ax.tick_params(which='minor', length=4)

ax.grid(b=True, which='major', linestyle='-')
ax.grid(b=True, which='minor', linestyle='--')

#saving pic
fig.savefig("test.png")



#showing our graph
plt.show()

file.close()
settings.close()