#break
#printah khusus guna memaksa melakukan perulangan sebelum waktunya.
#misalnya contoh 1

angka = int(input("masukkan angka:"))
number = 0

while number < angka:
    number += 1
    print(number) # aksi 1

    if number == 3:
        print("upss") 
        break #loop akan berhenti terpaksa ketika number = 3
    print ("oke")#aksi 2


#contoh 2 membuat program menghitung

angka = int(input("hitung sampai:"))
number = 0
while True :
    number += 1
    print (number)

    if number == angka:
         print ( "stop" )
         break
        
   
   
       

