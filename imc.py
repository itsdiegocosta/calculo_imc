print("-"*40)
print(" "*20, "Calculadora IMC")
print("-"*40)
print("Referência: https://www.ncbi.nlm.nih.gov/books/NBK541070/")
print("-"*40)

massa = float (input("Qual a sua massa corporal?:  "))
estatura= float (input("Qual a sua estatura?:  "))
imc= massa/estatura**2
imcr= round(imc)
print("seu índice de massa corporal é", imcr)
if imc < 18.5:
	print("Você está abaixo do peso ideal")
elif 18.5 < imc <=24.9:
	print("Você está no peso ideal")
elif 25 < imc <=29.9:
	print("Você está com sobrepeso")
elif 30 < imc <=34.9:
	print("Você está classificado como obeso grau 1")
elif 35 < imc <=39.9:
	print("Você está classificado como obeso grau 2")
elif 40 < imc:
	print("Você está classificado como obeso morbido")
else:
	print("digite um valor válido")