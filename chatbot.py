# Diccionario con claves y respuestas
respuestas = {
    "hola": "¡Hola! ¿Cómo estás?",
    "adiós": "¡Adiós! Que tengas un buen día.", 
    "cómo estás": "Muy bien, gracias. ¿Y tú?", 
    "gracias": "¡De nada!"
}
print(" Chatbot iniciado. Escribe 'salir' para terminar.")
while True:
    mensaje = input("Tú: ").lower()

    if mensaje == "salir":
        print("Bot: ¡Adiós!")
        break

    encontrado = False
    for clave in respuestas:
        if clave in mensaje:
            lista_respuestas = respuestas[clave]
            print("Bot:", lista_respuestas)
            encontrado = True
            break

    if not encontrado:
        print("Bot: Lo siento, no entendí eso.")