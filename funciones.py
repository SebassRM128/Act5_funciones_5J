print("Ejemplo de funciones")
# declarando funciones
def hola():
    print("Alguien uso la funcion hola")

def chat(mensa):
    print(mensa)
def ellacontesta(mensa):
        print(f"chat ella: {mensa}")
def escribenombre(ap,n):
    print(f"Tu nombre completo es: {n} {ap}")
def suma(a,b):
    s=a+b
    return s
    
    # llamadas a funciones
hola()
chat("que bonita estas")
ellacontesta("gracias")
escribenombre("Sebastian","Rojas")
print(" ")
print("Operaciones basicas")
print(" ")
print("Suma")
c1=int(input("ingresa un numero"))
c2=int(input("ingresa un numero"))
damesuma=suma(c1,c2)
print(f"La suma de {c1} + {c2} = {damesuma}")

print(" ")
print("Resta")
def resta(a,b):
    s=a-b
    return s
c3=int(input("ingresa un numero"))
c4=int(input("ingresa un numero"))
dameresta=resta(c3,c4)
print(f"La resta de {c3} - {c4} = {dameresta}")

print(" ")
print("Multiplicacion")
def mult(a,b):
    s=a*b
    return s
c5=int(input("ingresa un numero"))
c6=int(input("ingresa un numero"))
damemult=mult(c5,c6)
print(f"La multiplicacion de {c5} * {c6} = {damemult}")

print(" ")
print("Diviision")
def div(a,b):
    s=a/b
    return s
c7=int(input("ingresa un numero"))
c8=int(input("ingresa un numero"))
damediv=div(c7,c8)
print(f"La division de {c7} / {c8} = {damediv}")
