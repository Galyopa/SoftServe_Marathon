"""
The string defining the points of the quadrilateral has the next form: "#LB1:1#RB4:1#LT1:3#RT4:3"

 LB - Left Bottom point
 LT - Left Top point
 RT - Right Top point
 RB - Right Bottom point
numbers after letters are the coordinates of a point.
Write a function figure_perimetr() that calculates the perimeter of a quadrilateral

The formula for calculating the distance between points:



For example:

Test	Result
test1 = "#LB1:1#RB4:1#LT1:3#RT4:3"
print(figure_perimetr(test1))
10.0
test2 = "#LB0:1#RB5:1#LT4:5#RT8:3"
print(figure_perimetr(test2))
18.73454147995595

"""

