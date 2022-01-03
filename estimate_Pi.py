# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 01:26:13 2022

@author: user
"""

import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.gridspec import GridSpec
# import matplotlib.patches as patches


def calculatePi(sample_points = 1000):
    X = np.random.uniform(low=-1, high=1, size=(sample_points,))
    Y = np.random.uniform(low=-1, high=1, size=(sample_points,))
    
    inside_circle = 0
    for x, y in zip(X, Y):
        # Checking if (x, y) lies inside the circle
        r = np.hypot(x,y)
        if r <= 1.0:
            inside_circle += 1
            
    pi = 4 * inside_circle / sample_points
    
    return pi, X, Y


 
# def createPlot(X, Y, iteration, current_pi, avg_pi, pi_values):
#     fig = plt.figure(constrained_layout=True, figsize=(10, 5))    
#     gs = GridSpec(4, 2, figure=fig)
#     ax1 = fig.add_subplot(gs[0:4, 0])
#     ax3 = fig.add_subplot(gs[0, 1])
#     ax2 = fig.add_subplot(gs[1:3, 1])
    
#     # create scatter plot of the random points
#     ax1.scatter(X, Y, color = 'r', s = 3)    
    
#     # create circcle
#     ax1.add_patch(plt.Circle((0, 0), 1, color='g', alpha=0.3)) 
#     ax1.set_xticks(np.linspace(-1, 1, 5))
#     ax1.set_yticks(np.linspace(-1, 1, 5)) 
    
#     # create Square
#     ax1.plot([-1, 1, 1, -1, -1], [-1, -1, 1, 1, -1], linewidth=2, color = 'b')
    
#     ax1.set_title(f'Iteration: {iteration} \n\u03C0 (current value): {current_pi: .4f}\n\u03C0 (running average): {avg_pi: .4f}', fontweight='bold') #, fontweight='bold'
    
#     #Use adjustable='box-forced' to make the plot area square-shaped as well.
#     ax1.set_aspect('equal', adjustable='datalim')
#     # ax1.plot()   #Causes an autoscale update.
#     ax1.axis('off')
#     ax3.axis('off')    
    
    
#     # create histogram
#     x = pi_values    
#     ax2.hist(x, color='cyan', edgecolor='k', density=False, alpha=1)

#     mu = sum(x) / len(x)
#     ax2.vlines(x=mu, ymin=0, ymax=30, colors='r', linewidth=3, label=f'Mean value: {mu: .4f}')
#     ax2.legend(loc='upper left')
#     ax2.set_xlabel('Approximation to \u03C0')
#     ax2.set_ylabel('Frequency')
    
#     fig.savefig(f"pi_{iteration}.png", dpi=100, bbox_inches='tight')
    


def monteCarloSimulation(number_of_runs):
    pi_values = []
    for i in range(number_of_runs):
        pi, X, Y = calculatePi()
        pi_values.append(pi)
        pi_average = sum(pi_values) / len(pi_values)        
        # createPlot(X, Y, iteration = i+1, current_pi = pi, avg_pi = pi_average, pi_values = pi_values)
        print(f'Iteration: {i+1} Average Pi: {pi_average}')
        
    return pi_average


if __name__ == "__main__":
    pi_avg = monteCarloSimulation(number_of_runs = 10000)    
    print(f'Estimated pi: {pi_avg}')









