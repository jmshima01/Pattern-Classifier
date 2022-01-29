"""
Linear Classifier
by - James Shima
"""

#libraries
import numpy as num
import numpy as np
import csv
import matplotlib.pyplot as plt
import math

#points (x,y,class)
with open("points.csv") as file:
    data = csv.reader(file)

    points = []
    j = 0
    for i in data:
        #flag skip 1st line:
        if(j!= 0):
            points.append(i)
        j+=1

    
    points = [[float(string) for string in j] for j in points]
    #print(points)
    
    for point in points:
        if int(point[2]) == 1:
            plt.scatter(point[0], point[1], color="blue")
        else:
            plt.scatter(point[0], point[1],  color= "red")
    
    
    
    
    #Naming plot
    plt.ylabel('y axis')
    plt.title('Linear Classification')
    
    #finding avg points of both classes:
    x_avg_1 = 0
    y_avg_1 = 0
    x_avg_2 = 0
    y_avg_2 = 0
    num_of_pts = len(points)
    
    for point in points:
        if int(point[2]) == 1:
            x_avg_1 += point[0]
            y_avg_1 += point[1]
        else:
            x_avg_2 += point[0]
            y_avg_2 += point[1]
    
    x_avg_1 /= 10
    y_avg_1 /= 10
    x_avg_2 /= 10
    y_avg_2 /= 10
    
    print("xavg: ", x_avg_1)
    midpoint = [(x_avg_1+x_avg_2)/2, (y_avg_1+y_avg_2)/2]
    
    plt.scatter(midpoint[0], midpoint[1], color= "orange")
    plt.scatter(x_avg_1, y_avg_1,  color= "green")
    plt.scatter(x_avg_2, y_avg_2,  color= "green")
    
    avg_slope = (y_avg_2-y_avg_1)/(x_avg_2-x_avg_1)
    orthog_slope = (1/avg_slope) * -1
    #y-mx = b
    b = midpoint[1] - (orthog_slope*midpoint[0])
    print (f"b: {b}")
    
    print(f"AVG SLOPE: {avg_slope}")
    avg_line = []
    avg_line.append(avg_slope)
    avg_line.append((x_avg_1*avg_slope)+y_avg_1)
    
    x_avgs= [x_avg_1,x_avg_2]
    y_avgs = [y_avg_1,y_avg_2]
    plt.plot(x_avgs,y_avgs)
    
    x = [-4,6]
    y = [(orthog_slope*-4)+b,(orthog_slope*6)+b]
    plt.plot(x,y)
        
    
    print(f"The Equation of the line is:\ny - {midpoint[1]} = {orthog_slope}(x - {midpoint[0]})")
    output = f"y - {midpoint[1]} = {orthog_slope}(x - {midpoint[0]})"
    
    
    
    plt.plot(x,y)
    
    plt.xlabel("line: " + output)
    plt.xlim(-10,10)
    plt.ylim(-10,10)
    plt.show()
    
        
    