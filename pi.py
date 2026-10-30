# Here a unit circle x^2 + y^2 = 1 is considered
# Wait for 20 seconds atleast
distance = 10**(-6)
#Kind of value of dx
def quadratic(a,b,c):
    d = (b**2 - 4*a*c)
    if d<0:
       return 0
       # At last iteration complex root might come so its neglected
    return (-b+d**(0.5))/(2*a)
    # Quadratic formula
def tangent(x1,y1):
    tan = x1/y1
    #Slope of tangent at point x1,y1 on our circle
    cos = 1/((1 + tan**2)**(1/2))
    sin = (1- cos**2)**(1/2)
    # Basic trignometiric angle identities
    x2 = x1+ cos*distance
    y2 = y1- sin*distance
    # Parametric form of new point
    c1 = y1*x2 - x1*y2
    y3 = quadratic(x1**2 + y1**2,2*x1*c1*y1,c1**2 - y1**2)
    x3 = (1 - y3**2)**(1/2)
    # Calculated result of intersection of normal drawn from x2,y2 and the circle
    d = ((x3-x1)**2 + (y3-y1)**2)**(1/2)
    # Since we are working with very small distances, the distance between these 2 points would approx be an arc length
    return (x3,y3,d)
sum = 0
x = 0
y = 1
# Starting from (0,1) on our circle
while y>0:
    r = tangent(x,y)
    #The coordinates of new points are recieved and are updated
    sum += r[2]
    #The distance is added up
    x,y = r[0],r[1]
# Code stops when we just clear x axis
print("Value of pi is:",2*sum)
# By defination pi = circumference/diamter = 4*arc length / 2*radius = 2*arc length as radius = 1 in our case

#Note: Here trignometry is used but only the identites which are derived from right angled triangles, value of trig functions for angles is not used. 