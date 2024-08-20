import pandas as pd
import matplotlib.pyplot as plt

# Загрузите данные из CSV файла
df = pd.read_csv('cleaned_prices.csv')

# Предположим, что столбец с ценами называется 'price'
prices = df['Price']

# Построение гистограммы
plt.figure(figsize=(10, 6))
plt.hist(prices, bins=20, color='skyblue', edgecolor='black')

# Добавление заголовков и меток
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена, ₽')
plt.ylabel('Количество')

# Показать график
plt.grid(axis='y', alpha=0.75)
plt.show()