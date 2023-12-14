import os
os.system('crs')

a = True
limit = 5
i = 0 #1,2,3,.....limit
while a:
    i+=1
    print(f'Menjalankan Program {limit -i+1}')
    if i==limit:
        a = False
    
        print('Program berhenti di sini')
    else:
        a = True    