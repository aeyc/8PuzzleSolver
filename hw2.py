#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 16:54:25 2020

@author: Ayca
"""
import numpy as np
import copy
#########################################
#                                       #
#               GENERATION              #
#                                       #
#########################################
goal = [[1,2,3],[4,5,6],[7,8,-1]]
def findEmpty(l):
    col = len(l)
    row = len(l[0])
    for i in range(row):
        for j in range(col):
            if l[i][j] == -1:
                return (i,j)
"""
if mode == -1 random moves
else mode represents the directions to move
"""
def move(lst,noOfShuffle,mode):
    l = copy.deepcopy(lst)
    if mode == -1:
        for s in range(noOfShuffle):
            selection = np.random.randint(4)
            i,j = findEmpty(l)
            if selection == 0 and j !=0:
                l = right(l,i,j)
            elif selection ==1 and j!=2:
                l = left(l,i,j)
            elif selection ==2 and i!=2:
                l = up(l,i,j)
            elif selection ==3 and i!=0:
                l = down(l,i,j)
    else:
        for s in range(noOfShuffle):
            i,j = findEmpty(l)
            if mode == 0 and j !=0:
                l = right(l,i,j)
            elif mode ==1 and j!=2:
                l = left(l,i,j)
            elif mode ==2 and i!=2:
                l = up(l,i,j)
            elif mode ==3 and i!=0:
                l = down(l,i,j)
    return l

def right(l,i,j):
    l[i][j] = l[i][j-1]
    l[i][j-1] = -1
    return l
        
def left(l,i,j):
    l[i][j] = l[i][j+1]
    l[i][j+1] = -1
    return l

def up(l,i,j):
    l[i][j] = l[i+1][j]
    l[i+1][j] = -1
    return l
    
def down(l,i,j):
    l[i][j] = l[i-1][j]
    l[i-1][j] = -1
    return l

initial_states = []
i = 10
while len(initial_states)<30:
    new_state = move(goal,i,-1)
    #initial state should not be same with the goal state
    # and all initial states should be unique
    if (new_state in initial_states) or (new_state == goal): 
        i+=1
    else:
        initial_states.append((new_state))

#########################################
#                                       #
#               SOLVER                  #
#                                       #
#########################################
        
def findMisplaced(goal,current):    #set Heuristic
    count = 0
    for i in range(len(goal[0])):
        for j in range(len(goal)):
            if goal[i][j] != current[i][j]:
                count+=1
    return count

#Solve each of 30 puzzles via A* search
goal = [[1,2,3],[4,5,6],[7,8,-1]]

print(initial_states)
count = 0
succeeded = []
for i in initial_states:
    queue = []
    print("Iteration for state #: ",count)
    misplaced = findMisplaced(goal,i) #misplaced variable represents min cost
    #Form a one-element queue consisting of a zero-length path that contains only the root node
    queue.append(i)
    #Untill the first path in the queue terminates at the goal node or the queue is empty
    while goal != queue[0] and len(queue) != 0:
        ##  Remove the first path from the queue
        ##  Create new paths by extending the first path to all the neighbors of the terminal node
        for selection in range(0,4):
            inspected = move(queue[0],1,selection)
            print("Inspecting:\n",inspected)
            print("With misplacement:",findMisplaced(goal,inspected))
            ## Reject all new paths with loops
            ## If 2+ paths reach a common node, delete all those paths
            ## Except the one that reaches the common node with the min cost
            if inspected != i and misplaced>findMisplaced(goal,inspected):
                print("State approved for path:",inspected)
                misplaced = findMisplaced(goal,inspected)
                queue.append(inspected)
                queue.pop(0)
        print()
    print()
    succeeded.append((i,queue))
    count+=1
