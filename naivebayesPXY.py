#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Nigel
@author: Yichen
@author: M.Joo (smoothing with all zeros)
"""

import numpy as np

def naivebayesPXY(x, y):
# =============================================================================
#    function [posprob,negprob] = naivebayesPXY(x,y);
#
#    Computation of P(X|Y)
#    Input:
#    x : n input vectors of d dimensions (dxn)
#    y : n labels (-1 or +1) (1xn)
#
#    Output:
#    posprob: dx1 probability vector with entries p(x_alpha = 1|y=+1)
#    negprob: dx1 probability vector with entries p(x_alpha = 1|y=-1)
# =============================================================================



    # Convertng input matrix x and y into NumPy matrix
    # input x and y should be in the form: 'a b c d...; e f g h...; i j k l...'
    # TODO: do not use np.matrix!
    X = np.matrix(x)
    Y = np.matrix(y)

    d,n = X.shape

    # Pre-constructing a matrix of all-ones (dx2)
    X0 = np.ones((d,2))
    Y0 = np.array([[-1, 1]])

    # add one all-ones positive and negative example
    Xnew = np.hstack((X, X0)) #stack arrays in sequence horizontally (column-wise)
    Ynew = np.hstack((Y, Y0))

    # matrix of all-zeros -
    X1 = np.zeros((d, 2))
    # add one all-zeros positive and negative example - M.Joo
    Xnew = np.hstack((Xnew, X1))
    Ynew = np.hstack((Ynew, Y0))

    # Re-configuring the size of matrix Xnew
    d,n = Xnew.shape

# =============================================================================
# fill in code here
    # YOUR CODE HERE
    
    d,n = X.shape
    posprob = np.ones((d,1))
    negprob = np.ones((d,1))

    for j in range(d):
        pos_y = 0
        pos_x = 0
        neg_y = 0
        pos_x_1 = 0
        for i in range(n):
            if (Y[0,i] == 1):
                pos_y = pos_y +1
                if(X[j,i] == 1):
                    pos_x = pos_x +1
            else:
                neg_y = neg_y +1
                if(X[j,i]== 1):
                    pos_x_1 = pos_x_1 +1
        theta_p = (pos_x+1)/(pos_y+2)
        theta_n = (pos_x_1+1)/(neg_y+2)

        posprob[j,0] = theta_p
        negprob[j,0] = theta_n
        
        
    return posprob,negprob

# =============================================================================
