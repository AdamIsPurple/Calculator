def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Errore: divisione per zero!"
    return x / y

print("Operazioni disponibili:")
print("1. Addizione")
print("2. Sottrazione")
print("3. Moltiplicazione")
print("4. Divisione")

scelta = input("Scegli un'operazione (1/2/3/4): ")

try:
    num1 = float(input("Inserisci il primo numero: "))
    num2 = float(input("Inserisci il secondo numero: "))

    if scelta == '1':
        print("Risultato:", add(num1, num2))
    elif scelta == '2':
        print("Risultato:", subtract(num1, num2))
    elif scelta == '3':
        print("Risultato:", multiply(num1, num2))
    elif scelta == '4':
        print("Risultato:", divide(num1, num2))
    else:
        print("Scelta non valida")
except ValueError:
    print("Inserisci solo numeri validi.")

