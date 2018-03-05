import numpy as np 
import pandas as pd 
from multiplot import multiplot

t = np.arange(0.01, 10.0, 0.001)

df = {'x':t, 'sin(x)':np.sin(5*np.pi*t), 'cos(x)':np.sin(10*np.pi*t), 'sin^2(x)':np.power(np.sin(15*np.pi*t),2), 'sinc(x)':np.sinc(5*np.pi*t)}

df = pd.DataFrame(df)

multiplot(df['x'], 300, [df['sin(x)'], df['cos(x)'],df['sin^2(x)'],df['sinc(x)']])