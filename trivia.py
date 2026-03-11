nombre=input("introduce tu nombre")
bienvenida=print(f"Hola {nombre}, bienvenido a la trivia.")
instrucciones = print("responde correctamente las pregunetas para ganar puntos.")
puntos = 0

pregunta1 = input("cuantos angulos tiene un triangulo?")
respuesta_correcta1 = 3
if pregunta1 == respuesta_correcta1:
    puntos+=1
else:
    puntos=puntos
print(f"tus puntos acumulados son {puntos}")

pregunta2 = input("cuantos angulos tiene un triangulo?")
respuesta_correcta2 = 3
if pregunta2 == respuesta_correcta2:
    puntos+=1
else:
    puntos=puntos
print(f"tus puntos acumulados son {puntos}")

