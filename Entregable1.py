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
    palabras = ['python', 'programacion', 'ahorcado', 'entregable', 'funciones', 'libertad', 'casa', 'helicoptero']
    return palabras[random.randint(0, len(palabras)  - 1)]

def juego_esquema():
    """
    Función principal del código que simula el juego del 'Ahorcado'.
    Dos bucles while para seguimiento: datos de entrada y secuencias.

    Párametros: 
    None

    Returns: Mensajes de datos de entrada.
    """
    palabra = escoger_palabras()
    intentos = len(palabra) - 1
    letras_intentadas = []
    aciertos = 0
    palabra_acierto = palabra
    palabra_adivinar = ["_"] * len(palabra) 

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
                raise ValueError ("Solo puedes elegir Sí o no 🙄\n")
            
            if datos_entrada.capitalize() == "Si":
                print("Muchas gracias por su respuesta")
                nombre_usuario = str(input("Por favor ingrese su nombre: ")).capitalize()
                print(f"¡Bienvenidx al juego, {nombre_usuario}!\n")
                break

            else: 
                print("Gracias por participar. ¡Esperamos te animes a una próxima!\n")
                input("Presiona Enter para salir...")
                return

        except ValueError as e:
            print(e)
            
    print("=============================================================================")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ¡Juego iniciado!😃 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("=============================================================================" + "\n") 

    while intentos > 0 and "_" in palabra_adivinar:
        print(f"Tienes {intentos} intentos en esta ronda")
        print(f"La palabra a adivinar es: {palabra_adivinar}") 
        print (f"Letras intentadas: {letras_intentadas}")

        if datos_entrada.capitalize() == "Si":
            letra_escogida = str(input(f"Ingrese la letra escogida: ")).lower()
            print("\n")

        if len(letra_escogida) == 1 and 'a' <= letra_escogida <= 'z':

            if letra_escogida in letras_intentadas:
                print("Ya intentaste esa letra.\n")
            else: 
                letras_intentadas.append(letra_escogida)
                if letra_escogida in palabra:
                    #Se debe actualizar el esquema, iterar
                    for i in range(len(palabra)):
                        if palabra[i] == letra_escogida:
                            palabra_adivinar[i] = letra_escogida #Indice de la palabra a adivinar sea igual a l_e
                    print(f"Felicidades, adivinaste una letra :) \n")
                    aciertos += 1
                elif letra_escogida not in palabra:
                    print("Lo siento. Letra incorrecta :( \n")
                    intentos -= 1
        
        else:
            print("Por favor, ingrese una única letra válida.\n")

    if "_" not in palabra_adivinar:
        print("                        ¡JUEGO TERMINADO!\n                            ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"¡Felicidades {nombre_usuario}!. Tu puntuación fue de {aciertos} puntos.")
        print(f"La palabra para adivinar era: {palabra}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    else: 
        print("                        ¡JUEGO TERMINADO!\n                            ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"Bueno {nombre_usuario}, la vida es triste. Tus aciertos fueron: {aciertos}")
        print(f"La palabra para adivinar era: {palabra}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    input("Presiona Enter para salir...")

juego_esquema() 

