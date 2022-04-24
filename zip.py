import random
import zipfile
import time

start_time = time.time()
number = int(input("패스워드의 자릿수 :"))

while True:
    set = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ.!'
    zfile = zipfile.ZipFile('text.zip', 'r')
    paw = ''

    for i in range(8,13):
        paw += random.choice(set)

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
