#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Nigel
@author: MN (categorical/Bernoulli NB)
"""

import numpy as np
from naivebayesPY import naivebayesPY
from naivebayesPXY import naivebayesPXY

def naivebayesCL(x, y):
# =============================================================================
#function [w,b]=naivebayesCL(x,y);
#
#Implementation of a Naive Bayes classifier
#Input:
#x : n input vectors of d dimensions (dxn)
#y : n labels (-1 or +1)
#
#Output:
#w : weight vector
#b : bias (scalar)
# =============================================================================



    # Convertng input matrix x and x1 into NumPy matrix
    # input x and y should be in the form: 'a b c d...; e f g h...; i j k l...'
    X = np.matrix(x)

    # Pre-configuring the size of matrix X
    d,n = X.shape

# =============================================================================
# fill in code here
    # YOUR CODE HERE
    import math 

    theta_pos,theta_neg = naivebayesPXY(X,y)
    pi_pos,pi_neg = naivebayesPY(X,y)
    w = np.log(theta_pos) - np.log(theta_neg)
    b = math.log(pi_pos) - math.log(pi_neg)
    
    return w,b
# =============================================================================
