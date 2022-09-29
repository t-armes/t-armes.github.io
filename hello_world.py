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

#Exercise 1.5
#Computing the mass of 1L

#Convert between 1L & g/cm^3

#1L = 1dm^3 = 1000cm^3
#d = m/V         #density formula, m = mass, V = volume
#mass = density * volume

iron            = 7.874    #g/cm^3
air             = 0.001225 #g/cm^3
gasoline        = 0.75     #g/cm^3
ice             = 0.92     #g/cm^3
the_human_body  = 1        #g/cm^3
silver          = 10.49    #g/cm^3
platnium        = 21.45    #g/cm^3

print('---------------------------------------------------------')
print(f"1L of Iron weighs {iron*1000:g}g")
print(f"1L of Air weighs {air*1000:g}g")
print(f"1L of Gasoline weighs {gasoline*1000:g}g")
print(f"1L of Ice weighs {ice*1000:g}g")
print(f"1L of The Human Body weighs {the_human_body*1000:g}g")
print(f"1L of Silver weighs {silver*1000:g}g")
print(f"1L of Platnium weighs {platnium*1000:g}g")
print('---------------------------------------------------------')

#Exercise 2.1
#Farenheight to Celcius conversion

print('-------------------------------')
print(f"|  Farenheight  |   Celcius   |")
print('-------------------------------')

F = 0       #Celcius begynner i 0 grader
dF = 10     #Delta C, C øker med 10 grader per løkke
            #Formel for Farenheight, F = C * 1.8 + 32

while 100 >= F >= 0 :
    
    C = (F - 32)/1.8
    print(f"       {F},          {C:g}")
    F = F + dF
    
    
print('------------------------------')

#Exercise 2.2
#Add approx ^C 

C_ = (F - 30)/2     #Aprx C
print('-----------------------------------------')
print(f"|  Farenheight  |  Celcius   | Approx C |")
print('-----------------------------------------')

F = 0
dF = 10

while 100 >= F >= 0:
    
    C = (F - 32)/1.8
    C_ = (F - 30)/2     #Aprx C
    print(f"    {F},           {C:g},        {C_:g}")
    F = F + dF
    
print('-----------------------------------------')

#Exercise 2.3
#Lists, for loops

primes = [2,3,5,7,11,13]
for element in primes:
    print(element)

p = 17

primes.append(p)
print(primes)

# Exercise 2.4
# Even and Odd

n = -1

while n <= 100:
    n = n + 2
    print(n)


    
    
