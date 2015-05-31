# -*- coding: utf-8 -*-
"""
Created on Fri May 31 23:01:34 2015

@author: ccgoh


Documentation:
http://hubonit.com/wiki/index.php?title=2D_Newton_Raphson_method


This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
#Circle Trilateration using Newton Raphson method
from numpy import matrix
import numpy as np
count = 1
for x in range(0,100):
    if count == 1:
        X = 0.1
        Y = 1
    #f1 = X + X*X*Y*Y -2*Y + 3
    #f2 = Y - X*X*X + 2*X*Y*Y - 2
    f1 = X*X - 10*X + Y*Y - 10*Y + 34
    f2 = X*X - 22*X + Y*Y - 10*Y + 130
    if f1 == 0 and f2==0:
        break
    print "\r\nIteration=%d" %count
    count += 1
    print "f1= %f" %(f1)
    print "f2=%f" %(f2)
    #A = 1 + 2*X*Y*Y
    #B = 2*Y*X*X -2
    #C = -3*X*X + 2*Y*Y
    #D = 1 + 4*X*Y    
    A = 2*X - 10
    B = 2*Y - 10
    C = 2*X - 22
    D = 2*Y - 10
    print A,B
    print C,D
    J = np.matrix([[A,B],[C,D]]).I  #Jacobian matrix
    f3 = np.matrix([[f1],[f2]])
    T = np.matrix([[X],[Y]])
    Delta = J*f3
    E = T-Delta
    X = np.squeeze(np.asarray(E[0]))
    Y = np.squeeze(np.asarray(E[1]))
    print J
    #print Delta
    #print E    
    print "X=%f, Y=%f" %(X,Y)
