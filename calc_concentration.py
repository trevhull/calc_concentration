#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 14:51:49 2018

@author: trevario
"""

#Simple Concentration Calculator



print("What solvent are you using? (hexanes, toluene, benzene, chloroform)")
solv = input()
if solv.lower() == 'hexanes':
    solvent_density = 0.672
elif solv.lower() == 'toluene':
    solvent_density = 0.87
elif solv.lower() == 'benzene':
    benzene_density = 0.8765
elif solv.lower() == 'chloroform':
    chloroform_density = 1.564
else:
    print('I do not know that one. sorry')
    exit

print("what is your cuvette concentration (M)?")
C1 = float(input())

print("what is your sample volume in cuvette (mL)?")
V2 = float(input())

print("did you add solvent by mass or by volume? (answer mass or volume)")
ans = input()
if ans.lower() == 'mass':
    print("what is your solvent mass in cuvette (g)?")
    Vg = float(input())
    V1 = Vg/solvent_density
    
    
if ans.lower() == 'volume':

    print("what is your solvent volume in cuvette (mL)?")
    V1 = float(input())



C2 = C1*V1/V2
Cf = round(C2, 5)
print('the stock solution is: ' + str(Cf) + ' M')
