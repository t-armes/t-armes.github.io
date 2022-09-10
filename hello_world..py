#Exercise 1.2

a = 'Hello, World'

print(a)

#Exercise 1.3
#Will a baby born today live for 10**9 seconds?
    #I will convert this to years and see:

s = 1
m = s*60
h = m*60
d = 24*h
y = 365*d


answer = s*10**9/y
print(answer) 

#a baby born today will probably live beyond approx 32 years

#Exercise 1.4 
#Choose som amount of meters and convert it to british standard

meter = 1000        #cm
inch = 2.53         #cm
feet = inch*12      #cm
yards = feet*3      #cm
miles = 1760*yards  #cm

#how many inches, feet, yards and miles are there in 1km

km = 1000*meter

km_inch = km/inch
km_feet = km/feet
km_yards= km/yards
km_miles= km/miles

print(f"Amount of inches i 1000 meters is {km_inch:g}")
print(f"Amount of feet i 1000 meters is {km_feet:g}")
print(f"Amount of yards i 1000 meters is {km_yards:g}")
print(f"Amount of miles i 1000 meters is {km_miles:g}")

