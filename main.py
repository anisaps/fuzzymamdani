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


def rules2(m, var1, var2):
    result = []
    for i in range(0, len(var1)):
        for j in range(0, len(var2)):
            result.append([var1[i], var2[j]])
    return result


def rules3(m, var1, var2, var3):
    result = []
    for i in range(0, len(var1)):
        for j in range(0, len(var2)):
            for k in range(0, len(var3)):
                result.append([var1[i], var2[j], var3[k]])
    return result


def rules4(m, var1, var2, var3, var4):
    result = []
    for i in range(0, len(var1)):
        for j in range(0, len(var2)):
            for k in range(0, len(var3)):
                for l in range(0, len(var4)):
                    result.append([var1[i], var2[j], var3[k], var4[l]])
    return result


ex = st.beta_expander('Init Variable')
ex.write(
    'Masukkan variabel-variabel yang akan digunakan sebagai input/output pada sistem')
n = ex.number_input('Masukkan berapa banyak variabel : ', 0, 200, 1)
r = []
result = []

buatvar = []
for i in range(n):
    ex.info('Variabel ke-' + str(i+1))
    c1, c2, c3, c4 = ex.beta_columns(4)
    tipe = c1.selectbox('Tipe variabel', ['INPUT', 'OUTPUT'], key=i)
    var = c2.text_input('Nama Variabel : ', key=i)
    satuan = c3.text_input('Satuan : ', key=i)
    m = c4.number_input('Jumlah himpunan : ', 0, 100, 0, key=i)
    buatvar.append([tipe, var, satuan, m, himpunan(m)])

# st.write(r)
ex2 = st.beta_expander('Init Rules')
df = pd.DataFrame(buatvar)
ex2.table(df)
