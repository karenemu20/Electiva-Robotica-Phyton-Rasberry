import math

def volumen_prisma(base, altura):
    return base * altura

def volumen_piramide(base, altura):
    return (1/3) * base * altura

def volumen_cono(radio, altura):
    return (1/3) * math.pi * radio**2 * altura

def volumen_cilindro(radio, altura):
    return math.pi * radio**2 * altura

valor = 0 

def main():  
    print("CÁLCULO DE VOLUMENES")
    print("Seleccione el sólido del que desea calcular el volumen:")
    print("1. Prisma")
    print("2. Pirámide")
    print("3. Cono")
    print("4. Cilindro")
    print("5. SALIR")
        
    opcion = int(input("Seleccione una opción: "))
        
    if opcion == 1:
            base = float(input("Ingrese la base del prisma (cm): "))
            altura = float(input("Ingrese la altura del prisma (cm): "))
            resultado = volumen_prisma(base, altura)
            print("El volumen del prisma es:", resultado, 'cm3')
    elif opcion == 2:
            base = float(input("Ingrese la base de la pirámide (cm): "))
            altura = float(input("Ingrese la altura de la pirámide (cm): "))
            resultado = volumen_piramide(base, altura)
            print("El volumen de la pirámide es:", resultado,'cm3')
    elif opcion == 3:
            radio = float(input("Ingrese el radio del cono (cm):"))
            altura = float(input("Ingrese la altura del cono(cm): "))
            resultado = volumen_cono(radio, altura)
            print("El volumen del cono es:", resultado,'cm3')
    elif opcion == 4:
            radio = float(input("Ingrese el radio del cilindro (cm): "))
            altura = float(input("Ingrese la altura del cilindro (cm): "))
            resultado = volumen_cilindro(radio, altura)
            print("El volumen del cilindro es:", resultado,'cm3')
    elif opcion == 5:
            print("Programa finalizado")
            valor = 5
    else:
            print("Opción no válida. Por favor, seleccione un número del 1 al 5.")
    return valor

if __name__ == "__main__":
  
    while valor != '5':
        main()
