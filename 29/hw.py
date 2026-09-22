from matplotlib import pyplot as plt

days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
temperature=[22,27,20,30,14,23,25]
max_temp=max(temperature)
max_index=temperature.index(max_temp)
print(max_temp)
print(max_index)


plt.plot(days,temperature)
plt.scatter(days[max_index],max_temp,s=100,color="orange",zorder=5)
plt.annotate("The hottest day",xy=(days[max_index],max_temp),zorder=7)
plt.show()