# multiplot
Plot multiple (upto four) graphs in different scales in a single figure with scrollable x (horizontal) axis. 

## Sample Usage
```python
import numpy as np
import pandas as pd 
import multiplot

t = np.arange(0.01, 10.0, 0.001)

df = {'x':t, 'sin(x)':np.sin(5*np.pi*t), 'cos(x)':np.sin(10*np.pi*t), 'sin^2(x)':np.power(np.sin(15*np.pi*t),2), 'sinc(x)':np.sinc(5*np.pi*t)}

df = pd.DataFrame(df)

multiplot.multiplot(df['x'], 300, [df['sin(x)'], df['cos(x)'],df['sin^2(x)'],df['sinc(x)']])
```

## OUTPUT 

![alt text](https://github.com/orionfoysal/multiplot/blob/master/test.gif)


## Load from excel or csv file 
```python
import numpy as np 
import pandas as pd 
from multiplot import multiplot
import multiplot

df = pd.read_excel('test_data.xls')

x = df['Receive Time']
y1 = df['Voltage']
y2 = df['Velocity']
x = pd.to_datetime(x)
multiplot.multiplot(x, 50, [y1,y2])
```
## OUTPUT
![alt text](https://github.com/orionfoysal/multiplot/blob/master/3.png)
