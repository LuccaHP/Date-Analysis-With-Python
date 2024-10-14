import mean_var_std
from unittest import main
import numpy as np

def calcular():

    lista = input("Digite 9 números separados por vírgula: ")
    list = [int(x) for x in lista.split(",")]


    if len(list) != 9:
        raise ValueError("Digite 9 números!")

    matriz = np.array(list).reshape(3, 3)


    calculoMatriz = {
        'mean': [matriz.mean(axis=0).tolist(), matriz.mean(axis=1).tolist(), matriz.mean().tolist()],
        'variance': [matriz.var(axis=0).tolist(), matriz.var(axis=1).tolist(), matriz.var().tolist()],
        'standard deviation': [matriz.std(axis=0).tolist(), matriz.std(axis=1).tolist(), matriz.std().tolist()],
        'max': [matriz.max(axis=0).tolist(), matriz.max(axis=1).tolist(), matriz.max().tolist()],
        'min': [matriz.min(axis=0).tolist(), matriz.min(axis=1).tolist(), matriz.min().tolist()],
        'sum': [matriz.sum(axis=0).tolist(), matriz.sum(axis=1).tolist(), matriz.sum().tolist()]
    }

    return calculoMatriz


print(calcular())