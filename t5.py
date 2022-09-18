import matplotlib.pyplot as mtplt
import numpy as np
import pylab as plt

a = np.array([1,2,3,4,5,6,7,8,9,10])
b = np.array([7,8,6,3,2,1,5,8,4,15])
c = plt.plot(a,b,'.')
d = 5
plt.text(0.5,
         0.67,
         "d = {}".format(d),
         transform=plt.gca().transAxes)

plt.show()