import datetime
import os
from datetime import timedelta
import requests
import pandas as pd
from urllib.parse import urlencode
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from matplotlib import rc

def dat_str(date_in): # Изменение формата дат
    date_p = str(date_in)
    return (date_p[6:10] + date_p[3:5] + date_p[0:2])

def cbrf(val,date_start,date_end):  # Обращение за курсом на сайт ЦБ РФ
    global date_start_p, date_end_p
    val_date = []
    val_fl = []
    date_start_p = dat_str(date_start)
    date_end_p = dat_str(date_end)

    file_name = 'cbrf_'+val+'_'+date_start_p+'_'+date_end_p+'.csv'
    file_path = './'+file_name
    # Проверяем: сохранили ли мы файл с данными ЦБ РФ в файле после обращения к сайту
    if os.path.exists(file_path):
        print(f'Файл с архивом курса {val} уже существует.')
        return
    # R01235 - USD 840, R01375 - CNY 156
    if val == 'USD':
        val_rq = 'R01235'
    elif val == 'CNY':
        val_rq = 'R01375'
    data = requests.get('https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1='+date_start+'&date_req2='+date_end+'&VAL_NM_RQ='+val_rq)
    data_cont = data.text.split('<Record Date="')

    val_arh = {}
    for r in data_cont:
        try:
            date_val = r[0:r.find('" Id="')]
            date_val_ = datetime.datetime.strptime(date_val, '%d.%m.%Y')

            val_date.append(date_val_)
            valu_val = r[r.find('<VunitRate>') + len('<VunitRate>'):r.find('</VunitRate>')]
            val_1 = valu_val.find(',')
            val_2_1 = (valu_val[0:val_1])
            val_2_1_int = int(val_2_1)
            val_fl.append(float(val_2_1 + '.' + valu_val[val_1+1:len(valu_val)]))
            val_arh = {'Date':val_date, val: val_fl}
            # print(f'val_arh - {val_arh}')
        except:
            pass
        finally:
            pass
    df = pd.DataFrame.from_dict(val_arh)
    # print(f'df cbrf  {file_name} - {df}')
    df.to_csv(file_name, index=False)

def cbrf_USD_CNY_df(val1,val2,date_start,date_end): # Чтение курсов
    # юаня и доллара из ранее сохранённых файлов
    global df_1, df_2
    date_start_p = dat_str(date_start)
    date_end_p = dat_str(date_end)
    file_name1 = 'cbrf_' + val1 + '_' + date_start_p + '_' + date_end_p + '.csv'
    # print(f'file_name1 - {file_name1}')
    df_1 = pd.read_csv(file_name1)
    file_name2 = 'cbrf_' + val2 + '_' + date_start_p + '_' + date_end_p + '.csv'
    df_2 = pd.read_csv(file_name2)

def change_date(df_old): # Смена формата месяца с буквенного на числовой
    dict_mon = {
        ' Jan ': '/01/',
        ' Feb ': '/02/',
        ' Mar ': '/03/',
        ' Apr ': '/04/',
        ' May ': '/05/',
        ' Jun ': '/06/',
        ' Jul ': '/07/',
        ' Aug ': '/08/',
        ' Sep ': '/09/',
        ' Oct ': '/10/',
        ' Nov ': '/11/',
        ' Dec ': '/12/'
    }
    for key, value in dict_mon.items():
        df_old['Date'] = df_old['Date'].apply(
            lambda x: x.replace(key, value) if key in x else x)

    df_old['Date'] = df_old['Date'].apply(
        lambda x: x.replace('/20', '/') if '/20' in x else x)
    df_old['Date'] = df_old['Date'].apply(lambda x: datetime.datetime.strptime(x, '%d/%m/%y').date())
    df_old['Date'] = pd.to_datetime(df_old['Date'])
    df_sort = df_old.sort_values(by=['Date'], ascending=True)
    return df_sort

def course_norm(df_new):

    df_norm = pd.DataFrame()
    # Устанавливаем начальную и конечную даты в нужном формате
    date_start = datetime.datetime.strptime('01.01.2014', '%d.%m.%Y')
    date_end = datetime.datetime.strptime('01.11.2024', '%d.%m.%Y')

    date_now = date_start

    # Делаем дату индексной
    df_new = df_new.set_index('Date')

    course_prev = 0
    while date_now <= date_end:
        if date_now in df_new.index:
            course_prev = df_new['USD/CNY'].loc[date_now]
            # print(f'Элемент найден! {date_now}')
        else:
            new_rows = pd.DataFrame({"Date": [date_now], 'USD/CNY': [course_prev]})
            new_rows = new_rows.set_index('Date')
            df_new = pd.concat([df_new, new_rows], ignore_index=False)
            # print(f'Элемент НЕ найден! {new_rows}')
        date_now = date_now + datetime.timedelta(days=1)

    df_new = df_new.sort_values(by=['Date'], ascending=True)

    # print(f'df_new {df_new}')
    df_end = df_new
    # print(f'df_end {df_end}')
    return df_end

# Программа обращается к сайтам с курсами юаня и доллара в России и Китае,
# сохраняет курсы в файлы, нормализует курсы в разрядности и форматах,
# рассчитывает кросс-курс юаня к доллару в России,
# показывает графики курсов в России и Китае и арбитражный курс

