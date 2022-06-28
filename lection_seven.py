from stringprep import in_table_a1


operandoA = int(input("Insert the first number:"))
operandoB = int(input("Insert the second number:"))
# OPERADOERES ARITMETIOS EN PYTHON
suma = operandoA + operandoB
print(f'Resultado de la resta: {suma}')

rest = operandoA - operandoB
print(f'Resultado de la resta: {rest}')

multiplicacion = operandoA * operandoB
print(f'Resultado de la multiplicacion: {multiplicacion}')

division = operandoA / operandoA
print(f'Resultado de la division: {division}')

divisionTipoEntero = operandoA // operandoB
print(f'Resultado de la division tipo entero {divisionTipoEntero}')

modulo = operandoA % operandoB
print(f'Resultado residuo division (MOdulo ): {modulo} ')

exponenete = operandoA ** operandoB
print(f'Resultado de exponenete: {exponenete}')
