import streamlit as st
import pandas as pd
import forfuzzy as ff


@st.cache(persist=True)
def abc():
    st.write('Fuzzy')


option = st.sidebar.selectbox(
    'Silakan pilih:',
    ('Home', 'Teori Fuzzy Logic', 'Fuzzy Mamdani 2 Input', 'Fuzzy Mamdani Continue')
)

if option == 'Home' or option == '':
    st.title(""" UTS Pemrograman Simulasi""")
    st.write("""# SIMULASI FUZZY MAMDANI""")
    st.subheader(""" created by :""")
    st.subheader(""" 1. 152017084 Cindy Mawar Kasih""")
    st.subheader(""" 2. 152017114 Anisa Putri Setyaningrum""")

elif option == 'Fuzzy Mamdani 2 Input':
    st.write("""## Fuzzy Mamdani 2 Input""")
    try:
        ex = st.beta_expander('Init Variable')
        buatvar = []
        n = ex.number_input('Masukkan berapa banyak variabel : ', 0, 200, 1)

        for i in range(n):
            ex.info('Variabel ke-' + str(i+1))
            c1, c2, c3, c4 = ex.beta_columns(4)
            tipe = c1.selectbox('Tipe variabel', ['INPUT', 'OUTPUT'], key=i)
            var = c2.text_input('Nama Variabel : ', key=i)
            satuan = c3.text_input('Satuan : ', key=i)
            m = c4.number_input('Jumlah himpunan : ', 0, 100, 0, key=i)
            buatvar.append([tipe, var, satuan, m, ff.himpunan2(m, ex, i)])
        df = pd.DataFrame(buatvar)
        ex.table(df)

        # if(buatvar[0][4][1][1] > buatvar[0][4][0][1]):
        # xaxis = [1, 0]
        # yaxis = [buatvar[0][4][1][1], buatvar[0][4][0][1]]
        # chart_data = pd.DataFrame([xaxis, yaxis], columns=[['a', 'b']])
        # ex.area_chart(chart_data)

        buatrule = []
        ex2 = st.beta_expander('Init Rules')
        # try:
        for i in range(4):
            co1, co2, co3 = ex2.beta_columns(3)
            r11 = co1.selectbox(
                'Jika ' + str(buatvar[0][1]), [buatvar[0][4][0][0], buatvar[0][4][1][0]], key=1+i)
            r12 = co2.selectbox(
                'Dan ' + str(buatvar[1][1]), [buatvar[1][4][0][0], buatvar[1][4][1][0]], key=2+i)
            r13 = co3.selectbox(
                'Maka ' + str(buatvar[2][1]), [buatvar[2][4][0][0], buatvar[2][4][1][0]], key=3+i)
            buatrule.append([r11, r12, r13])
        ex2.write(buatrule)

        ex3 = st.beta_expander('Fuzzifikasi')
        ex3.write('Masukkan nilai yang akan diujikan kepada setiap variabel :')
        col = ex3.beta_columns(len(buatvar))
        buatfuzz = []

        for i in range((len(buatvar))-1):
            fuzz = col[i].number_input(
                str(buatvar[i][1])+' :', 0, 100000, key=i+1)
            buatfuzz.append(fuzz)
        ex3.write(buatfuzz)

        hasilfuzz = []
        for i in range(len(buatfuzz)):
            if(buatvar[i][4][1][1] > buatvar[i][4][0][1]):
                namamin = buatvar[i][4][0][0]
                namamax = buatvar[i][4][1][0]
                nilaifuzzymin = (buatvar[i][4][1][1] - buatfuzz[i]) / \
                    (buatvar[i][4][1][1] - buatvar[i][4][0][1])
                nilaifuzzymax = (buatfuzz[i] - buatvar[i][4][0][1]) / \
                    (buatvar[i][4][1][1] - buatvar[i][4][0][1])
            else:
                namamin = buatvar[i][4][1][0]
                namamax = buatvar[i][4][0][0]
                nilaifuzzymin = (buatvar[i][4][0][1] - buatfuzz[i]) / \
                    (buatvar[i][4][0][1] - buatvar[i][4][1][1])
                nilaifuzzymax = (buatfuzz[i] - buatvar[i][4][1][1]) / \
                    (buatvar[i][4][0][1] - buatvar[i][4][1][1])
            hasilfuzz.append([namamin, nilaifuzzymin, namamax, nilaifuzzymax])
        ex3.write(hasilfuzz)

        ex4 = st.beta_expander('Implikasi')
        ex4.write(
            'Mencari nilai minimum dari kedua variabel berdasarkan rule yang sudah dibuat ')
        rules = pd.DataFrame(buatrule)
        ex4.table(rules)

        ex4.write(
            'Variabel ke-1')
        # var1
        implivar1 = []
        for i in range(len(buatrule)):
            if buatrule[i][0] == hasilfuzz[0][0]:
                im = hasilfuzz[0][1]
            else:
                im = hasilfuzz[0][3]
            implivar1.append([im, buatrule[i][2]])
        datavar1 = pd.DataFrame(implivar1)
        ex4.table(datavar1)

        ex4.write(
            'Variabel ke-2')
        # var2
        implivar2 = []
        for j in range(len(buatrule)):
            if buatrule[j][1] == hasilfuzz[1][0]:
                im = hasilfuzz[1][1]
            else:
                im = hasilfuzz[1][3]
            implivar2.append([im, buatrule[j][2]])
        # ex4.write(implivar2)
        datavar2 = pd.DataFrame(implivar2)
        ex4.table(datavar2)

        # hasil implikasi
        ex4.write(
            'Hasil Implikasi')
        hasilimpli = []
        for k in range(len(implivar1)):
            impli = min(implivar1[k][0], implivar2[k][0])
            hasilimpli.append([impli, implivar1[k][1]])

        # ex4.write(hasilimpli)
        hasilnya = pd.DataFrame(hasilimpli)
        ex4.table(hasilnya)

        ex5 = st.beta_expander('Defuzzifikasi')
        ex5.write(
            'Mencari nilai terbesar dari keputusan rule berdasarkan nilai implikasi yang sudah di dapat')

        max1 = []
        max2 = []
        for i in range(len(hasilimpli)):
            if(buatvar[2][4][0][0] == hasilimpli[i][1]):
                buatmax = hasilimpli[i][0]
            else:
                buatmax = 0
            max1.append(buatmax)
        for i in range(len(hasilimpli)):
            if(buatvar[2][4][1][0] == hasilimpli[i][1]):
                buatmax = hasilimpli[i][0]
            else:
                buatmax = 0
            max2.append(buatmax)

        ex5.write('1. '+str(buatvar[2][4][0][0])+' : '+str(max(max1)))
        ex5.write('2. '+str(buatvar[2][4][1][0]) + ' : '+str(max(max2)))

        col1, col2 = ex5.beta_columns(2)
        b1 = col1.number_input(
            'Masukkan berapa banyak random number (Var 1) : ', 5, 200, 5)
        b2 = col2.number_input(
            'Masukkan berapa banyak random number (Var 2) : ', 5, 200, 5)

        if(buatvar[2][4][1][1] > buatvar[2][4][0][1]):
            rand = ff.randnum(b1, buatvar[2][4][0][1], buatvar[2][4][1][1])
            rand2 = ff.randnum(b2, buatvar[2][4][0][1], buatvar[2][4][1][1])
        else:
            rand = ff.randnum(b1, buatvar[2][4][1][1], buatvar[2][4][0][1])
            rand2 = ff.randnum(b2, buatvar[2][4][1][1], buatvar[2][4][0][1])

        ex5.write(randvar1)
        ex5.write(randvar2)

        data = {str(buatvar[2][4][0][0]): rand,
                str(buatvar[2][4][1][0]): rand2, }

        datadf = pd.DataFrame(
            data, columns=[str(buatvar[2][4][0][0]), str(buatvar[2][4][1][0])])
        ex5.write(datadf)
        maxi1 = max(max1)
        maxi2 = max(max2)

        defuzz = ((randvar1*maxi1))+(randvar2*(maxi2)) / \
            ((maxi1*len(rand))+(maxi2*len(rand2)))
        ex5.write(
            'Nilai Defuzzifikasi : '+str(defuzz))
        ex5.write('Jadi '+str(buatvar[2][1]) +
                  ' yang diperlukan adalah sebesar '+str(defuzz)+' '+buatvar[2][2])

    except:
        ex2.write('')


