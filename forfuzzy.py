# All Function
import random
import pandas as pd
import os
import base64


def himpunan(m, ex, i):
    buathim = []
    for j in range(m):
        cl1, cl2, cl3 = ex.beta_columns(3)
        him = cl1.text_input('Nama Himpunan ke-' + str(j+1), key=i+j)
        mini = cl2.number_input('Minimum', 0, 10000,
                                key='var'+str(i)+'min' + str(m+j))
        maxi = cl3.number_input('Maximum', 0, 10000,
                                key='var'+str(i)+'min' + str(m+j))
        buathim.append([him, mini, maxi])
    return buathim


def himpunan2(m, ex, i):
    buathim = []
    for j in range(m):
        cl1, cl2 = ex.beta_columns(2)
        him = cl1.text_input('Nama Himpunan ke-' + str(j+1), key=i+j)
        nilai = cl2.number_input('Nilai ', 0, 10000,
                                 key='var'+str(i)+'min' + str(m+j))
        buathim.append([him, nilai])
    return buathim


def rules(var):
    isi = []
    sl = []
    a = var[4]
    isi.append(a)
    for m in range(len(isi)):
        for l in range(len(isi[m])):
            b = isi[m][l][0]
            sl.append(b)
    return sl


def implik(var):
    isi = []
    sl = []
    a = var[1]
    isi.append(a)
    for m in range(len(isi)):
        for l in range(len(isi[m])):
            b = isi[m][l][0]
            sl.append(b)
    return sl


def rangenya(var):
    isi = []
    sl = []
    a = var[4]
    isi.append(a)
    for m in range(len(isi)):
        for l in range(len(isi[m])):
            aw = isi[m][l][0]
            b = isi[m][l][1]
            c = isi[m][l][2]
            sl.append([aw, b, c])
    return sl


def nilaimin(var):
    isi = []
    sl = []
    a = var[4]
    isi.append(a)
    for m in range(len(isi)):
        for l in range(len(isi[m])):
            b = isi[m][l][1]
            sl.append(b)
    return sl


def nilaimax(var):
    isi = []
    sl = []
    a = var[4]
    isi.append(a)
    for m in range(len(isi)):
        for l in range(len(isi[m])):
            b = isi[m][l][2]
            sl.append(b)
    return sl


def splitter(a, b):
    length = len(a)
    index = length//len(b)
    arr = []
    for i in range(length):
        arr.append(a[i:index])
        i += index
    return arr


def randnum(n, mini, maxi):
    i = 1
    r = 0
    new_list = []
    while i <= n:
        na = random.randrange(mini, maxi)
        r = round(na, 3)
        i += 1
        new_list.append(r)
    return new_list


def randnum2(n, mini, maxi):
    i = 1
    r = 0
    new_list = []
    while i <= n:
        na = random.randrange(mini, maxi)
        r = round(na, 3)
        i += 1
        new_list.append(r)
    return new_list


def jumlah(arr):
    hasil = 0
    for i in range(0, len(arr)):
        hasil = hasil + arr[i]
    return hasil


def exploredata(data):
    df = pd.read_csv(os.path.join(data))
    return df


def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    # some strings <-> bytes conversions necessary here
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}">Download csv file</a>'
