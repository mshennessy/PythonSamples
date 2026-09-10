# 4032 - simple traffic simulation
# G Hennessy CUS

import random
import matplotlib.pyplot as plt


def get_modifiers(weather, day_type, holiday, event):
    #Modifiers for weather
    if weather ==1:
        weather_mod= 1.0
    elif weather ==2:
        weather_mod= 0.85
    else:   # snowy
        weather_mod= 0.65
    #Modifiers for weekday
    if day_type == 1:
        day_mod = 1.0
    else:
        day_mod = 0.8
    #Modifiers for holidays   
    if holiday == 1:
        holiday_mod = 0.7
    else:
        holiday_mod = 1.0
    #Modifiers for special events    
    if event == 1:
        event_mod = 1.3
    else:
        event_mod = 1.0

    return weather_mod, day_mod, holiday_mod, event_mod

def base_traffic(hour):
    #Returns base traffic level depending on hour (simulates real patterns).
    if 7 <= hour <= 9:
        return random.randint(90, 120)  # Morning rush
    elif 16 <= hour <= 18:
        return random.randint(100, 130)  # Evening rush
    elif 12 <= hour <= 13:
        return random.randint(60, 90)   # Lunch hour
    elif 0 <= hour <= 5:
        return random.randint(10, 30)   # Night time
    else:
        return random.randint(40, 70)   # Other times

def simulate_traffic(weather_mod, day_mod, holiday_mod, event_mod):
    # Create a list of 24 traffic values for the graph
    hourly_traffic = []
    
    # Simulate 24 hours of traffic
    for hour in range(24):
        base = base_traffic(hour)
        adjusted = int(base * weather_mod * day_mod * holiday_mod * event_mod)
        hourly_traffic.append(adjusted)

    return hourly_traffic

def plot_traffic(hourly_traffic):
    hours = list(range(24))
    plt.figure(figsize=(12, 6))
    plt.plot(hours, hourly_traffic, marker='o', linestyle='-', linewidth=2)
    plt.title("Simulated Traffic at a Junction Over 24 Hours")
    plt.xlabel("Hour of Day")
    plt.ylabel("Number of Cars")
    plt.xticks(hours)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# You should code the inputs as numbers for simpler code.
# 1=sunny 2=rainy etc
print("Welcome to the Traffic Simulation ")
weather = int(input("Enter weather (1= sunny, 2= rainy, 3=snowy): "))


day_type = int(input("Is it a 1=weekday or 2=weekend? "))


holiday = input("Is it a public holiday? (y/n): ").lower()
if holiday=="y":
    hols=1
else:
    hols=0


event = input("Is there a local event nearby? (y/n): ").lower()
if event == "y":
    ev=1
else:
    ev=0

# Figure out the adjustments for weather etc
weather_mod, day_mod, holiday_mod, event_mod = get_modifiers(weather, day_type, hols, ev)
print(weather_mod, day_mod, holiday_mod, event_mod)
# Now simulate the traffic
traffic_data = simulate_traffic(weather_mod, day_mod, holiday_mod, event_mod)
# For test
print(traffic_data)
plot_traffic(traffic_data)


