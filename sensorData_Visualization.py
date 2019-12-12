
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns  # visualization tool

# get dataset from directory
data = pd.read_csv('/kaggle/input/sensor-data/dataset.csv')

# shows first 10 row
data.head(10)

"""
#correlation map  
Determines the relationship between these two variables when an individual has two measurements.
As a result of correlation analysis, whether there is a linear relationship and the degree of this relationship,if any, is calculated with the correlation coefficient.

0.00 No relationship
0.01 – 0.29 low level relationship
0.30 – 0.70 moderate relationshipi
0.71 – 0.99 high level relationship
1.00        perfect relationship
    
annot -> makes text appear
linewidth -> degree of margin
fmt -> determines the number of decimal places to display
ax -> Plot size to be displayed as preset 18x18
    
"""
f,ax = plt.subplots(figsize = (18,18))
sns.heatmap(data.corr(),annot = True , linewidth =.5 , fmt= '.1f' , ax = ax)

data.plot(kind='line', x ='ID', y='Temperature', alpha = 0.5, grid = True ,color = 'red')
plt.xlabel('20 May 2019 19:08:34 GMT -- 1 May 2019 07:02:00 GMT')
plt.ylabel('Temperature (Celcius)')
plt.title('Temperature-Time Scatter Plot')



#As we have seen on the correlation map, PM2.5 and PM10 have a perfect relationship, below we see a scatter plot

data.plot(kind='scatter', x ='PM10', y='PM2.5', alpha = 0.5, grid = True ,color = 'blue')
plt.xlabel('PM10')
plt.ylabel('PM2.5')
plt.title('PM10-PM2.5 Scatter Plot \n 20 May 2019 19:08:34 GMT -- 1 May 2019 07:02:00 GMT')


# we can also filter the Dataset
filteredData = data[np.logical_and( data['Temperature']> 23, data['Humidity']> 32.5 ) ] 
print(filteredData)

# scatter plot of filtered datas
sns.scatterplot(x=filteredData.Temperature,y=filteredData.Humidity,data=data)

