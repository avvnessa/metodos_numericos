# -*- coding: utf-8 -*-
"""av2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1isOgqa4I5mWcd9zzPYwV0It6FQW3a1uD
"""

import numpy as np

def jacobi(A, b, x0, tol, N):
    A = A.astype('double')
    b = b.astype('double')
    x0 = x0.astype('double')

    n = np.shape(A)[0]
    x = np.zeros(n)
    it = 0

    while it < N:
        it += 1

        for i in np.arange(n):
            x[i] = b[i]
            for j in np.concatenate((np.arange(0, i), np.arange(i + 1, n))):
                x[i] -= A[i, j] * x0[j]
            x[i] /= A[i, i]

        if np.linalg.norm(x - x0, np.inf) < tol:
            return x

        x0 = np.copy(x)

    raise NameError('Número máximo de iterações excedido.')

def gauss_seidel(A, b, tol, max_iter):
    x = np.zeros_like(b, dtype=np.double)
    for k in range(max_iter):
        x_old = x.copy()
        for i in range(A.shape[0]):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, (i + 1):], x_old[(i + 1):])) / A[i, i]
        if np.linalg.norm(x - x_old, ord=np.inf) / np.linalg.norm(x, ord=np.inf) < tol:
            return x
    return x

# Matriz A
A = np.array([[1, 2, -1, 0],
              [2, -1, 0, 0],
              [0, -1, 2, -1],
              [0, 0, -1, 2]])

# Vetor de termos independentes b
b = np.array([1, 1, 1, 1])

# Vetor inicial x0
x0 = np.array([0, 0, 0, 0])

# Tolerância
tolerance = 0.0001

# Número máximo de iterações
max_iterations = 1000

# Resolução do sistema usando o método de Jacobi
try:
    x_jacobi = jacobi(A, b, x0, tolerance, max_iterations)
    print("Solução pelo método de Jacobi:", x_jacobi)
except NameError as e:
    print(e)

# Resolução do sistema usando o método de Gauss-Seidel
solution_gauss_seidel = gauss_seidel(A, b, tolerance, max_iterations)
print("Solução pelo método de Gauss-Seidel:", solution_gauss_seidel)

import numpy as np

# Pontos de dados
x = np.array([1, 2, 3, 4])
y = np.array([2, 0.4, 3, 3.5])

# Grau do polinômio interpolador
degree = len(x) - 1

# Função de interpolação de Lagrange
def lagrange_interpolation(x, y, degree, xi):
    result = 0
    for i in range(degree+1):
        term = y[i]
        for j in range(degree+1):
            if j != i:
                term *= (xi - x[j]) / (x[i] - x[j])
        result += term
    return result

# Valores xi para interpolação
xi = np.linspace(1, 4, 100)

# Calculando os valores yi interpolados
yi = [lagrange_interpolation(x, y, degree, val) for val in xi]

# Imprimindo os coeficientes do polinômio interpolador
coefficients = np.polyfit(x, y, degree)
polynomial = np.poly1d(coefficients)
print("Polinômio interpolador:", polynomial)

# Plotando os pontos e o polinômio interpolador
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
plt.plot(xi, yi, label='Polinômio interpolador')
plt.scatter(x, y, color='red', label='Pontos')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolação de Lagrange')
plt.legend()
plt.grid(True)
plt.show()

import math
import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return math.exp(x) + x**3

def derivative_exact(x):
    return math.exp(x) + 3*x**2

def derivative_numeric(x, h=0.001):
    return (func(x + h) - func(x)) / h

# Valores de x para o gráfico
x = np.linspace(-5, 5, 100)

# Valores correspondentes de y, derivada exata e derivada numérica
y = [func(i) for i in x]
exact_derivative = [derivative_exact(i) for i in x]
numeric_derivative = [derivative_numeric(i) for i in x]

# Plotando a função e as derivadas
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Função y = e^x + x^3')
plt.plot(x, exact_derivative, label='Derivada Exata')
plt.plot(x, numeric_derivative, label='Derivada Numérica')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Função e Derivadas')
plt.legend()
plt.grid(True)
plt.show()
print("Derivada exata:", exact_derivative)
print("Derivada numérica:", numeric_derivative)

import numpy as np
import matplotlib.pyplot as plt

# Dados de entrada (pontos)
x = [1, 1.5, 2, 2.5, 3, 3.5]
y = [3.25, 3.5, 3.75, 4, 4.25, 4.5]

# Realizando a regressão linear
coefficients = np.polyfit(x, y, 1)
slope = coefficients[0]  # Coeficiente angular
intercept = coefficients[1]  # Coeficiente linear

# Equação da reta de regressão
equacao_reta = f"y = {slope} * x + {intercept}"
print("Equação da reta de regressão:", equacao_reta)

