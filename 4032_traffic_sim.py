# 4032 - simple traffic simulation
# G Hennessy CUS

import random
import matplotlib.pyplot as plt


def get_modifiers(weather, day_type, holiday, event):
    #Modifiers for weather
    if weather =='sunny':
        weather_mod= 1.0
    elif weather =='rainy':
        weather_mod= 0.85
    else:   # snowy
        weather_mod= 0.65
    #Modifiers for weekday
    if day_type == 'weekday':
        day_mod = 1.0
    else:
        day_mod = 0.8
    #Modifiers for holidays   
    if holiday == 'yes':
        holiday_mod = 0.7
    else:
        holiday_mod = 1.0
    #Modifiers for special events    
    if event == 'yes':
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



print("Welcome to the Traffic Simulation ")
weather = input("Enter weather (sunny, rainy, snowy): ").lower()
while weather not in ['sunny', 'rainy', 'snowy']:
    weather = input("Please enter sunny, rainy, or snowy: ").lower()

day_type = input("Is it a weekday or weekend? ").lower()
while day_type not in ['weekday', 'weekend']:
    day_type = input("Please enter weekday or weekend: ").lower()

holiday = input("Is it a public holiday? (yes/no): ").lower()
while holiday not in ['yes', 'no']:
    holiday = input("Please enter yes or no: ").lower()

event = input("Is there a local event nearby? (yes/no): ").lower()
while event not in ['yes', 'no']:
    event = input("Please enter yes or no: ").lower()

# Figure out the adjustments for weather etc
weather_mod, day_mod, holiday_mod, event_mod = get_modifiers(weather, day_type, holiday, event)
print(weather_mod, day_mod, holiday_mod, event_mod)
# Now simulate the traffic
traffic_data = simulate_traffic(weather_mod, day_mod, holiday_mod, event_mod)
# For test
print(traffic_data)
plot_traffic(traffic_data)