elif option == 'Fuzzy Mamdani Continue':
    st.write("""## Fuzzy Mamdani Continue (Masih tahap pembangunan)""")  # menampilkan judul halaman dataframe
    ex = st.beta_expander('Init Variable')
    ex.write(
        'Masukkan variabel-variabel yang akan digunakan sebagai input/output pada sistem')
    n = ex.number_input('Masukkan berapa banyak variabel : ', 0, 200, 1)

    # buat variabel
    buatvar = []
    for i in range(n):
        ex.info('Variabel ke-' + str(i+1))
        c1, c2, c3, c4 = ex.beta_columns(4)
        tipe = c1.selectbox('Tipe variabel', ['INPUT', 'OUTPUT'], key=i)
        var = c2.text_input('Nama Variabel : ', key=i)
        satuan = c3.text_input('Satuan : ', key=i)
        m = c4.number_input('Jumlah himpunan : ', 0, 100, 0, key=i)
        buatvar.append([tipe, var, satuan, m, ff.himpunan(m, ex, i)])

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
            c = ff.rules(buatvar[k])
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
    ex2.write(aturan)

    # buat fuzzifikasi
    ex3 = st.beta_expander('Fuzzifikasi')
    ex3.write('Masukkan nilai yang akan diujikan kepada setiap variabel :')
    col = ex3.beta_columns(len(buatvar))
    buatfuzz = []
    for i in range((len(buatvar))-1):
        nilai = col[i].number_input(
            str(buatvar[i][1])+' :', 0, 100000, key=i+1)
        buatfuzz.append(nilai)
    ex3.write(buatfuzz)

    nilaifuzzy = []
    for j in range(len(buatvar)-1):
        ranges = ff.rangenya(buatvar[j])
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
    ex4.write(nilaifuzzy)
    buatimpli = []

    for i in range(len(nilaifuzzy)):
        for p in range(len(aturan)):
            if(aturan[p] == nilaifuzzy[i][0]):
                x = nilaifuzzy[i][2]
            else:
                x = nilaifuzzy[i][1]
            buatimpli.append(x)
    ex4.write(buatimpli)

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
