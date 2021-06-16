from datetime import time

from matplotlib import colors


print('Basic text all basic python')
print('Basic text stirng 1 pyhton')
def my_funcion() :
    print('basic text stirng 1 python')
    print('basic text string 2 python')
    print('basic text stirng 3 python')
    print('basic text stirng 4 python')
my_funcion()
print(" ")

print('Basic text syntax 1 pyhton')
def my_funcion() :
    if 5 > 2:
        print('basic text syntax 1 pyhton')
    if 5 > 2:
        print('basic text syntax 2 python')
    if 5 > 2:
        print('basic text syntax 3 pyhton')
    if 5 > 2:
        print('basic text syntax 4 pyhton')
my_funcion()
print(" ")

print('Basic text syntax 2 python')
def my_funcion() :
    if 5 > 2:
        print('basic text syntax 1 loop')
        print('basic text syntax 2 loop')
        print('basic text syntax 3 loop')
        print('basic text syntax 4 loop')
my_funcion()
print(" ")

print('Basic text variable 1 pyhton')
def my_funcion() :
    a="this is text variable value is :"
    b=100
    print(a)
    print(b)
my_funcion()
print(" ")

print('Basic text variable 2 pyhton')
def my_funcion() :
    a,b,c,d="text 1","text 2","text 3","text 4"
    print(a)
    print(b)
    print(c)
    print(d)
my_funcion()
print(" ")

print('Basic text variable 3 pyhton')
def my_funcion() :
    a=b=c=d="text python loop vairbale"
    print(a)
    print(b)
    print(c)
    print(d)
my_funcion()
print(" ")

print('Basic text list')
def my_funcion() :
    buah=["nanas","pisang","jeruk","jambu"]
    a,b,c,d=buah
    print(a)
    print(b)
    print(c)
    print(d)
my_funcion()
print(" ")

print('Basic text pyhton output 1')
def my_fucnion() :
    a="manis"
    print("buah itu rasanya sangat " +a)
    b="pedas"
    print("cabai itu rasanya sangat " +b)
my_funcion()
print(" ")

print('Basic text pyhton output 2')
def my_funcion() :
    a="buah itu rasanya sangat "
    b="manis"
    c=a+b
    print(c)
my_funcion()
print(" ")

print('Basic text pyhton list')
def my_fucnion() :
    a="""this is multi string for make script or more"""
    print(a)
my_funcion()
print(" ")

print('Basic text pyhton name list')
def my_funcion() :
    name1=["text 1 pyhton"]
    name2=["text 2 python"]
    name3=["text 3 pyhton"]
    print(name1)
    print(name2)
    print(name3)
my_funcion()
print(" ")

print('Basic text pyhton 1')
def my_funcion() :
    a="banana"
    print(len(a))
my_funcion()
print(" ")

print('Basic text pyhton 2')
def my_funcion() :
    for x in "123456789":
        print(x)
    print('10')
my_funcion()
print(" ")

print('Basic text pyhton 3')
def my_funcion() :
    txt="buah itu rasanya sangat manis"
    print("manis" in txt)
    txt="buah itu rasanya sangat manis"
    print("pedas" in txt)
my_funcion()
print(" ")

print('Basic text python 4')
def my_funcion() :
    buah=["nanas"]
    print(len(buah))
my_funcion()
print(" ")

print('Basic text pyhton 5')
def my_funcion() :
    list1=["text 1 python"]
    objec=1
    status=True
    print(list1)
    print(objec)
    print(status)
my_funcion()
print(" ")

print('Basic text pyhton 6')
def my_funcion() :
    buah=["nanas","jambu"]
    print(buah[:1])
    buah=["nanas","jambu"]
    print(buah[:2])
my_funcion()
print(" ")

print('Basic text python 7')
def my_funcion() :
    buah=["nanas"]
    if "nanas" in buah:
        print("Ya :buah nanas terdaftar dari list")
my_funcion()
print(" ")

print('Basic text pyhton 8')
def my_funcion() :
    buah=["nanas"]
    buah.append("jambu")
    print(buah)
my_funcion()
print(" ")

print('Basic text python 9')
def my_funcion() :
    buah=["nanas"]
    buah.insert(1,"jambu")
    print(buah)
