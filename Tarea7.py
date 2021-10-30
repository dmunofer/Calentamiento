#Tarea 7
from random import randint
for i in range(0,51):
    print(i)

# Voy a suponer que cada helado te quita un 20% de hambre
dinero = 2000
edad = randint(0,50)
print(edad)
hambre = edad/100
helado = 100
num_helados = 0
if edad>=85:
    print("Ya estás satisfecho")
elif edad>=0 and edad<85:
    while hambre < 0.85:
        dinero = dinero - helado
        num_helados += 1
        helado = helado*1.20
        hambre = hambre + 0.2

    if dinero<0:
        print("No tienes dinero suficiente para saciarte con helados, te dara para"+f'{num_helados -1}')        
    else:
        print("Hasta estar satisfecho puedes comer "+ f'{num_helados} helados')
else:
    print("Intoduce una edad válida")


