#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 31 16:30:59 2025

@author: stanislawkiedrzynski
"""
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from scipy.interpolate import make_interp_spline

def plot_smooth_election_curve(X, Y, c, smooth_factor=100):

    # Step 1: Average duplicate X values
    sum_dict = defaultdict(float)
    count_dict = defaultdict(int)

    for x, y in zip(X, Y):
        sum_dict[x] += y
        count_dict[x] += 1

    X_unique = np.array(sorted(sum_dict.keys()))
    Y_avg = np.array([sum_dict[x] / count_dict[x] for x in X_unique])



    X_smooth = np.linspace(X_unique.min(), X_unique.max(), smooth_factor)

    # Step 3: Cubic spline smoothing
    spline = make_interp_spline(X_unique, Y_avg, k=3)
    Y_smooth = spline(X_smooth)

    # Step 4: Plot
    plt.plot(X_smooth, Y_smooth, '--', color=c)

#[year, PO-led, PiS-led, turnout, gov, Right, Centre, Left] gov: 1 - PiS, 0 - PO
parl23 = [2023, 30.70, 35.39, 74.38, 1, 35.39 + 7.17 + 1.86 + 1.63, 30.70 + 14.41, 8.61]
parl19 = [2019, 27.40, 43.59, 61.74, 1, 43.59 + 6.81, 27.40 + 8.55, 12.56]
parl15 = [2015, 24.09, 37.58, 50.92, 0, 37.58 + 4.76 + 8.81, 24.09 + 5.13, 7.55 + 3.62]
parl11 = [2011, 39.18, 29.89, 48.92, 1, 29.89 + 2.19 + 1.06 + 0.24, 39.18 + 8.36, 10.02 + 8.24]
parl07 = [2007, 41.51, 32.11, 53.88, 1, 32.11 + 1.53 + 1.30, 41.51 + 8.91, 13.15]
parl05 = [2005, 24.14, 26.99, 40.57, 2, 26.99 + 11.41 + 7.97, 24.14 + 6.96, 11.31]

parliamentary = [parl23,parl19, parl15, parl11, parl07, parl05]
presidential = [
    [2005, 36.3, 33.1, 49.7, 2, 33.1 + 15.1 + 1.43, 36.3 + 1.8 + 1.4 + 1.23 , 10.3],
    [2010, 41.5, 36.5, 54.92, 1, 36.5 + 2.5 + 1.06 + 1.22 , 41.5 + 1.75 + 1.44, 13.68],
    [2015, 33.77, 34.76, 48.96, 0, 34.76 + 20.8 + 3.26 + 0.83 + 0.46 + 0.2, 33.77 + 1.6, 2.38],
    [2020, 30.46, 43.5, 64.51, 1, 43.5 + 6.78 + 0.23 + 0.17 + 0.14  + 0.11, 30.46 + 2.36 + 13.87, 2.22 + 0.14],
    [2025, 31.1, 29.5, 74.38, 1, 29.5 + 14.8 + 6.8 + 1.2 + 0.09 + 0.8 + 0.5, 31.1 + 4.99, 4.86 + 4.23 + 1.09]
]
parliamentary = [parl23, parl19, parl15, parl11, parl07, parl05]

years = [par[0]-2000 for par in parliamentary]
po_values = [par[3]*par[1]/100 for par in parliamentary]
pis_values = [par[3]*par[2]/100 for par in parliamentary]
non_voters = [100 - par[3] for par in parliamentary]
#other = [100 - po - pis - nv for po, pis, nv in zip(po_values, pis_values, non_voters)]



years = years + [par[0]-2000 for par in presidential]
po_values = po_values + [par[3]*par[1]/100 for par in presidential]
pis_values = pis_values + [par[3]*par[2]/100 for par in presidential]
non_voters = non_voters + [100 - par[3] for par in presidential]
other = [100 - po - pis - nv for po, pis, nv in zip(po_values, pis_values, non_voters)]

# Plot lines
plt.scatter(years, po_values, color='orange', label='PO-led', s = 100, edgecolors='black')
plt.scatter(years, pis_values, color='blue', label='PiS-led', s = 100, edgecolors='black')
plt.scatter(years, non_voters, color='black', label='Non-voters', s = 100, edgecolors='black')
plt.scatter(years, other, color='grey', label='Other', s = 100, edgecolors='black')

plot_smooth_election_curve(years, pis_values, 'blue')
plot_smooth_election_curve(years, po_values, 'orange')
plot_smooth_election_curve(years, other, 'grey')
plot_smooth_election_curve(years, non_voters, 'black')


# Final polish
plt.title("Polish Elections: Participation by Bloc")
plt.xlabel("Year")
plt.ylabel("Percentage of Eligible Voters")
plt.legend(fontsize = 9)
plt.grid(True)
plt.tight_layout()
plt.show()


years = [par[0]-2000 for par in parliamentary]
Right= [par[3]*par[5]/100 for par in parliamentary]
Centre = [par[3]*par[6]/100 for par in parliamentary]
Left  = [par[3]*par[7]/100 for par in parliamentary]
non_voters = [100 - par[3] for par in parliamentary]




years = years + [par[0]-2000 for par in presidential]
Right = Right + [par[3]*par[5]/100 for par in presidential]
Centre = Centre + [par[3]*par[6]/100 for par in presidential]
Left = Left + [par[3]*par[7]/100 for par in presidential]
non_voters = non_voters + [100 - par[3] for par in presidential]

# Plot lines
plt.scatter(years, Right, color='blue', label='Right', s = 100, edgecolors='black')
plt.scatter(years, Centre, color='orange', label='Centre', s = 100, edgecolors='black')
plt.scatter(years, Left, color='green', label='Left',  s = 100, edgecolors='black')
plt.scatter(years, non_voters, color='black', label='Non-voters',  s = 100, edgecolors='black')

plot_smooth_election_curve(years, Right, 'blue')
plot_smooth_election_curve(years, Centre, 'orange')
plot_smooth_election_curve(years, Left, 'green')
plot_smooth_election_curve(years, non_voters, 'black')


# Final polish
plt.title("Polish Elections by sides of spectrum")
plt.xlabel("Year")
plt.ylabel("Percentage of Eligible Voters")
plt.legend(fontsize=9)
plt.grid(True)
plt.tight_layout()
plt.show()

for i in range(0,11):
    print(str(years[i])+': ' + str(Right[i]+Centre[i]+Left[i]+non_voters[i]) )