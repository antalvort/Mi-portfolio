import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x=df['Year']
    y=df['CSIRO Adjusted Sea Level']
    plt.scatter(x,y)
   

    # Create first line of best fit
    res=linregress(x,y)
    x_pred=pd.Series([i for i in range(1880,2051)])
    y_pred=res.slope*x_pred+res.intercept
    plt.plot(x_pred,y_pred,'g')

    # Create second line of best fit
    filter=df.loc[df['Year']>=2000]
    x_new=filter['Year']
    y_new=filter['CSIRO Adjusted Sea Level']
    res_new=linregress(x_new,y_new)
    x_pred_new=pd.Series([i for i in range(2000,2051)])
    y_pred_new=res_new.slope*x_pred_new+res_new.intercept
    plt.plot(x_pred_new,y_pred_new, 'r')
    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()