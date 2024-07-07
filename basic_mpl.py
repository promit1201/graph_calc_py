import matplotlib.pyplot as mpl
import pandas as ps
import math
import numpy as np  
xrr=[1,2,3,4,5,6,7,8]      
yrr=[0.3,0.5,0.6,0.7,0.8,1,1.35,1.5] 

#figsize
mpl.figure(figsize=(5,3), dpi=300)   

mpl.title('Our first graph!',fontdict={"fontname":"Comic Sans MS","fontsize":20})


#(xlabel, ylabel)
#mpl.plot(xrr,yrr,label="0.1x", color = "r", lw =5, marker =".", mew=6)  #can pass hexadecimal colors, in some cases short forms as well

#shorthand notation
mpl.plot(xrr,yrr,"b^--",label="0.1x", lw =5, mew=6)

#r=color, --=linsestyle, ^= marker; fmt=<color><marker><line>

#line 2
xarr2=np.arange(0,4.5,0.5) #arange(start, stop, step)
mpl.plot(xarr2[:6],xarr2[:6]**2,"r.-",label="x**2")
mpl.plot(xarr2[5:],(xarr2[5:])**2,"r.--")

#sin graph trial
#pl.plot(xarr2, math.sin(xarr2))

#graph labels
mpl.xlabel("x axis")
mpl.ylabel("y axis")

#graph scale
mpl.xticks([0,2,4,6,8])   #use (x/y)ticks() to resize graph
#mpl.yticks([0,0.2,0.4,0.6,0.8])         #ticks includes origin marker 0

mpl.legend()
mpl.savefig("FirstGraph.png",dpi=300)
mpl.show()

# first figsize, plot, then rest of the functions, lastly show and just b4 show, save