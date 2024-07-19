import math

## BASE DE CONSULTAS BÁSICAS


##### Inteiros (int)
## 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

primeiro_numero = int(input("Insira o primeiro número: "))
segundo_numero = int(input("Insira o segundo número: "))
resultado_soma = primeiro_numero + segundo_numero
print(resultado_soma)

## 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

numero = int(input("Insira um número: "))
resultado_resto = numero % 5
print("O resto da divisão por cinco é: ", resultado_resto)

## 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

p_numero = int(input("Insira o primeiro número: "))
s_numero = int(input("Insira o segundo número: "))
num = p_numero * s_numero
resultado = num
print(resultado)

## 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

p_num = int(input("Insira um número inteiro: "))
s_num = int(input("Insira segundo número inteiro: "))
resultado = p_num // s_num
print(resultado)

## 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

num = int(input("Insira um número para o calculo do quadrado: "))
calculo = num ** 2
resultado = calculo
print(calculo)

##### Números de Ponto Flutuante (float)

## 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

num_01 = float(input("Insira um número: "))
num_02 = float(input("Insira um segundo número: "))
soma = num_01 + num_02
resultado = soma
print(soma)

## 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

num_01 = float(input("Insira um número: "))
num_02 = float(input("Insira o segundo número: "))
media = (num_01 + num_02) / 2
print("A média é: ", media)

## 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

base = float(input("Digite a base: "))
expoente = float(input("Digite o expoente: "))
potencia = base ** expoente
print("O resultado da potência é: ", potencia)

## 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C é igual a {fahrenheit}°F")

## 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

raio_circulo = float(input("Digite o raio: "))
area_circulo = math.pi * raio_circulo ** 2
    # área formatada = "{:.2f}" .format(area_circulo)
    # maneira mais apropriada:
print(f"{area_circulo:.2f}")

##### Strings (str)

## 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

texto = input("Digite um texto: ")
texto_maiusculas = texto.upper()
print("Texto em maiúsculas:", texto_maiusculas)

## 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

texto = input("Digite um texto: ")
texto_minusculas = texto.lower()
print("Texto em minusculas:", texto_minusculas)

## 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

frase = input("Digite uma frase: ")
frase_sem_espacos = frase.strip()
print("Frase sem espaços no início e no final:", frase_sem_espacos)

## 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

try: 
    
    data_do_usuario = input("Insira uma data no formato dd/mm/aaaa: ")
    lista_dd_mm_aaaa = data_do_usuario.split("/")
    print(f"Dia é: {lista_dd_mm_aaaa[0]}")
    print(f"Mês é: {lista_dd_mm_aaaa[1]}")
    print(f"Ano é: {lista_dd_mm_aaaa[2]}")

except: print( "Insira uma data válida")

## 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

parte1 = input("Digite a primeira parte do texto: ")
parte2 = input("Digite a segunda parte do texto: ")
texto_concatenado = parte1 + parte2
print("Texto concatenado:", texto_concatenado)

##### Booleanos (bool)

## 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

valor1 = True
valor2 = False
resultado_and = valor1 and valor2
print("Resultado do AND lógico:", resultado_and)

## 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

resultado_or = valor1 or valor2
print("Resultado do OR lógico:", resultado_or)

## 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

resultado_not = not valor1
print("Resultado do NOT lógico:", resultado_not)

## 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

num1 = 5
num2 = 5
resultado_igualdade = (num1 == num2)
print("Resultado da igualdade:", resultado_igualdade)

## 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

resultado_diferenca = (num1 != num2)
print("Resultado da diferença:", resultado_diferenca)


## try -except e if

## 21. Conversor de temperatura
## 22. Verificador de Palíndromo
## 23. Calculadora simples
## 24. Classificador de números
## 25. Conversão de tipo com Validação