my_funcion()
print(" ")

print('Basic text pyhton 10')
def my_funcion() :
    list1=["text 1 python"]
    list2=["text 2 python"]
    list1.extend(list2)
    print(list1)
my_funcion()
print(" ")

print('Basic text python 11')
def my_funcion() :
    buah=["nanas","jambu"]
    buah.remove("jambu")
    print(buah)
my_funcion()
print(" ")

print('Basic text python 12')
def my_funcion() :
    buah=["nanas"]
    for x in "nanas":
        print(x)
my_funcion()
print(" ")

print('Basic text pyhton 13')
def my_funcion() :
    buah=["nanas","jambu"]
    newlist=[]
    for x in buah:
        if "a" in x:
            newlist.append(x)
    print(newlist)
my_funcion()
print(" ")

print('Basic text python 14')
def my_funcion() :
    buah=["nanas","jambu"]
    newlist=[x for x in buah if x!="jambu"]
    print(newlist)
my_funcion()
print(" ")

print('Basic text pyhton 15')
def my_funcion() :
    buah=["nanas","jambu"]
    newlist=[x for x in buah]
    print(newlist)
my_funcion()
print(" ")

print('Basic text python 16')
def my_funcion() :
    newlist=[x for x in range(5)]
    print(newlist)
    newlist=[x for x in range(10)]
    print(newlist)
my_funcion()
print(" ")

print('Basic text python 17')
def my_funcion() :
    buah=["nanas"]
    newlist=[x.upper() for x in buah]
    print(newlist)
my_funcion()
print(" ")

print('Basic text python 18')
def my_funcion() :
    buah=["nanas","pisang","jambu"]
    newlist=['jambu' for x in buah]
    print(newlist)
my_funcion()
print(" ")

print('Basic text python 19')
def my_funcion() :
    buah=["nanas"]
    newlist=[x if x!="nanas" else "jambu" for x in buah]
    print(newlist)
my_funcion()
print(" ")

print('Basic text python 20')
def my_funcion() :
    buah=["nanas","jambu","pisang"]
    buah.sort()
    print(buah)
my_funcion()
print(" ")

print('Basic text pyhton 21')
def my_funcion() :
    buah=["nanas","jambu","pisang"]
    buah.reverse()
    print(buah)
my_funcion()
print(" ")

print('Basic text python 22')
def my_funcion() :
    list1=["text 1 python"]
    list2=["text 2 python"]
    list3=["text 3 pyhton"]
    gabungan=list1+list2+list3
    print(gabungan)
my_funcion()
print(" ")

print('Basic text pyhotn 23')
def my_funcion() :
    import datetime
    time=datetime.datetime.now()
    print(time)
my_funcion()
print(" ")

print('Basic text pyhton 24')
def my_funcion() :
    import datetime
    time=datetime.datetime(2021,2,10)
    print(time)
my_funcion()
print(" ")

print('Basic text pyhton 25 pasword')
def my_funcion() :
    while True:
        pasword=input("masukan sadi anda :")
        if pasword=="farel":
            print("sandi anda di terima")
            break
        else:
            print("sandi anda salah cobalagi")
my_funcion()
print(" ")

print('Basic text pyhton 26 percakapan')
def my_funcion() :
    percakapan=input("masukan nama anda :")
    print("selamat datang :" +percakapan)
my_funcion()
print(" ")

print('Basic text python 27 myorder')
def my_funcion() :
    myorder="saya mempunyai mobil dengan merek {merek} , dan dengan series {series}"
    print(myorder.format(merek="TOYOTA" ,series="77,gop"))
    print(" ")
    myorder="saya mempunyai motor dengan merek {merek} , dan dengan serise {series}"
    print(myorder.format(merek="YAMAHA" ,series="4,221lop"))
my_funcion()
print(" ")

print('Basic text pyhton 28 myorder 2')
def my_funcion() :
    namabarang="kueh"
    jumlah=13
    harga="14.0000"
    myorder="saya ingin membeli {} dengan jumlah {} dan harga :Rp.{}"
    print(myorder.format(namabarang,jumlah,harga))
    namabarang="permen"
    jumlah=14
    harga=14
    myorder="saya ingin membeli {} dengan jumlah {} dan harga :$.{:.2f}"
    print(myorder.format(namabarang,jumlah,harga))
