import random
import zipfile
import time

start_time = time.time()
number = int(input("패스워드의 자릿수 :"))
list1 = []
while True:
    set = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ.!'
    zfile = zipfile.ZipFile('text.zip', 'r')
    paw = ''

    for i in range(len(list1)):
        if list1[i] == paw:
            print("overlap")
    
    for i in range(0,2):
        paw += random.choice(set)
    list1.append(paw)
    
    if zfile:
        try:
            zfile.extractall(path='.', pwd=str(paw).encode('utf-8'))
            end_time = time.time()
            print("the compressed password is:", paw)
            print('It tooks %s seconds to crack the compressed file ' % (end_time-start_time))

            break

        except Exception as e:
            print('pass password: ', paw)
            pass
