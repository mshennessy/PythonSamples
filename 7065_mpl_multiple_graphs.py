# Samples drawing graphs just using lists of integers as input
# We will usually form these lists by reading from a csv file

import matplotlib.pyplot as plt


# Set up 3 sets of data - 24 temp readings
day_one_temp = [4.5,4.2,4,3.2,2.5,1.9,2.8,3,2.3,1.7,2,3.6,4.5,5,5.7,5.4,5.1,4.3,3.1,3,2.5,1.7,1.5,1.2]
day_two_temp = [1.1,0.6,0.1,0.3,0.4,0.8,1.3,1.4,1.3,1.3,1.4,1.7,1.9,2.6,2.2,2.8,2.1,0.7,0,-0.3,-0.6,-1.1,-1.2,-1.5]
day_three_temp = [-1.4,-1.4,-1.3,-1.5,-1.6,-1.2,-1.5,-1.4,-0.6,-0.4,0.3,0.7,1.9,2.5,2.1,2.4,2.1,2.4,3.2,3.9,4.2,4.4,4.4,4.5]
# Set up times 
hours = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]


# Day 1 - How to show one data set on a trend graoh
plt.figure(figsize=(5,4))
plt.plot(hours, day_one_temp, color="red")
plt.title("Temperature Day One")
plt.ylabel("Temperature (°)")
plt.xlabel("Time (hrs)")

plt.xlim(1,24)
plt.ylim(min(day_one_temp),max(day_one_temp))

# There are too many values for x-axis, so use these instead
plt.xticks([3,6,9,12,15,18,21,24])
# Show the graph
plt.show()


# Day 1 to 3 - how to graph 3 data sets
# larger graph
plt.figure(figsize=(10,10))
plt.plot(hours, day_one_temp, color="red")
plt.plot(hours, day_two_temp, color="green")
plt.plot(hours, day_three_temp, color="blue")

plt.title("Temperature Of All Days")
plt.ylabel("Temperature (°)")
plt.xlabel("Time (hrs)")
plt.legend(["Day 1", "Day 2", "Day 3"]);

plt.xlim(1,24)
# must be the lowest value to highest value in all 3 lists
# minus 1 from the min value and add 1 to the max value for pure optics!
plt.ylim(min(min(day_one_temp),min(day_two_temp),min(day_three_temp))-1,max(max(day_one_temp),max(day_two_temp),max(day_three_temp))+1)

plt.xticks([3,6,9,12,15,18,21,24])

plt.show()

# create a new list with the average temperature each day
# use your own mean function here instead of statistics.mean()
average_temperatures = [12,15,14]
barLabels= ["Day One", "Day Two", "Day Three"]
plt.figure(figsize=(6,3))
plt.bar(barLabels, average_temperatures, color=("red","green","blue"))
plt.title("Average Temperatures")
plt.ylabel("Temperature (°)")
plt.xlabel("Days")
plt.grid(color="black", linestyle="--", linewidth=1, axis="y", alpha=0.3);
plt.ylim(min(average_temperatures)-1,max(average_temperatures)+1)

plt.show()

# Different type of bar chart, where bars don't start at zero.
min_day_one_temp = min(day_one_temp)
max_day_one_temp = max(day_one_temp)
min_day_two_temp = min(day_two_temp)
max_day_two_temp = max(day_two_temp)
min_day_three_temp = min(day_three_temp)
max_day_three_temp = max(day_three_temp)

temp_ranges = [max_day_one_temp-min_day_one_temp,max_day_two_temp-min_day_two_temp,max_day_three_temp-min_day_three_temp]
min_temps = [min_day_one_temp,min_day_two_temp,min_day_three_temp]
max_temps = [max_day_one_temp,max_day_two_temp,max_day_three_temp]

plt.figure(figsize=(5,4))
plt.bar(["Day One", "Day Two", "Day Three"], temp_ranges, bottom = min_temps, color=("red","green","blue"))
plt.title("Daily Temperature Ranges")
plt.ylabel("Temperature (°)")
plt.xlabel("Days")
plt.grid(color="black", linestyle="--", linewidth=1, axis="y", alpha=0.3);

plt.ylim(min(min_temps)-1,max(max_temps)+1)

plt.show()


day_one_rainfall = [0,0,0.1,0.3,0,0.1,0.2,0.6,1.1,3.4,0.7,0,0,0,0,0,0,0,0,0.5,2.2,1.3,0.3,0]
day_two_rainfall = [0,0,0,0,0,0,0,0.1,0.5,0.2,0,0,0.1,0.3,1.7,0.9,0.4,0.1,0,0,0,0,0,0]
day_three_rainfall = [0.3,0.2,0.1,1.3,0,0,0.6,0,0.1,0.2,0.3,0.4,2.4,0,0,0.5,0,0.1,0,0.8,0.1,0,0.1,0.8]

plt.figure(figsize=(5,4))
plt.title("Total Rainfall")
plt.pie([sum(day_one_rainfall),sum(day_two_rainfall),sum(day_three_rainfall)], labels=["Day One", "Day Two", "Day Three"], colors=["red","green","blue"])
#NB savefig() saves the graph in a file, but might fails if the file already exists or it can't write
plt.savefig("test1.png")
plt.show()
