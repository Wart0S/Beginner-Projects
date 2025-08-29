print("""*********************************

Fibonacci serisi bir sayıyı önceki iki sayıyı toplamı şeklinde oluşur.

Örnek;
2,2,4,6,10,16,26,42,68,110,178,288.............................

*********************************
""")

a = 2
b = 2

fibonacci = [a,b]

for i in range(100):

    a,b = b,a+b

    fibonacci.append(b)

print(fibonacci)