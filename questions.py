import random

# Preguntas para el juego
questions = ["¿Qué función se usa para obtener la longitud de una cadena en Python?",
"¿Cuál de las siguientes opciones es un número entero en Python?",
"¿Cómo se solicita entrada del usuario en Python?",
"¿Cuál de las siguientes expresiones es un comentario válido en Python?",
"¿Cuál es el operador de comparación para verificar si dos valores son iguales?",]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
#unificamos las 3 listas en 1
questions_to_ask = random.sample(list(zip(questions,answers, correct_answers_index)), k=3)
#inicializamos el puntaje en 0
point=0
# El usuario deberá contestar 3 preguntas
for questions,answers,correct_answers_index in questions_to_ask:
    # Se muestra la pregunta y las respuestas posibles
    print(questions)
    for i, answer in enumerate(answers):
        print(f"{i + 1}. {answer}")
    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_put =(input("Respuesta: "))
        #se verifica si la respuesta es un numero
        if  not user_put.isdigit():
            print("Respuesta no valida, no se permiten letras")
            exit(1)
        #se verifica si el numero ingresado esta entre el rango posible de las respuesta
        num= int(user_put)
        if num<1 or num>4:
            print("Respuesta no valida(rango entre 1-4)")
            exit(1)
        user_answer= int(num) -1
        # Se verifica si la respuesta es correcta
        if user_answer == correct_answers_index:
            point+=1
            print("¡Correcto!")
            break
        else:
            point-=0.5
            
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(answers
[correct_answers_index])
print('el puntaje final es',point)
#Se imprime un blanco al final de la pregunta
print()