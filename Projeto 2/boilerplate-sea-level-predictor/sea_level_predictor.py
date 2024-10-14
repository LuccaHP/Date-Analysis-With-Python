import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Cria o df com base no banco de dados
    df = pd.read_csv('epa-sea-level.csv')

    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data', color='blue')

    # Ano 1880 - 2050
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_ext = pd.Series([i for i in range(1880, 2051)])
    plt.plot(years_ext, intercept + slope * years_ext, label='Best fit line 1880-2050', color='green')

    # Ano 2000 - 2050
    df_2000 = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    years_ext_2000 = pd.Series([i for i in range(2000, 2051)])
    plt.plot(years_ext_2000, intercept_2000 + slope_2000 * years_ext_2000, label='Best fit line 2000-2050', color='red')

    # Adiciona labels e título
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Salva o gráfico como arquivo
    plt.savefig('sea_level_plot.png')
    return plt.gca()
