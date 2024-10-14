import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carrega o Df
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Filtra o DF
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]

def draw_line_plot():
    # Cria o gráfico de linhas
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df['value'], color='red', linewidth=1)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.grid(True)
    
    # Salva a figura nos arquivos
    plt.savefig('line_plot.png')
    return plt.gcf()

def draw_bar_plot():
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    # Agrupa por ano e mês
    df_bar_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Desenha o gráfico de barras
    df_bar_grouped.plot(kind='bar', figsize=(10, 6))
    plt.title('Average Page Views per Month')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=[
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ])
    plt.xticks(rotation=45)
    
    # Salva the figure
    plt.savefig('bar_plot.png')
    return plt.gcf()

def draw_box_plot():
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box['date']]
    df_box['month'] = [d.strftime('%b') for d in df_box['date']]
    months_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Desenha o box 
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    
    sns.boxplot(x='year', y='value', data=df_box, ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')

    sns.boxplot(x='month', y='value', data=df_box, order=months_order, ax=ax2)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')

    # Salva a figura 
    fig.savefig('box_plot.png')
    return fig