# Pontos de x para o gráfico
x_grafico = np.linspace(min(x), max(x), 100)

# Valores correspondentes de y para a reta de regressão
y_regressao = slope * x_grafico + intercept

# Plotando os pontos e a reta de regressão
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', label='Pontos')
plt.plot(x_grafico, y_regressao, color='red', label='Reta de Regressão')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regressão Linear')
plt.legend()
plt.grid(True)
plt.show()

import math
import numpy as np

def func_a(x):
    return np.cos(2*x)

def func_b(x):
    return np.log(x)

def riemann_sum(func, a, b, n):
    dx = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = func(x)
    return dx * np.sum(y[:-1])

def trapezoidal_rule(func, a, b, n):
    dx = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = func(x)
    return dx * (np.sum(y) - 0.5 * (y[0] + y[-1]))

def simpsons_rule(func, a, b, n):
    if n % 2 != 0:
        n += 1  # Ajuste para garantir que seja um número par de subintervalos
    dx = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = func(x)
    return (dx / 3) * (np.sum(y[0:-1:2]) + 4*np.sum(y[1:-1:2]) + y[-1])

def absolute_error(true_value, approx_value):
    return np.abs(true_value - approx_value)

# Intervalo de integração para a integral (a)
a_a = 2
b_a = 5

# Intervalo de integração para a integral (b)
a_b = 1
b_b = 4

# Número de subintervalos para as tabelas
n_values = [4, 10, 25, 100]

# Tabela 1: Comparação dos resultados (integral a)
print("Tabela 1: Comparação dos resultados (integral a)")
print("n \t\t Riemann \t\t Trapézios \t\t Simpson")
print("-" * 56)
for n in n_values:
    result_riemann_a = riemann_sum(func_a, a_a, b_a, n)
    result_trapezoidal_a = trapezoidal_rule(func_a, a_a, b_a, n)
    result_simpson_a = simpsons_rule(func_a, a_a, b_a, n)
    print(f"{n} \t\t {result_riemann_a:.6f} \t\t {result_trapezoidal_a:.6f} \t\t {result_simpson_a:.6f}")
print()

# Tabela 2: Comparação dos erros absolutos (integral a)
print("Tabela 2: Comparação dos erros absolutos (integral a)")
print("n \t\t Erro Riemann \t\t Erro Trapézios \t\t Erro Simpson")
print("-" * 72)
true_value_a = math.sin(4) - math.sin(10)
for n in n_values:
    result_riemann_a = riemann_sum(func_a, a_a, b_a, n)
    result_trapezoidal_a = trapezoidal_rule(func_a, a_a, b_a, n)
    result_simpson_a = simpsons_rule(func_a, a_a, b_a, n)
    error_riemann_a = absolute_error(true_value_a, result_riemann_a)
    error_trapezoidal_a = absolute_error(true_value_a, result_trapezoidal_a)
    error_simpson_a = absolute_error(true_value_a, result_simpson_a)
    print(f"{n} \t\t {error_riemann_a:.6f} \t\t {error_trapezoidal_a:.6f} \t\t {error_simpson_a:.6f}")
print()

# Tabela 1: Comparação dos resultados (integral b)
print("Tabela 1: Comparação dos resultados (integral b)")
print("n \t\t Riemann \t\t Trapézios \t\t Simpson")
print("-" * 56)
for n in n_values:
    result_riemann_b = riemann_sum(func_b, a_b, b_b, n)
    result_trapezoidal_b = trapezoidal_rule(func_b, a_b, b_b, n)
    result_simpson_b = simpsons_rule(func_b, a_b, b_b, n)
    print(f"{n} \t\t {result_riemann_b:.6f} \t\t {result_trapezoidal_b:.6f} \t\t {result_simpson_b:.6f}")
print()

# Tabela 2: Comparação dos erros absolutos (integral b)
print("Tabela 2: Comparação dos erros absolutos (integral b)")
print("n \t\t Erro Riemann \t\t Erro Trapézios \t\t Erro Simpson")
print("-" * 72)
true_value_b = b_b * (math.log(b_b) - 1) - a_b * (math.log(a_b) - 1)
for n in n_values:
    result_riemann_b = riemann_sum(func_b, a_b, b_b, n)
    result_trapezoidal_b = trapezoidal_rule(func_b, a_b, b_b, n)
    result_simpson_b = simpsons_rule(func_b, a_b, b_b, n)
    error_riemann_b = absolute_error(true_value_b, result_riemann_b)
    error_trapezoidal_b = absolute_error(true_value_b, result_trapezoidal_b)
    error_simpson_b = absolute_error(true_value_b, result_simpson_b)
    print(f"{n} \t\t {error_riemann_b:.6f} \t\t {error_trapezoidal_b:.6f} \t\t {error_simpson_b:.6f}")
print()