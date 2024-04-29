num1 = float(input("Angka 1 : "))
num2 = float(input("Angka 2 : "))
ops  = input("Operasi : ")

while ops != "=":
    if ops == "+":
        hasil = num1 + num2
    elif ops == "-":
        hasil = num1 - num2
    elif ops == "x":
        hasil = num1 * num2
    elif ops == "/":
        hasil = num1 / num2
    elif ops =="%":
        hasil = num1 % num2
    else:
        print("Operasi yang anda masukan salah")

print (f"Hasil dari {num1} {ops} {num2} = {hasil}")