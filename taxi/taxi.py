import pandas as pd

taxi = pd.read_csv('./2_taxi_nyc.csv')  # чтение файла
taxi_data = taxi.shape                  # вывод количества строк и столбцов
columns = taxi.dtypes.value_counts()    #  taxi.dtypes - выводит информацию о типе данных для каждого столбца
                                        # далее считает, сколько раз встречается каждый тип
taxi = taxi.rename(columns={'pcp 01': 'pcp_01',
                            'pcp 06': 'pcp_06',
                            'pcp 24': 'pcp_24'})   # переименование столбцов (удаление пробелов)
brooklyn_count = taxi.borough.value_counts()     # выводит, сколько раз встречается 'Brooklyn'
pickups = taxi.pickups.sum()
group_borough = taxi \
                .groupby('borough', as_index=False)\
                .agg({'pickups': 'sum'})\
                .sort_values('pickups', ascending=False)
min_pickups = taxi \
                .groupby('borough')\
                .agg({'pickups': 'sum'})\
                .idxmin()

hollyday = taxi\
       .query("hday == 'Y'") \
       .groupby('borough', as_index=False) \
       .agg({'pickups': 'mean'})
weekday = taxi\
       .query("hday == 'N'") \
       .groupby('borough', as_index=False) \
       .agg({'pickups': 'mean'})
mean = hollyday.merge(weekday, on='borough')\
       .query("pickups_x > pickups_y") \
       .borough

pickups_by_mon_bor = taxi.groupby(['borough', 'pickup_month'], as_index=False) \
                     .agg({'pickups': 'sum'}).sort_values('pickups', ascending=False)

print(pickups_by_mon_bor)
# print(group_borough)
