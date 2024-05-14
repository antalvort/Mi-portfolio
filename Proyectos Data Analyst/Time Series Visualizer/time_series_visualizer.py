import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df=pd.read_csv('/Users/antoniojosealvarez/Desktop/Programacion/time series/fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
# Clean data
limite_superior=df['value'].quantile(0.975)
limite_inferior=df['value'].quantile(0.025)
df=df[(df['value']<limite_superior)&(df['value']>limite_inferior)]


def draw_line_plot():
    # Draw line plot
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    x=df.index
    y=df['value']
    fig=plt.plot(x,y)



    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df['month']=df.index.month
    df['year']=df.index.year
    df_bar=df.groupby(['year','month'])['value'].mean()
    df_bar=df_bar.unstack()


    # Draw bar plot
    fig=df_bar.plot.bar(figsize=(12,8),xlabel='Years',ylabel="Average Page Views",legend=True)
    plt.legend(['January','February','March','April','May','June','July','August','September','October','November','December'])




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    df_box['month_num']=df_box['date'].dt.month
    df_box=df_box.sort_values('month_num')
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18, 8))
    sns.boxplot(x=df.index.year, y='value', data=df, ax=axes[0])
    sns.boxplot(x=df.index.month_name(), y='value', data=df, ax=axes[1])

    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
