temperature=(30,32,35,78,65,46)
# 1. To find the Hottest and Coldest

hottest=max(temperature)
print("HOT Temperature :: ",hottest)

coldest=min(temperature)
print("COLD Temperature :: ",coldest)

# 2. AVG. Temperature
avg=sum(temperature)/len(temperature)
print("Average :: ",avg)
