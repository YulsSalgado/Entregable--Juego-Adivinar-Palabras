import random 
def escoger_palabras():
    palabras = ['python', 'programacion', 'ahorcado', 'entregable', 'funciones']
    return palabras[random.randint(0, len(palabras) - 1)]

escoger_palabras() #???

# Con Len se le dice a random.randint que debe ir desde el indice cero hasta el final de la longitud de la palabra 

def juego_esquema():
    palabra = escoger_palabras()
    intentos = 6 #No sirve porque es una funcion, pero antes si servia
    letras_intentadas = []
    palabra_adivinada = ["_"] * len(palabra) #Var local, no global. Fix it >> Quitar la tercera funcion

    print("¡Bienvenido al juego del ahorcado!")

    while intentos >= 0: #Necesita un bucle, while?
        print(f"La palabra a adivinar es: {palabra_adivinada}")#No muestra los guiones
        print (f"Letras intentadas: {letras_intentadas}")
        print (f"Te quedan {intentos} intentos")    
        
    letra_escogida = input(f"Ingrese la letra escogida: ").lower
    
    if letra_escogida == 1 and "a" <= letra_escogida <= "z":
        if letra_escogida in letras_intentadas:
            print("Ya intentaste con esa letra")
        if letra_escogida in palabra:
            print(f"Felicidades, adivinaste una letra. Aún te quedan {intentos} por adivinar")
        else: 
            letras_intentadas.append(letra_escogida)
            print("Intenta con una nueva letra")

print("Prueba while")    

juego_esquema() 
#Sigue andando el bucle while de forma infinita, pero no marca error como ayer

