import datetime
import os
from datetime import datetime, timedelta

import requests
import pandas as pd
from urllib.parse import urlencode


def dat_str(date_in):
    date_p = str(date_in)
    return (date_p[6:10] + date_p[3:5] + date_p[0:2])

def cbrf(val,date_start,date_end):
    global date_start_p, date_end_p
    val_date = []
    val_fl = []
    date_start_p = dat_str(date_start)
    date_end_p = dat_str(date_end)
    file_name = 'cbrf_'+val+'_'+date_start_p+'_'+date_end_p+'.csv'
    file_path = './'+file_name
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
            date_val_ = datetime.datetime.strptime(date_val, '%d.%m.%Y').date()
            val_date.append(date_val_)
            valu_val = r[r.find('<VunitRate>') + len('<VunitRate>'):r.find('</VunitRate>')]
            val_1 = valu_val.find(',')
            val_2_1 = (valu_val[0:val_1])
            val_2_1_int = int(val_2_1)
            val_fl.append(float(val_2_1 + '.' + valu_val[val_1+1:len(valu_val)]))
            val_arh = {'date':val_date, val: val_fl}
        except:
            pass
        finally:
            pass
    df = pd.DataFrame.from_dict(val_arh)
    df.to_csv(file_name, index=False)

def cbrf_USD_CNY_df(val1,val2,date_start,date_end):
    global df_1, df_2
    date_start_p = dat_str(date_start)
    date_end_p = dat_str(date_end)
    file_name1 = 'cbrf_' + val1 + '_' + date_start_p + '_' + date_end_p + '.csv'
    df_1 = pd.read_csv(file_name1)
    file_name2 = 'cbrf_' + val2 + '_' + date_start_p + '_' + date_end_p + '.csv'
    df_2 = pd.read_csv(file_name2)

def change_date(df_old):
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
    df_old['Date'] = df_old['Date'].apply(
        lambda x: datetime.strptime(x, '%d/%m/%y').date())
    df_old['Date'] = pd.to_datetime(df_old['Date'])
    df_sort = df_old.sort_values(by=['Date'], ascending=True)
    return df_sort

cbrf('USD','01/01/2014','20/11/2024')
cbrf('CNY','01/01/2014','20/11/2024')
cbrf_USD_CNY_df('USD','CNY','20/09/2024','20/11/2024')

df_cbrf = df_1.merge(df_2[['CNY', 'date']], on = 'date', how = 'left')
df_cbrf['USD/CNY'] = df_cbrf['USD'] / df_cbrf['CNY']
file_name = 'cbrf_'+'USDCNY'+'_'+date_start_p+'_'+date_end_p+'.csv'
df_cbrf.to_csv(file_name, index=False)


base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'
public_key = 'https://disk.yandex.ru/d/KXLQSFIX3u06dw'  # Сюда вписываете вашу ссылку

# Получаем загрузочную ссылку
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

df_c = pd.read_csv(file_name, sep=';', engine='python')

df_c = df_c.drop([2635, 2636])
df_c_1 = change_date(df_c)

date_start = datetime.strptime('01.01.2014', '%d.%m.%Y').date()
date_end = datetime.strptime('01.11.2024', '%d.%m.%Y').date()

dict_rus = {}
dict_rus = {
  "Date": date_start,
  "Val_Russia": 0.0000
}
from datetime import timedelta
data = {'Date': [date_start],
        'Valute': [0]}

df_c_1 = df_c_1.set_index('Date')
print(df_c_1)
df_list = df_c_1.index.tolist()
df_list_ = []
for li in df_list:
    li_ = str(li)[0:10]
    df_list_.append(li_)
# print(f'df_list {df_list_}')
df_c_2 = df_c_1
print(f'df_c_2')
print(df_c_2)
val_prev = 0
while (date_start <= date_end):
    date_ = str(date_start)
    if date_ in df_list_:
        pass
    else:
        new_row = {'Date': [pd.Timestamp(date_start)], 'USD/CNY': [val_prev]}
        df_new = pd.DataFrame(new_row)
        df_new = df_new.set_index('Date')
        df_c_1 = pd.concat([df_c_1, df_new], axis=0)

    date_start = date_start + timedelta(days=1)
print(df_c_1)
df_sort_1 = df_c_1.sort_values(by=['Date'], ascending=True)
print(df_sort_1)
df_old['Date'] = df_old['Date'].apply(
    lambda x: x.replace(key, value) if key in x else x)

