import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Carrega o banco de dados
df = pd.read_csv('medical_examination.csv')

# Coluna overwheight
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# Normalização de dados
df['cholesterol'] = df['cholesterol'].apply(lambda x: 1 if x > 1 else 0)
df['gluc'] = df['gluc'].apply(lambda x: 1 if x > 1 else 0)

# Desenhar gráfico (cat plot)
def draw_cat_plot():
    # Df para o gráfico
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Agrupar os dados
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).size()

    # Trocar nome da coluna
    df_cat.rename(columns={'size': 'total'}, inplace=True)

    # Desenhar o gráfico
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar').fig

    # Cria o arquivo da figura
    fig.savefig('catplot.png')
    return fig


# Desenhar mapa de calor
def draw_heat_map():
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Calcular correlação
    corr = df_heat.corr()

    # Máscara para o triângulo superior da matriz
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Desenha o mapa de calor
    fig, ax = plt.subplots(figsize=(12, 12))
    sns.heatmap(corr, annot=True, fmt='.1f', mask=mask, square=True, linewidths=1, ax=ax)

    # Cria o arquivo da figura
    fig.savefig('heatmap.png')
    return fig