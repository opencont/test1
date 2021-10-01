from superfastcode import vol
from superfastcode import SliceCalculation, BishopMethod
import numpy as np
from math import sqrt
import array
from random import random
from random import sample
from random import uniform
from constants import S, S1, a_min, a_max, b_min, b_max, R_min, R_max, slopeTop_x, slopeTop_y, slopeBottm_x, slopeBottm_y, slopeToe_x, slopeToe_y, Slope_BaseToe_x, Slope_BaseToe_y, UnitWight, cohesion, phi, Pore_pressure
from initial_values import initialise
from bounds import ensure_bounds

class Population:
    centerX = 0.0 
    centerY = 0.0 
    radius = 0.0
    fitness = 0.0
    Sa3 = 0.0
    Sa31 = 0.0
    Ua3 = 1.0
    Ua31 = 0.0

    def __init__(self, X, Y, R, Sa3, Sa31, Ua3, Ua31):
        self.centerX = X
        self.centerY = Y
        self.radius = R
        self.Sa3 = Sa3
        self.Sa31 = Sa31
        self.Ua3 = Ua3
        self.Ua31 = Ua31
    
    def setcenterX(self, centerX):
        self.centerX = centerX

    def setcenterY(self, centerY):
        self.centerY = centerY
    
    def setRadius(self, radius):
        self.radius = radius

    def setfitness(self, fitness):
        self.fitness = fitness

    def setSa3(self, Sa3):
        self.Sa3 = Sa3
        
    def setSa31(self, Sa31):
        self.Sa31 = Sa31

    def setUa3(self, Ua3):
        self.Ua3 = Ua3

    def setUa31(self, Ua31):
        self.Ua31 = Ua31

population = np.empty(S, dtype = float)
SliceWidth = 0.0
base_angle = np.empty(S1, dtype = float)
height = np.empty(S1, dtype = float)
Weight = np.empty(S1, dtype = float)
        
#--- FUNCTIONS ----------------------------------------------------------------+

def minimize(population, popsize, mutate, recombination, maxiter):
         
    #--- SOLVE --------------------------------------------+
    
    # cycle through each generation (step #2)
    for i in range(1,maxiter+1):
        print ("GENERATION:",i)
        gen_scores = [] # score keeping

        # cycle through each individual in the population
        for j in range(0, popsize):

            #--- MUTATION (step #3.A) ---------------------+
            
            # select three random vector index positions [0, popsize), not including current vector (j)
            candidates = list(range(0,popsize))
            candidates.remove(j)
            random_index = sample(candidates, 3)

            x_1 = population[random_index[0]]
            x_2 = population[random_index[1]]
            x_3 = population[random_index[2]]
            x_t = population[j]     # target individual
             
            # subtract x3 from x2, and create a new vector (x_diff)
            #x_diff = [x_2_i - x_3_i for x_2_i, x_3_i in zip(x_2, x_3)]
            x_diff = [x_2[0] - x_3[0], x_2[1] - x_3[1], x_2[2] - x_3[2]]

            # multiply x_diff by the mutation factor (F) and add to x_1
            #v_donor = [x_1_i + mutate * x_diff_i for x_1_i, x_diff_i in zip(x_1, x_diff)]
            v_donor = [x_1[0] + mutate*x_diff[0], x_1[1] + mutate*x_diff[1], x_1[2] + mutate*x_diff[2]]
            v_donor = ensure_bounds(v_donor)
            v_donor = v_donor.T

            #--- RECOMBINATION (step #3.B) ----------------+
            
            v_trial = []
            for k in range(len(x_t)):
                crossover = random()
                if crossover <= recombination:
                    v_trial.append(v_donor[k])

                else:
                    v_trial.append(x_t[k])
                    
            #--- GREEDY SELECTION (step #3.C) -------------+
            radius = v_donor[0] 
            slipcircle_center_x = v_donor[1]   
            slipcircle_center_y = v_donor[2]
            slipcircleintersection_toe_x = v_donor[3]           
            slipcircleintersection_toe_y = v_donor[4]         
            slipcircleintersection_crest_x = v_donor[5]         
            slipcircleintersection_crest_y = v_donor[6]       
            
            score_trial  = SliceCalculation(SliceWidth, radius, slipcircle_center_x, slipcircle_center_y, slipcircleintersection_toe_x, slipcircleintersection_toe_y, slipcircleintersection_crest_x, slipcircleintersection_crest_y)
            
            radius = x_t[0] 
            slipcircle_center_x = x_t[1]   
            slipcircle_center_y = x_t[2]
            slipcircleintersection_toe_x = x_t[3]           
            slipcircleintersection_toe_y = x_t[4]         
            slipcircleintersection_crest_x = x_t[5]         
            slipcircleintersection_crest_y = x_t[6]       
           
            score_target  = SliceCalculation(SliceWidth, radius, slipcircle_center_x, slipcircle_center_y, slipcircleintersection_toe_x, slipcircleintersection_toe_y, slipcircleintersection_crest_x, slipcircleintersection_crest_y)

            #score_target = cost_func(x_t)

            if score_trial < score_target:
                population[j] = v_trial
                gen_scores.append(score_trial)
               #print( '   >',score_trial, v_trial)

            else:
                #print( '   >',score_target, x_t)
                gen_scores.append(score_target)

        #--- SCORE KEEPING --------------------------------+

        gen_avg = sum(gen_scores) / popsize                         # current generation avg. fitness
        gen_best = max(gen_scores)                                  # fitness of best individual
        gen_sol = population[gen_scores.index(max(gen_scores))]     # solution of best individual

        print ('      > GENERATION AVERAGE:',gen_avg)
        print ('      > GENERATION BEST:',gen_best)
        print ('         > BEST SOLUTION:',gen_sol,'\n')
        
    pass

population = initialise()
population = np.array(population)
print(population.shape)

for i in range(10):
    v_donor = population[i]
    radius = v_donor[0] 
    slipcircle_center_x = v_donor[1]   
    slipcircle_center_y = v_donor[2]
    slipcircleintersection_toe_x = v_donor[3]           
    slipcircleintersection_toe_y = v_donor[4]         
    slipcircleintersection_crest_x = v_donor[5]         
    slipcircleintersection_crest_y = v_donor[6]       
            
    k = SliceCalculation(SliceWidth, radius, slipcircle_center_x, slipcircle_center_y, slipcircleintersection_toe_x, slipcircleintersection_toe_y, slipcircleintersection_crest_x, slipcircleintersection_crest_y) 
    print(k)

maxiter = int(input("Enter Generation : "))

minimize(population, 10, 0.2, 0.7, maxiter)
