# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 15:40:34 2018

@author: T3
"""

def goodBadCheck (ax1,ax2,ay1,ay2,bx1,bx2,by1,by2):
    import numpy as np
    import math
    #first create a function that returns A,B,C for Ax + By = C
    def find_line_equation (x1,x2,y1,y2):
        A = y1 - y2
        B = x2 - x1
        C = A*x1 + B*y1
        return_list = [A,B,C]
        return(return_list)
    #Now if we assume that the two equations define two lines rather than line segments
    #then we should be able to find an intersection (assuming the lines have different slopes).
    
    #Given the values for the line segment end points we can find the lenth of the line segment
    def length_of_line_segment(ax1,ax2,ay1,ay2):
        length_of_segment = ((ax1-ax2)**2 + (ay1-ay2)**2)**.5
        return(length_of_segment)
        
    #This code finds the intersection f=of two lines (not line segments)
    def find_the_intersection_point (list_1, list_2):
      coefficient_matrix = np.matrix([[list_1[0], list_1[1]],[list_2[0],list_2[1]]])
      RHS_matrix = np.matrix([[list_1[2]],[list_2[2]]])
      inverse_coefficient_matrix = coefficient_matrix.I
      solution = inverse_coefficient_matrix.dot(RHS_matrix)
      return(solution)
    
    #This uses the previous two functions to give back a specific answer as to whether the two
    #line segments intersect (knowing their endpoint coordinates).
    def line_segments_intersect (ax1,ax2,ay1,ay2,bx1,bx2,by1,by2):
      a_coefficients = find_line_equation(ax1,ax2,ay1,ay2) #reference the earlier function
      b_coefficients = find_line_equation(bx1,bx2,by1,by2) #reference the earlier function
      intersection_point = find_the_intersection_point(a_coefficients, b_coefficients) #reference the earlier function
      #Now find the boundaries of the line segments. 
      min_ax = int(min(ax1,ax2)); max_ax = int(max(ax1,ax2))
      min_ay = int(min(ay1,ay2)); max_ay = int(max(ay1,ay2))
      min_bx = int(min(bx1,bx2)); max_bx = int(max(bx1,bx2))
      min_by = int(min(by1,by2)); max_by = int(max(by1,by2))
      #If the intersection is within the boundaries
      #defined by the most extreme values of the coordinates then we can be assured that the
      #line segments actually do intersect. The following if statement returns the necessary 
      #TRUE or FALSE that we want to see in order to move on.
      if ((min_ax <= intersection_point[0] <= max_ax) and \
          (min_ay <= intersection_point[1] <= max_ay) and \
          (min_bx <= intersection_point[0] <= max_bx) and \
          (min_by <= intersection_point[1] <= max_by)):
          return(True)
      else:
          return(False)
          
    #Initial setup for testing 1
    #ax1 = 10000
    #ax2 = 20000
    #ay1 = 10000
    #ay2 = 10000
    #bx1 = 14131.75911
    #bx2 = 15868.24088
    #by1 = 5000
    #by2 = 15000
    
    #Initial setup for testing 2
    A1 = find_line_equation(ax1,ax2,ay1,ay2)[0]
    B1 = find_line_equation(ax1,ax2,ay1,ay2)[1]
    C1 = find_line_equation(ax1,ax2,ay1,ay2)[2]
    A2 = find_line_equation(bx1,bx2,by1,by2)[0]
    B2 = find_line_equation(bx1,bx2,by1,by2)[1]
    C2 = find_line_equation(bx1,bx2,by1,by2)[2]
    
    #Manual input for how much of an angle we allow there to be between the line segments
    #angle_threshold = int(input("When the lines are greater than this angle (degrees) from  perpendicular then eliminate them from consideration: "))
    angle_threshold = 10
    
    if(length_of_line_segment(ax1,ax2,ay1,ay2) != 0): #Is first line not a point?
    #Due to math limitations we have to deal with cases of vertical lines  first.
    #If a line is vertical then it has slope infinity.
        slopeAEE = 0
        slopeBEE = 0
        slopes_are_different = False
        if(B1 == 0):
            slopeAEE = float("inf")
            if(B2 != 0):
                slopes_are_different = True
        else:
            slopeAEE = -A1/B1
        if(B2 == 0):
            slopeBEE = float("inf")
            if(B1 != 0):
                slopes_are_different = True
        else:
            slopeBEE = -A2/B2    
        slopes_are_different = (slopeAEE!=slopeBEE) #If the slopes are different then set the flag appropriately
        if(slopes_are_different):
            if(slopeAEE==0 and slopeBEE==float("inf")):
                intersection_point = [bx1,ay1]
            elif(slopeAEE==float("inf") and slopeBEE==0):
                intersection_point = [ax1,by1]
            else:
                intersection_point_inputs_1 = find_line_equation(ax1,ax2,ay1,ay2)
                intersection_point_inputs_2 = find_line_equation(bx1,bx2,by1,by2)
    #           Calculate intersection with matrix method
                intersection_point = find_the_intersection_point(intersection_point_inputs_1,intersection_point_inputs_2)
            min_ax = float(min(ax1,ax2)); max_ax = float(max(ax1,ax2))
            min_ay = float(min(ay1,ay2)); max_ay = float(max(ay1,ay2))
            min_bx = float(min(bx1,bx2)); max_bx = float(max(bx1,bx2))
            min_by = float(min(by1,by2)); max_by = float(max(by1,by2))
      #This if statement returns the necessary TRUE or FALSE that we want to see in order to move on.
            if ((min_ax <= float(intersection_point[0]) <= max_ax) and \
                (min_ay <= float(intersection_point[1]) <= max_ay) and \
                (min_bx <= float(intersection_point[0]) <= max_bx) and \
                (min_by <= float(intersection_point[1]) <= max_by)):
                the_line_segments_intersect = True
                return(True) #good intersection
            else:
                the_line_segments_intersect = False
                return(False) #bad intersection
        if(slopeAEE*slopeBEE != -1 and slopeAEE != float("inf") and slopeBEE != float("inf")):    #slopes are not perpendicular 
            angle_between_the_lines = np.arctan(abs((slopeAEE-slopeBEE)/(1+slopeAEE*slopeBEE))) #gives the angle between 0 and pi/2 (0 and 90 degrees)
        elif(slopeAEE*slopeBEE == -1 or \
             (slopeAEE == float("inf") and slopeBEE == 0) or \
             (slopeBEE == float("inf") and slopeAEE == 0)): #slopes are perpendicular
    #			Then angle is pi/2
            angle_between_the_lines = math.pi/2
        else:
            angle_between_the_lines = 0
        if(abs(angle_between_the_lines-math.pi/2)>angle_threshold*math.pi/180):
            return(False) #bad intersection
    else:
        return(False) #bad intersection

print(goodBadCheck(0,0,0,0,0,0,0,0))