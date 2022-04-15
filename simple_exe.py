import pandas as pd
from datetime import datetime

df = pd.read_csv('./lesson_1_data.csv', encoding='windows-1251', sep=';')
df = df.rename(columns={'Номер': 'number',
                'Дата создания': 'create_date',
               'Дата оплаты': 'payment_date',
               'Title': 'title',
               'Статус': 'status',
               'Заработано': 'money',
               'Город': 'city',
               'Платежная система': 'payment_system'})

all_money = round(df.money.sum(), 2)
unique = df.title.unique()

count_of_orders = df\
    .query('status == "Завершен"') \
    .groupby('title', as_index=False)\
    .aggregate({'money': 'sum', 'number': 'count'})\
    .sort_values('money',  ascending=False) \
    .rename(columns={'number': 'success_orders'})

check_title = count_of_orders.title.count()
check_sum = count_of_orders.money.sum()

today = datetime.today().strftime('%Y-%m-%d')
file_name = f"count_of_orders_{today}.csv"

if check_sum == all_money and check_title == len(unique):
    count_of_orders.to_csv(file_name, index=False)
    print(f'Success! File {file_name} is written')
else:
    'ERROR'
