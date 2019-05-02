# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 00:48:23 2018

@author: Admin
"""

import numpy as np
from numpy.random import randn


answer = ""
x = randn()
if (x > 1):
    answer = "Greater than 1"
else:
    answer = "Less than 1"
print(x)
print(answer)

type(answer)

example = None
example = 5 + 4
type(example)