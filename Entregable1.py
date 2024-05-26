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
    """
    Función que devuelve una palabra aleatoria de una lista de palabras
    
    Parámetro: 
    None 
    
    Returns: 
    str: Una palabra random desde una lista predefinida de palabras.
    """
    palabras = ['python', 'programacion', 'ahorcado', 'entregable', 'funciones']
    #palabra_facil= {'casa', 'letra', 'rojo', 'azul', 'lapiz'}
    return palabras[random.randint(0, len(palabras)  - 1)]

def juego_esquema():
    palabra = escoger_palabras()
    intentos = len(palabra) - 1
    letras_intentadas = []
    aciertos = []
    palabra_adivinada = ["_"] * len(palabra) 

    print ("=============================================================================")
    print("\033[4;;47m" + "~~~~~~~~¡Bienvenido al juego de adivina la palabra! 👩‍💻~~~~~~~~" + "\033[0;m")
    print ("=============================================================================\n")
    
    print("Simulación del clásico juego del 'Ahorcado', donde se dispone de varios intentos para adivinar la palabra aleatoria.\n")
    #print(f"Siguiendo este esquema:\n{dibujo_juego()}\n")
    print("Instrucciones✍: Los intentos son proporcionales a la longitud de la palabra aleatoria.")
    print("Al obtener un acierto, se suma un punto; caso contrario, al perder, se van restando vidas.\n")
    
    while True:
        try:
            datos_entrada = (str(input("¿Te gustaría jugar (Si / No): ")).capitalize()).strip() #Eliminar espacios, anticipar fallas
            if datos_entrada.capitalize() not in ["Si", "No"]:
                raise ValueError ("Solo puedes elegir Sí o no 🙄")
            
            if datos_entrada.capitalize() == "Si":
                print("Muchas gracias por su respuesta")
                nombre_usuario = str(input("Por favor ingrese su nombre: ")).capitalize()
                print(f"¡Bienvenidx al juego, {nombre_usuario}!")
                print(f"La palabra a adivinar es: {palabra_adivinada}") 
                break

            else:
                print("Gracias por participar. ¡Esperamos te animes a una próxima!")
                return

        except ValueError as e:
            print(e)
            
     
    #while intentos >= 0 and datos_entrada == "Si":
        # ??? No tiene sentido
    if datos_entrada == "Si":
        letra_escogida = str(input(f"Ingrese la letra escogida: ")).lower()

    while intentos >= 0 and aciertos == len(palabra):
        print (f"Letras intentadas: {letras_intentadas}")
        print (f"Te quedan {intentos} intentos")    

        if len(letra_escogida) == 1 and 'a' <= letra_escogida <= 'z':
            if letra_escogida in letras_intentadas:
                print("Ya intentaste esa letra.")
            elif letra_escogida in palabra:
                print(f"Felicidades, adivinaste una letra. Aún te quedan {intentos} por adivinar")
                aciertos =+ 1
        else: 
            letras_intentadas.append(letra_escogida)
            print("Intenta con una nueva letra")

juego_esquema() 