df_norm  = pd.DataFrame()

start_date = '01/01/2014'
end_date = '01/11/2024'
# Обращение к сайту ЦБ РФ за архивом курса доллара
cbrf('USD',start_date,end_date)
# Обращение к сайту ЦБ РФ за архивом курса юаня
cbrf('CNY',start_date,end_date)
# Чтение курсов ЦБ из файла и их загрузка в фрейм
cbrf_USD_CNY_df('USD','CNY',start_date,end_date)
# формирование фрейма с данными о курсе доллара и юаня
df_cbrf = df_1.merge(df_2[['CNY', 'Date']], on = 'Date', how = 'left')
# Формирование кросс-курса доллара к юаню
df_cbrf['USD/CNY'] = df_cbrf['USD'] / df_cbrf['CNY']
# Сохранение кросс-курса в файл
file_name = 'cbrf_'+'USDCNY'+'_'+date_start_p+'_'+date_end_p+'.csv'
df_cbrf.to_csv(file_name, index=False)

# Обращение за китайским курсом
base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'
public_key = 'https://disk.yandex.ru/d/KXLQSFIX3u06dw'  # Сюда вписываете вашу ссылку

# Если данные уже получениы и сохранены в файл, то в интернет не идём
file_name = 'china_valute.csv'
if os.path.exists(file_name):
    print(f'Файл с архивом китайского курса USD/CNY уже существует.')
else:
    final_url = base_url + urlencode(dict(public_key=public_key))
    response = requests.get(final_url)
    download_url = response.json()['href']

    download_response = requests.get(download_url)
    download_content = download_response.content
    with open(file_name, 'wb') as f:   # Здесь укажите нужный путь к файлу
        f.write(download_response.content)

# Читаем  фрейм данные из файла о китайском курсе доллара
df_c = pd.read_csv(file_name, sep=';', engine='python')

# Очищаем фрейм от ненужных заголовков
df_c = df_c.drop([2635, 2636])
# Меняем формат месяца с символьного на цифровой
df_c_1 = change_date(df_c)

df_norm = course_norm(df_c_1)
df_norm_c = df_norm


# Сохраняем нормализованны файл по китайскому курсу
file_name = 'cbcn_'+'USDCNY'+'_'+date_start_p+'_'+date_end_p+'_n.csv'
df_norm_c.to_csv(file_name, index=False)

# Формируем фрейм с календарными датами и нулевым значением российского курса,
# если такой даты во фрейме с курсами нет
date_start = datetime.datetime.strptime('01.01.2014', '%d.%m.%Y').date()
df_cbrf.rename({'date': 'Date'}, axis=1, inplace=True)

df_r_1 = df_cbrf
df_r_1 = df_r_1.drop(['USD', 'CNY'], axis=1)

df_r_1['Date'] = pd.to_datetime(df_r_1['Date'])

df_norm_r = course_norm(df_r_1)

df_norm_c.rename({'USD/CNY': 'cin'}, axis=1, inplace=True)
df_norm_r.rename({'USD/CNY': 'rus'}, axis=1, inplace=True)

vertical_concat = pd.concat([df_norm_c, df_norm_r], axis=1)
vertical_concat.cin = vertical_concat.cin.astype(float)
vertical_concat['div'] = vertical_concat['cin'] / vertical_concat['rus']

vertical_concat = vertical_concat.reset_index()


#Рисуем графики курса и кросс-курса юаня к доллару
fig, axes = plt.subplots(figsize=(16, 8))

axes.plot(vertical_concat['Date'], vertical_concat['rus'], 'b-', label='Кросс-курс юаня к доллару в России')
axes.plot(vertical_concat['Date'], vertical_concat['cin'], 'r-', label='Курс юаня к доллару в Китае')

axes.grid(which='major', linewidth=1.2)
axes.grid(which='minor', linestyle='--', color='gray', linewidth=0.5)

axes.legend([r'Кросс-курс юаня к доллару в России', r'Курс юаня к доллару в Китае'], fontsize=12, loc=0) # добавить легенду
plt.ylim(6, 8)

plt.title('Курс юаня к доллару в Китае и кросс-курс юаня к доллару в России', fontsize=16,) # заголовок
plt.xlabel('Дата', fontsize=14) # ось абсцисс
plt.ylabel('CNY/USD', fontsize=14) # ось ординат

#Рисуем график арбитражного курса юаня к доллару в России и Китае
fig1, axes1 = plt.subplots(figsize=(14, 6))

axes1.plot(vertical_concat['Date'], vertical_concat['div'], 'g-', label='Разница между кросс-курсом юаня к доллару в России и курсом доллара в Китае')

axes1.grid(which='major', linewidth=1.2)
axes1.grid(which='minor', linestyle='--', color='gray', linewidth=0.5)

axes1.legend(['Арбитражный курс юаня к доллару'], fontsize=12, loc=0) # добавить легенду
plt.ylim(0.9, 1.1)

plt.title('Арбитражный курс юаня к доллару в России и Китае', fontsize=16,) # заголовок
plt.xlabel('Дата', fontsize=14) # ось абсцисс
plt.ylabel('CNY/USD', fontsize=14) # ось ординат

plt.show()

