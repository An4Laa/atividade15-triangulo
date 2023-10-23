med1 = int(input("Digite medida 1: "))
med2 = int(input("Digite medida 2: "))
med3 = int(input("Digite medida 3: "))

if med1 < med2 + med3 and med2 < med1 + med3 and med3 < med1 + med2 :
    print("Com essas medidas, um triângulo pode sim ser formado.")
else : 
    print("Com essas medidas, não é possível formar um triângulo.")