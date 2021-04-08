import streamlit as st
import pandas as pd

st.title('FUZZY MAMDANI')
st.subheader('created by : 152017114 Anisa Putri Setyaningrum')


@st.cache(persist=True)
def abc(a):
    st.write('apa aja')


def himpunan(m):
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


ex = st.beta_expander('Init Variable')
ex.write(
    'Masukkan variabel-variabel yang akan digunakan sebagai input/output pada sistem')
n = ex.number_input('Masukkan berapa banyak variabel : ', 0, 200, 1)

buatvar = []
for i in range(n):
    ex.info('Variabel ke-' + str(i+1))
    c1, c2, c3, c4 = ex.beta_columns(4)
    tipe = c1.selectbox('Tipe variabel', ['INPUT', 'OUTPUT'], key=i)
    var = c2.text_input('Nama Variabel : ', key=i)
    satuan = c3.text_input('Satuan : ', key=i)
    m = c4.number_input('Jumlah himpunan : ', 0, 100, 0, key=i)
    buatvar.append([tipe, var, satuan, m, himpunan(m)])

# buat rules
ex2 = st.beta_expander('Init Rules')
df = pd.DataFrame(buatvar)
ex2.table(df)
jmlrule = ex2.number_input('Masukkan jumlah rule : ', 0, 200, 1)
aturan = []
for i in range(jmlrule):
    cos = ex2.beta_columns(len(buatvar)+1)
    for k in range(len(buatvar)):
        c = rules(buatvar[k])
        if k == (len(buatvar) - 1):
            rule = cos[k].selectbox(
                'Maka ' + str(buatvar[k][1])+' :', c, key=k+i)
        elif(k == 0):
            rule = cos[k].selectbox('R' + str(i+1) + ' => Jika ' +
                                    str(buatvar[k][1])+' :', c, key=k+i)
        else:
            rule = cos[k].selectbox(
                'Dan ' + str(buatvar[k][1])+' :', c, key=k+i)
        aturan.append(rule)


# buat fuzzifikasi
ex3 = st.beta_expander('Fuzzifikasi')
ex3.write('Masukkan nilai yang akan diujikan kepada setiap variabel :')
col = ex3.beta_columns(len(buatvar))
buatfuzz = []
for i in range(len(buatvar)-1):
    nilai = col[i].number_input(str(buatvar[i][1])+' :', 0, 100000, key=i+1)
    buatfuzz.append(nilai)
ex3.write(buatfuzz)

for j in range(len(buatvar)):
    ranges = rangenya(buatvar[j])
    for k in range(len(ranges)):
        # ex3.write(ranges)
        if buatfuzz[j] in range(ranges[k][1], ranges[k][2]):
            ex3.write('Terpilih : '+str(ranges[k][0]))
            nilaifuzzymin = (ranges[k][2] - buatfuzz[j]) / \
                (ranges[k][2] - ranges[k][1])
            nilaifuzzymax = (buatfuzz[j] - ranges[k][1]) / \
                (ranges[k][2] - ranges[k][1])
            ex3.write('uMinimum : '+str(nilaifuzzymin))
            ex3.write('uMaximum : '+str(nilaifuzzymax))

        else:
            continue
