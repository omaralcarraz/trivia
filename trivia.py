nombre=input("introduce tu nombre: ")
bienvenida=print(f"Hola {nombre}, bienvenido a la trivia.")
instrucciones = print("responde correctamente las preguntas para ganar puntos.")
puntos = 0

pregunta1 = int(input("cuantos angulos tiene un triangulo?: "))
respuesta_correcta1 = 3

if pregunta1 == respuesta_correcta1:
    puntos=puntos+1    
    print("respuesta correcta!!")
    
else:
    print(f"respuesta incorrecta, la respuesta era {respuesta_correcta1}")
    puntos=puntos
print(f"tus puntos acumulados son {puntos}")

pregunta2 = int(input("cuantos dias tiene una semana?: "))
respuesta_correcta2 = 7

if pregunta2 == respuesta_correcta2:
    puntos=puntos+1
    print("respuesta correcta!!")
    
else:
    print(f"respuesta incorrecta, la respuesta era {respuesta_correcta2}")
    puntos=puntos

print(f"tus puntos acumulados son {puntos}")

pregunta3 = int(input("cuantas vocales hay en la palabra 'muricelago'?: "))
respuesta_correcta3 = 5

if pregunta3 == respuesta_correcta3:
    puntos=puntos+1    
    print("respuesta correcta!!")
    
else:
    print(f"respuesta incorrecta, la respuesta era {respuesta_correcta3}")
    puntos=puntos
print(f"tus puntos acumulados son {puntos}")

pregunta4 = int(input("cuanto es 48-13?: "))
respuesta_correcta4 = 35

if pregunta4 == respuesta_correcta4:
    puntos=puntos+1
    print("respuesta correcta!!")
    
else:
    print(f"respuesta incorrecta, la respuesta era {respuesta_correcta4}")
    puntos=puntos

print(f"conseguiste un total de {puntos} puntos")