my_funcion()
print(" ")

print('Basic text pyhton 29 import json')
def my_funcion() :
    import json
    x={
        "NAMA" : "FAREL RIZAL FERDIAN NURHAKIM"
    }
    myvar=json.dumps(x)
    print(myvar)
my_funcion() 
print(" ")

print('Basic text pyhton 30 import pandas 1')
def my_funcion() :
    import pandas as pd
    mydataset={
        "mobil" : ["bmw"],
        "series" : [2011],
        "warna" : ["silver"]
    }
    myvar=pd.DataFrame(mydataset)
    print(myvar)
my_funcion()
print(" ")

print('Basic text pyhton 31 import pandas 2')
def my_funcion() :
    import pandas as pd
    a=[1,2,3,4]
    myvar=pd.Series(a,index=["True","True","True","True"])
    print(myvar)
my_funcion()
print(" ")

print('Basic text pyhton 32 import pandas 3')
def my_funcion() :
    import pandas as pd
    data={"data 1" :100,"data 2" :200,"data 3" :300}
    myvar=pd.Series(data)
    print(myvar)
my_funcion()
print(" ")

print('Basic text python 33 import pandas 4')
def my_funcion() :
    import pandas as pd
    data={"data 1" :100,"data 2" :200,"data 3" :300}
    myvar=pd.Series(data,index=["data 1","data 2"])
    print(myvar)
my_funcion()
print(" ")

print('Basic text pyhton 34 import pandas 5')
def my_funcion() :
    import pandas as pd
    data={
        "jumlah data":{
            "data 1" :[200],
            "data 2" :[200]
        },
        "subtotal":{
            "data 1" :[100],
            "data 2" :[300]
        },
        "total":{
            "data 1" :[300],
            "data 2" :[500]
        },
    }
    myvar=pd.DataFrame(data)
    print(myvar)
my_funcion()
print(" ")

print('Basic text pyhton 35 import data csv 1')
def my_funcion() :
    import pandas as pd
    df=pd.read_csv('data.csv')
    print(df.to_string())
my_funcion()
print(" ")

print('Basic text pyhton 36 import data csv 2')
def my_funcion() :
    import pandas as pd
    df=pd.read_csv('data2.csv')
    print(df)
my_funcion()
print(" ")

print('Basic text pyhton 37 import pandas data statistick 1')
def my_funcion() :
    import pandas as pd
    import matplotlib.pyplot as plt
    df=pd.read_csv('data.csv')
    df.plot()
    plt.show()
my_funcion()
print(" ")

print('Basic text python 38 import pandas data statistik 2')
def my_funcion() :
    import pandas as pd
    import matplotlib.pyplot as plt
    df=pd.read_csv('data2.csv')
    df.plot()
    plt.show()
my_funcion()
print(" ")

print('Basic text pyhton 39 import numpy data statistik 3')
def my_funcion() :
    import numpy as np
    from scipy.spatial import Delaunay
    import matplotlib.pyplot as plt
    points=np.array([
        [3,2],
        [2,1],
        [3,4],
        [4,2],
        [2,3]
    ])
    simplices=Delaunay(points).simplices
    plt.triplot(points[:,0] ,points[:,1],simplices)
    plt.scatter(points[:,0] ,points[:,1] ,color='r')
    plt.show()
my_funcion()
print(" ")

print('Basic text pyhton 40 import numpy data statistik 4')
def my_funcion() :
    import numpy as np
    from scipy.spatial import ConvexHull
    import matplotlib.pyplot as plt
    points=np.array([
        [2,3],
        [4,3],
        [5,2],
        [2,3],
        [2,4],
        [5,2],
        [2,4],
        [5,3],
        [3,5],
        [4,3]
    ])
    hull=ConvexHull(points)
    hull_points=hull.simplices
    plt.scatter(points[:,0],points[:,1])
    for simplex in hull_points:
        plt.plot=(points[simplex,0] ,points[simplex,1] ,'k-')
    plt.show()
my_funcion()




