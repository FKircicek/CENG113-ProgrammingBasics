# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 23:20:27 2020

@author: fatih
"""
locations = open("provinces.txt","r")
list_of_locations = []
for i in locations:
    i = i.replace("\n","")
    i = i.split(",")
    list_of_locations.append(i)
    
cities = []
for i in list_of_locations:
    cities.append(i[0])
cities.sort()


departure = input("Departure province: \n")
departure = departure.upper()
while True:
    possible_departures = []
    if departure in cities:
        break
    else:
        for i in cities:
            if i.startswith(departure):
                possible_departures.append(i)
    if possible_departures == []:
        print("Province not found!")    
        departure = input("Departure province: \n")
        departure = departure.upper()       
    else:
        print("Province not found!")
        print("Possible provinces: ", possible_departures)
        departure = input("Departure province: \n")
        departure = departure.upper()
        
arrival = input("Arrival province: \n")
arrival = arrival.upper()
while True:
    possible_arrival = []
    if arrival in cities:
        break
    else:
        for i in cities:
            if i.startswith(arrival):
                possible_arrival.append(i)
    if possible_arrival == []:
        print("Province not found!")    
        arrival = input("Arrival province: \n")
        arrival = arrival.upper()       
    else:
        print("Province not found!")
        print("Possible provinces: ", possible_arrival)
        arrival = input("Arrival province: \n")
        arrival = arrival.upper()
        
vehicles = {"CAR":90, "MOTORCYCLE":80, "BICYCLE":25}
while True:
    travel_type = input("Enter travel type: \n")
    travel_type = travel_type.upper()
    if travel_type in vehicles.keys():
        break
    else:
        continue
speed = vehicles[travel_type]
   
print("I am calculating the distance between",departure,"and",arrival)

for i in list_of_locations:
    if departure in i:
        x1 = float(i[1])
        y1 = float(i[2])
        list_of_locations.remove(i)
for i in list_of_locations:
    if arrival in i:
        x2 = float(i[1])
        y2 = float(i[2])        
dx = x2 - x1
dy = y2 - y1
distance = ((dx**2)+(dy**2))**0.5
distance_km = distance * 100
time = distance_km/speed
hours = int(time)
minutes = (time - hours)*60
print("Distance: " , distance_km , "km")
print("Approximate travel time with" , travel_type,":", hours ,"hours" , int(minutes) , "minutes")


all_places = []
for i in list_of_locations:
    xr = float((i[1]))
    yr = float((i[2]))
    dx = xr - x1
    dy = yr - y1
    distance = ((dx**2)+(dy**2))**0.5
    distance_km = distance * 100
    x = [i[0],distance_km]
    all_places.append(x)
recommended_places = []
for i in range(3):
    a = 7000
    for j in all_places:
        if j[1] < a:
            a = j[1]
            b = j
    recommended_places.append(b)
    all_places.remove(b)
for i in recommended_places:
    i.remove(i[1])
recommended_places.sort()
x = []
for i in recommended_places:
    for j in i:
        x.append(j)        
print("Recommended places close to",departure,":",x[0],","
      ,x[1],",",x[2])






























