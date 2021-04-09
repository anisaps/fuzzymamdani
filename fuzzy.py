import streamlit as st
import pandas as pd


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


def splitter(a, b):
    length = len(a)
    index = length//len(b)
    arr = [list(i) for i in zip(*[a[i:length]
                                  for i in range(0, length, index)])]
    return arr


option = st.sidebar.selectbox(
    'Silakan pilih:',
    ('Home', 'Teori Fuzzy Logic', 'Fuzzy Mamdani')
)

if option == 'Home' or option == '':
    st.title(""" UTS Pemrograman Simulasi""")
    st.write("""# SIMULASI FUZZY MAMDANI""")
    st.subheader(""" created by :""")
    st.subheader(""" 1. 152017084 Cindy Mawar Kasih""")
    st.subheader(""" 2. 152017114 Anisa Putri Setyaningrum""")

elif option == 'Fuzzy Mamdani':
    st.write("""## Fuzzy Mamdani""")  # menampilkan judul halaman dataframe
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
    buatrulenya = []
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
                    'Dan ' + str(buatvar[k][1])+' :', c, key='m'+str(k)+str(i))
            aturan.append(rule)

    # buat fuzzifikasi
    ex3 = st.beta_expander('Fuzzifikasi')
    ex3.write('Masukkan nilai yang akan diujikan kepada setiap variabel :')
    col = ex3.beta_columns(len(buatvar))
    buatfuzz = []
    for i in range(len(buatvar)-1):
        nilai = col[i].number_input(
            str(buatvar[i][1])+' :', 0, 100000, key=i+1)
        buatfuzz.append(nilai)
    ex3.write(buatfuzz)

    nilaifuzzy = []
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
                nilaifuzzy.append([ranges[k][0], nilaifuzzymin, nilaifuzzymax])
            else:
                continue
    ex3.write(nilaifuzzy)

    # buat implikasi
    ex4 = st.beta_expander('Implikasi')
    nilainya = splitter(aturan, buatvar)
    ex4.write(nilainya)


elif option == 'Teori Fuzzy Logic':
    st.title("""Teori Fuzzy Logic""")
    st.write("""## Manfaat Logika Fuzzy """)
    st.text("""Menurut Bart Kosko, Profesor di University of Southern California, Logika Fuzzy dapat menghasilkan 
sesuatu yang mengagumkan, seperti: 
•	Ahli pengambilan keputusan, secara teori dapat membuat pertimbangan 
        berdasarkan seluruh dokumen yang pernah ditulis
•	Kendaraan cerdas dengan perangkat sonar yang dapat mengatur pengereman mendadak. 
        Dengan fuzzy navigator, peta terkomputasi, serta perangkat transmitter dan receiver pada 
        aspal, suatu kendaraan dapat mengendalikan dirinya sendiri
•	Robot seperti manusia, yang dapat meniru perilaku manusia
""")

    st.write("""## Alasan Menggunakan Fuzzy """)
    st.text("""•	Konsep logika fuzzy mudah dimengerti 
•	Logika fuzzy sangat fleksibel 
•	Memiliki toleransi terhadap data-data yang tidak tepat 
•	Dapat membangun dan mengaplikasikan pengalaman-pengalaman para pakar secara langsung 
        tanpa harus melalui proses pelatihan 

""")

    st.write("""## Fuzzy Mamdani """)
    st.text("""•	Pada model ini, aturan fuzzy didefinisikan sebagai : 
        IF x1 is A1 AND…AND xn is An THEN y is B.
•	Dimana A1…..An dan B adalah nilai-nilai linguistik (atau fuzzy set) dan 
        “x1 is A1” menyatakan bahwa nilai variabel x1 adalah anggota fuzzy set A1
""")

    st.write("""## Fuzzy Mamdani Dikstrit """)
    st.text("""Untuk menghitung Fuzzy Logic Mamdani terdapat tiga tahap yaitu Fuzzifikasi, Inferensi, 
dan Defuzifikasi.
1.	Fuzzifikasi
    •	Fuzzifikasi merupakan formulasi proses pemetaan masukan yang diberikan ke bagian keluaran 
        menggunakan Logika Fuzzy.
    •	Prosesnya melibatkan hal-hal yang telah dijelaskan: Fungsi Keanggotaan, Operator Logika 
        Fuzzy, dan Aturan IF-THEN. 
    •	Fuzzification mengubah input-input yang nilai kebenarannya bersifat pasti 
        (crisp input) ke dalam bentuk fuzzy input, yang berupa nilai linguistik yang semantiknya 
        ditentukan berdasarkan fungsi keanggotaan tertentu.
    •	Fuzzification : mengubah kedua nilai crisp input tersebut menjadi fuzzy input menggunakan 
        fungsi-fungsi keanggotaan.

2.	Inferensi 
    •	Inference melakukan penalaran menggunakan fuzzy input dan fuzzy rules yang 
        telah ditentukan sehingga menghasilkan fuzzy output.
    •	Rule evaluation : melakukan reasoning menggunakan nilai-nilai fuzzy input tersebut dan 
        fuzzy rule sehingga dihasilkan fuzzy output.
    •	Langkah – Langkah Inference :
        Langkah 1 : Fuzifikasi Masukan
        Langkah 2 : Aplikasi Operasi Fuzzy 
        Langkah 3 : Aplikasi Metoda Implikasi
        Langkah 4 : Agregasi/Komposisi Seluruh Aturan
        Langkah 5 : Defuzzifikasi
3.	Defuzzification 
    •	Defuzzification mengubah fuzzy output menjadi crisp value berdasarkan fungsi keanggotaan 
        yang telah ditentukan
    •	Defuzzification : mengubah fuzzy output menjadi nilai Crisp (dalam satuan detik) 
        berdasarkan fungsi keanggotaan untuk output.
    •	Pada proses defuzzifikasi, set fuzzy hasil komposisi dikeluarkan menjadi suatu bilangan. 
        Metode defuzzifikasi, antara lain: Centroid, Bisector, Middle of Maximum, 
        Largest of Maximum, dan Smallest of Maximum.
        a.  Centroid method merupakan Center of Area atau Center of Gravity. Metoda ini untuk 
            menghitung nilai crisp menggunakan rumus :

            Dimana y adalah nilai crisp dan µR(y) adalah derajat keanggotaan dari y
        b.  Height method merupakan metoda yang memiliki prinsip keanggotaan maksimum karena
            metoda ini secara sederhana memilih nilai crisp yang memiliki derajat 
            keanggotaan maksimum.
        c.  Mean-Max Method merupakan generalisasi dari height method untuk kasus dimana 
            terdapat lebih dari satu nilai crisp yang memiliki derajat keanggotaan  maksimum. 
            Sehingga y* didefinisikan sebagai titik tengah antara nilai crisp terkecil (m) dan 
            nilai crisp terbesar (M) :
 
""")


st.markdown(
    '<style>body{background-color: #AADBE1;}</style>', unsafe_allow_html=True)
