import random 

def dibujo_juego():
    dibujo = [""""
               ------
               |    |
               |    O
               |   /|\\
               |   / \\
               |
            ------
            """]
    return dibujo

def escoger_palabras():
    palabras = ['python', 'programacion', 'ahorcado', 'entregable', 'funciones']
    #palabra_facil= {'casa', 'letra', 'rojo', 'azul', 'lapiz'}
    return palabras[random.randint(0, len(palabras)  - 1)]
# Con Len se le dice a random.randint que debe ir desde el indice cero hasta el final de la longitud de la palabra 

def juego_esquema():
    palabra = escoger_palabras()
    intentos = len(palabra) - 1
    letras_intentadas = []
    palabra_adivinada = ["_"] * len(palabra) 

    print ("=============================================================================")
    print("\033[4;;47m" + "~~~~~~~~¡Bienvenido al juego de adivina la palabra! 👩‍💻~~~~~~~~" + "\033[0;m")
    print ("=============================================================================\n")
    
    print("Simulación del clásico juego del 'Ahorcado', donde se dispone de varios intentos para adivinar la palabra aleatoria.\n")
    print(f"Siguiendo este esquema:\n{dibujo_juego()}\n")
    print("*Instrucciones*:writing_hand:: Los intentos son proporcionales a la longitud de la palabra aleatoria.")
    print("Al obtener un acierto, se suma un punto; caso contrario, al perder, se van restando vidas.\n")

    datos_entrada = (str(input("¿Te gustaría jugar (Si / No): ")).strip()).capitalize() #Eliminar espacios, anticipar fallas

    if datos_entrada.capitalize() == "Si":
        print("Muchas gracias por su respuesta")
        nombre_usuario = str(input("Por favor ingrese su nombre: ")).capitalize()
        print(f"¡Bienvenidx al juego, {nombre_usuario}!")
        
    else:
        print("Ni modo")
    
    #Arreglar el try and except. Tal vez usar while para repetir el mensaje y que no cierre el zip
        print("Solo puedes elegir Sí o no :face_with_rolling_eyes:")
     
    #while intentos >= 0: #Necesita un bucle, while?
        #print(f"La palabra a adivinar es: {palabra_adivinada}")#No muestra los guiones
        #print (f"Letras intentadas: {letras_intentadas}")
        #print (f"Te quedan {intentos} intentos")    
        
    if datos_entrada == "Si":
        letra_escogida = str(input(f"Ingrese la letra escogida: ")).lower()

        if len(letra_escogida) == 1 and 'a' <= letra_escogida <= 'z':
            if letra_escogida in letras_intentadas:
                print("Ya intentaste esa letra.")
            elif letra_escogida in palabra:
                print(f"Felicidades, adivinaste una letra. Aún te quedan {intentos} por adivinar")
        else: 
            letras_intentadas.append(letra_escogida)
            print("Intenta con una nueva letra")

juego_esquema() 

print("\033[4;;47m" + "Esto es una prueba de color" + "\033[0;m") #Video de youtube
#La extensión de emojis no funcionó, borrar
