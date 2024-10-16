# Tabuada
numero = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# Contagem Regressiva
import time

for i in range(10, 0, -1):
    print(i)
    time.sleep(1)  # Espera 1 segundo entre os números
print("Fogo!")
