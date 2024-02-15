#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Nigel
"""

import numpy as np

def classifyLinear(x, w, b):
# =============================================================================
#function preds=classifyLinear(x,w,b);
#
#Make predictions with a linear classifier
#Input:
#x : n input vectors of d dimensions (dxn)
#w : weight vector
#b : bias
#
#Output:
#preds: predictions
# =============================================================================

    # Convertng input matrix x and x1 into NumPy matrix
    # input x and y should be in the form: 'a b c d...; e f g h...; i j k l...'
    X = np.matrix(x)
    W = np.matrix(w)
    
# =============================================================================
# fill in code here
    # YOUR CODE HERE

    w = np.transpose(w)
    preds = w @ x + b
    for i in range(preds.shape[1]):
        if preds[0,i] >= 0:
            preds[0,i] = 1
        else:
            preds[0,i] = -1
    
    
    return preds
# =============================================================================
