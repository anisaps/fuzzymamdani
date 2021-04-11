# All Function

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
