#%%
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib as mlt 
x = np.linspace(0,20,100)
plt.plot(x, np.sin(x))
plt.show

#%%
for i in range(10):
    print(i)

#%%
names = ['Alice','Bob','Charlie']
for name in names:
    print(name)

#%%
s = set()
s.add(1)
s.add(3)
s.add(5)
print(s)

#%%
ages ={'Alice':22, 'Bob':25}
ages['Charlie']=30
print(ages)
ages['Alice'] += 1
print(ages)

#%%
def square(x):
    return(x*x)

for i in range(10):
    print("{} square is {}".format(i, square(i)))
