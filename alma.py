print ("Hola usuario")
print ("Bienvenido a la escuela.")
edad = int(input("Bueno... empecemos: ¿Cuántos años tienes? "))
print ("Ok. Tengo tres materias que ofrecerte. Tú deberás elegir una:")
print ("a Ciencias")
print ("b Religión")
print ("c Matemáticas")
opc = input("Elige la letra de la opción: ")

while opc == "a" :
    porcentaje = int(input("¿Cuántas personas de ustedes diez asistirán? "))
    total = (porcentaje * 10) / 100
    print (f"El porcentaje de ustedes diez que asisten a la clase es {total}%")
