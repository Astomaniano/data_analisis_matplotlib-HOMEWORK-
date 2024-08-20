from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import pandas as pd
import matplotlib.pyplot as plt

driver = webdriver.Chrome()

# Открытие страницы
driver.get('https://www.divan.ru/category/divany-i-kresla')

time.sleep(5)

# Парсинг цен
prices = driver.find_elements(By.XPATH, "//span[@class='ui-LD-ZU KIkOH' and contains(@data-testid, 'price')]")

# Открытие CSV файла для записи
with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
   writer = csv.writer(file)
   writer.writerow(['Price'])  # Записываем заголовок столбца

   # Записываем цены в CSV файл
   for price in prices:
       writer.writerow([price.text])

driver.quit()

# Чистка данных
df = pd.read_csv('prices.csv')

df['Price'] = df['Price'].str.replace('руб.', '').str.replace(' ', '').astype(int)

df.to_csv('cleaned_prices.csv', index=False)

# Поиск средней цены
data = pd.read_csv('cleaned_prices.csv')
average_price = data['Price'].mean()

print(f'Средняя цена дивана: {average_price}.руб')

# График
df = pd.read_csv('cleaned_prices.csv')

prices = df['Price']

plt.figure(figsize=(10, 6))
plt.hist(prices, bins=20, color='skyblue', edgecolor='black')

plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена, ₽')
plt.ylabel('Количество')

plt.grid(axis='y', alpha=0.75)
plt.show()
