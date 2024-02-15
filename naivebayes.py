#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Nigel
"""

import numpy as np
from naivebayesPY import naivebayesPY
from naivebayesPXY import naivebayesPXY

def naivebayes(x, y, x1):
# =============================================================================
#function logratio = naivebayes(x,y,x1);
#
#Computation of log P(Y|X=x1) using Bayes Rule
#Input:
#x : n input vectors of d dimensions (dxn)
#y : n labels (-1 or +1)
#x1: input vector of d dimensions (dx1)
#
#Output:
#logratio: log (P(Y = 1|X=x1)/P(Y=-1|X=x1))
# =============================================================================


    
    # Convertng input matrix x and x1 into NumPy matrix
    # input x and y should be in the form: 'a b c d...; e f g h...; i j k l...'
    X = np.matrix(x)
    X1= np.matrix(x1)
    
    # Pre-configuring the size of matrix X
    d,n = X.shape
    
# =============================================================================
# fill in code here
    # YOUR CODE HERE

    

    XY_pos,XY_neg = naivebayesPXY(X,y)
    Y_pos,Y_neg = naivebayesPY(X,y)
    log_pos = (XY_pos * Y_pos)
    log_neg = (XY_neg * Y_neg)
    #logratio = np.log(np.divide(log_pos,log_neg))
    #logratio = (np.log(XY_pos)+np.log(Y_pos)) - (np.log(XY_neg)+np.log(Y_neg))
    logratio = np.log(Y_pos) - np.log(Y_neg) + np.transpose(X1)@(np.log(XY_pos)) - np.transpose(X1)@(np.log(XY_neg))    
    
    
    
    
    return logratio
# =============================================================================
