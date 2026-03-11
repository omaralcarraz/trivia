nombre=input("introduce tu nombre")
bienvenida=print(f"Hola {nombre}, bienvenido a la trivia.")
instrucciones = print("responde correctamente las pregunetas para ganar puntos.")
puntos = 0

pregunta1 = input("cuantos angulos tiene un triangulo?")
respuesta_correcta1 = 3
if pregunta1 == respuesta_correcta1:
    print("respuesta correcta!!")
    puntos+=1
else:
    print(f"respuesta incorrecta, la respuesta era {respuesta_correcta1}")
    puntos=puntos
print(f"tus puntos acumulados son {puntos}")

pregunta2 = input("cuantos dias tiene una semana")
respuesta_correcta2 = 7
if pregunta2 == respuesta_correcta2:
    print("respuesta correcta!!")
    puntos+=1
else:
    print(f"respuesta incorrecta, la respuesta era {respuesta_correcta2}")
    puntos=puntos
print(f"tus puntos acumulados son {puntos}")

