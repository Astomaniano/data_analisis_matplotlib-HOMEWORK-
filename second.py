import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
x = np.random.rand(100)  # массив из 100 случайных чисел для оси X
y = np.random.rand(100)  # массив из 100 случайных чисел для оси Y

# Создание диаграммы рассеяния
plt.figure(figsize=(10, 6))
plt.scatter(x, y, alpha=0.75, edgecolors='w', s=50)

# Настройка сетки и заголовков
plt.grid(axis='both', alpha=0.5)
plt.title('Диаграмма рассеяния случайных данных')
plt.xlabel('X')
plt.ylabel('Y')

# Отображение графика
plt.show()