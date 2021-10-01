import numpy as np
from math import sqrt
import array
from random import random
from random import sample
from random import uniform
from constants import S, S1, a_min, a_max, b_min, b_max, R_min, R_max, slopeTop_x, slopeTop_y, slopeBottm_x, slopeBottm_y, slopeToe_x, slopeToe_y, Slope_BaseToe_x, Slope_BaseToe_y, UnitWight, cohesion, phi, Pore_pressure



def ensure_bounds(vec):

    flag = True

    CentreA = vec[0]
    CentreB = vec[1]
    radius = vec[2]

    vec_new = []

    LineSlope = ((slopeTop_y - slopeBottm_y)/(slopeTop_x - slopeBottm_x))
    Equation_D = ((LineSlope * (- slopeBottm_x) ) + slopeBottm_y )
    Equation_A = ((radius)* (radius)* (1 + (LineSlope * LineSlope)))
    Equation_B = ((CentreB - (LineSlope * CentreA)- Equation_D )*(CentreB - (LineSlope * CentreA)- Equation_D))
    Equation_C = Equation_A - Equation_B 
    if Equation_C >= 0 :
        Equation_E = sqrt(Equation_C)
    else:
        flag = False
        Equation_E = 0.0
    U3 = ((( CentreA + ((CentreB) * (LineSlope) )-( Equation_D * LineSlope)) - Equation_E )/ (1 + (LineSlope * LineSlope)))  
    a3 = ((( CentreA + ((CentreB) * (LineSlope) )-( Equation_D * LineSlope)) + Equation_E )/ (1 + (LineSlope * LineSlope)))  
    if U3 < slopeTop_x :
        U3 = ((radius * radius)-((slopeTop_y - CentreB)*( slopeTop_y - CentreB))) 
        U3 = (-sqrt(U3)+ CentreA)
    else:
        U3 = U3
    if a3 > slopeBottm_x :
        a3 = ((radius * radius)-((slopeBottm_y - CentreB)*( slopeBottm_y - CentreB))) 
        if a3 >= 0:
            a3 = (sqrt(a3) + CentreA)
        else :
            flag = False
            a3 = 0.0
    else :
        a3 = a3 

    a31 = 0.0
    Ua31 = 0.0

    if (radius * radius)-((a3 - CentreA)*(a3 - CentreA)) >= 0:
        a31 = -sqrt((radius * radius)-((a3 - CentreA)*(a3 - CentreA))) + CentreB
    else:
        flag = False
    
    if (radius * radius)-(( U3 - CentreA)*(U3 - CentreA)) >= 0:
        Ua31 = -sqrt((radius * radius)-(( U3 - CentreA)*(U3 - CentreA))) + CentreB
    else: 
        flag = False

    if Equation_C > 0 and U3 > slopeToe_x and a3<Slope_BaseToe_x and a3>slopeTop_x and U3<slopeBottm_x and flag:
        vec_new.append((radius, CentreA, CentreB, a3, a31, U3, Ua31))
    else:
       while True:
            radius = R_min + np.random.rand()*(R_max - R_min)
            CentreA = a_min + np.random.rand()*(a_max - a_min)
            CentreB = b_min + np.random.rand()*(b_max - b_min)

            LineSlope = ((slopeTop_y - slopeBottm_y)/(slopeTop_x - slopeBottm_x))
            Equation_D = ((LineSlope * (- slopeBottm_x) ) + slopeBottm_y )       
            Equation_A = ((radius)* (radius)* (1 + (LineSlope * LineSlope)))   
            Equation_B = ((CentreB - (LineSlope * CentreA)- Equation_D )*(CentreB - (LineSlope * CentreA)- Equation_D))
            Equation_C = Equation_A - Equation_B  
            if Equation_C < 0:
                continue
            Equation_E = sqrt(Equation_C)		
                       
            U3 = ((( CentreA + ( (CentreB) * (LineSlope) )-( Equation_D * LineSlope)) - Equation_E ) / (1 + (LineSlope * LineSlope)))  
            a3 = ((( CentreA + ( (CentreB) * (LineSlope) )-( Equation_D * LineSlope)) + Equation_E ) / (1 + (LineSlope * LineSlope)))  
            if U3 < slopeTop_x: 
                U3 = ((radius * radius)-((slopeTop_y - CentreB)*( slopeTop_y - CentreB)))
                U3 = (-sqrt(U3)+ CentreA)
                                    
            else:
                U3 = U3 
            
            if a3 > slopeBottm_x :
                a3 = ((radius * radius)-((slopeBottm_y - CentreB)*( slopeBottm_y - CentreB)))
                if a3 < 0:
                    continue
                a3 = (sqrt(a3) + CentreA )
                
            else:
                a3 = a3 
                
            if Equation_C > 0 and a3 < Slope_BaseToe_x and U3 > slopeToe_x and a3 > slopeTop_x and U3 < slopeBottm_x :
                break
       a31 = -sqrt((radius * radius)-((a3 - CentreA)*(a3 - CentreA))) + CentreB
       U31 = -sqrt((radius * radius)-(( U3 - CentreA)*(U3 - CentreA))) + CentreB

       vec_new.append((CentreA, CentreB, radius, a3, a31, U3, U31))

    vec_new = np.array(vec_new)

    return vec_new
