import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df =df=pd.read_csv('medical data visualizer/medical_examination.csv')

# 2
df['height_m']=df['height']/100
df['imc']=(df['weight'])/(df['height_m']**2)
df['overweight']=df['imc'].apply(lambda x:1 if x>25 else 0)

# 3
df['cholesterol']=df['cholesterol'].apply(lambda x:0 if x==1 else 1)
df['gluc']=df['gluc'].apply(lambda x:0 if x==1 else 1)
# 4
def draw_cat_plot():
    
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # 6
    df_cat = df_cat.rename(columns={'variable': 'feature', 'value': 'condition'}, inplace=True)
    

    # 7
    figura=sns.catplot(x='feature', hue='condition', kind='count', col='cardio', data=df_cat)


    # 8
    fig = figura.figure


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    quantile_25=df['height'].quantile(0.025)
    quantile_97=df['height'].quantile(0.975)
    
    percentil25_peso=df['weight'].quantile(0.025)
    percentil975_peso=df['weight'].quantile(0.975)
   
    # 11
    df_heat = df[(df['weight']>=percentil25_peso)& (df['weight']<=percentil975_peso)&   
    (df['height']>=quantile_25)&(df['height']<=quantile_97)]
    # 12
    corr =df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    plt.figure(figsize=(12,8))
    plt.title('Correlation medical data')

    # 15
    fig=sns.heatmap(data=corr, mask=mask, cmap='coolwarm',annot=True)


    # 16
    fig.savefig('heatmap.png')
    return fig
