#Este codigo ha sido generado por el modulo psexport 20230904-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


# En python no hay forma de elegir como pasar una variable a una
# funcion (por referencia o por valor). Las variables "inmutables"
# (str, int, float, bool) se pasan siempre por copia mientras que
# las demas (listas, objetos, etc.) se pasan siempre por referencia.
# Esto coincide con el comportamiento por defecto en pseint, pero
# cuando utiliza las palabras clave "Por Referencia" para
# alterarlo la traducción no es correcta.

def mp(num3, num4):
	esmultiplo = bool()
	if num3%num4==0:
		esmultiplo = True
	else:
		esmultiplo = False
	return esmultiplo

if __name__ == '__main__':
	num1 = int()
	num2 = int()
	resultado = bool()
	print(" ingrese un numero a evaluar")
	num1 = int(input())
	num2 = int(input())
	resultado = mp(num1, num2)
	print(" El resultado multiplo es ",resultado)
	if resultado:
		print(" el numero 1 es multiplo del num 2")
	else:
		print(" El numero 1 no multiplo del num 2")

