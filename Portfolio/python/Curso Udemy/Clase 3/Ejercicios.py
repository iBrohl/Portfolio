'''Crear un programa, que tenga una variable con la cadena "Te quiero
solo como amigo", y muestre la siguiente información:
• Imprima los dos primeros caracteres.
• Imprima los tres últimos caracteres.
• Imprima dicha cadena cada dos caracteres. Ej.: Si la cadena fuera
"recta" debería imprimir rca
• Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola
mundo! debe imprimir !odnum aloh
• Imprima la cadena en un sentido y en sentido inverso. Ej: Si la
cadena es "reflejo" imprime reflejoojelfer.'''


"Ejercicio 1"

# cadena = "Te\b q\bui\ber\bo \bso\blo\b c\bom\bo \bam\big\bo" No hace falta hacer esto

# # print(cadena[0:2])
# # print(cadena[-3: ])
# print(cadena)

# cadena = "Te quiero solo como amigo"
# print(cadena[: : 2])

# cadena = "Te quiero solo como amigo"
# print(cadena [: : -1])

# cadena = "Te quiero solo como amigo"
# print(cadena + cadena[: : -1])


'''Crear un programa que tenga una variable con la cadena "Separado"
y un carácter de coma (,); e inserte el carácter entre cada letra de la
cadena. Ej: separar y, deberia devolver s,e,p,a,r,a,r
Pista: Debes utilizar un método de las cadenas llamado "Replace",
recuerda que la posición de los caracteres empieza en 0.'''

"Ejercicio 2"


# cadena = "eparado"

# print(cadena)

# reemplazar = cadena.replace("",",")
# print("S",reemplazar)

#·NOTA: Aparece S, e,p,a,r,a,d,o, Necesito quitar la coma del final y el espacio entre S, y e