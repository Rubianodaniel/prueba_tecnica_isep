#1 Crea una función que tome un número como entrada y devuelva "Fizz" si el número es divisible por 3,
#  "Buzz" si es divisible por 5 y "FizzBuzz" si es divisible por ambos. En caso contrario,
#  la función debe devolver el número. (0.5 punto)


def evaluate(number):

    """
    Evalúa un número y devuelve una cadena de texto basada en las siguientes reglas:
    - Si el número es divisible por 3 y por 5, devuelve "FizzBuzz".
    - Si el número es divisible por 3, devuelve "Fizz".
    - Si el número es divisible por 5, devuelve "Buzz".
    - En cualquier otro caso, devuelve el número.
    
    Parámetros:
    - number: Un número entero o decimal a evaluar.
    
    Retorna:
    - Una cadena de texto o el número evaluado.
    
    Raises:
    - TypeError: Si el argumento no es un número.
    """
    try:
        if number % 3 == 0 and number % 5 == 0:
            return "FizzBuzz" 

        elif number % 3 == 0:
            return "Fizz"
        elif number % 5 == 0:
            return "Buzz"
        else:
            return number 
    except TypeError:
        return "Error: El argumento debe ser un número."


2#Crea una función que tome una lista de números como entrada 
# y devuelva la suma de todos los números pares en la lista. (0.5 punto)


def sum_num_pairs(lst_num):
    """
    Toma una lista de números como entrada y devuelve la suma de todos los números pares en la lista.
    
    Parámetros:
    - lst_num: Una lista de números.
    
    Retorna:
    - La suma de todos los números pares en la lista.
    
    Raises:
    - TypeError: Si el argumento no es una lista de números.
    - ValueError: Si el argumento no es una lista válida.
    """
    try:
        num_pairs = [number for number in lst_num if number % 2 == 0]
        return sum(num_pairs)
    except (TypeError, ValueError):
        return "Error: No es una lista de numeros"



# Escribe una función que tome una cadena de texto como entrada y devuelva el número de palabras que contiene. 
# Se considera que una palabra es cualquier secuencia de caracteres separada por espacios. (0.5 punto)

def count_word(cadena):
    """
    Toma una cadena de texto como entrada y devuelve el número de palabras que contiene.
    Se considera que una palabra es cualquier secuencia de caracteres separada por espacios.
    
    Parámetros:
    - cadena: Una cadena de texto.
    
    Retorna:
    - El número de palabras en la cadena de texto.
    
    Raises:
    - AttributeError: Si el argumento no es una cadena de texto.
    """
    try:
        lst_cadena = cadena.split()
        return len(lst_cadena)
    except AttributeError:
        return "Error: No es una cadena de texto"
    


def ordered_lst(lst_numbers):
    """
    Toma una lista de números como entrada y devuelve una nueva lista con los mismos elementos, 
    ascendentemente
    
    Parámetros:
    - lst_numbers: Una lista de números enteros o decimales.
    
    Retorna:
    - Una lista ordenada de menor a mayor.
    
    Raises:
    - ValueError: Si la lista contiene elementos que no son números enteros o decimales.
    """
    if not all(isinstance(num, (int, float)) for num in lst_numbers):
        raise ValueError("Error: La lista debe contener solo números enteros o decimales.")
    if len(lst_numbers) <= 1:
        return lst_numbers
    partition = lst_numbers[len(lst_numbers) // 2]
    minor = [number for number in lst_numbers if number < partition]
    equals =[number for number in lst_numbers if number == partition]
    major = [number for number in lst_numbers if number > partition]
    return ordered_lst(minor) + equals + ordered_lst(major)



## 5. Escribe una función que tome un número como entrada
#  y devuelva la suma de todos los números naturales menores o
#  iguales a ese número que son múltiplos de 3 o 5. (0.5 punto)


def sum_natural_num(number):
    """
    Toma un número como entrada y devuelve la suma de todos los números naturales menores o iguales
    a ese número que son múltiplos de 3 o 5.
    
    Parámetros:
    - number: Un número entero.
    
    Retorna:
    - La suma de los números naturales menores o iguales al número dado que son múltiplos de 3 o 5.
    
    Raises:
    - TypeError: Si el argumento no es un número.
    - ValueError: Si el número es negativo.
    """
    try:
        if number >= 0:
            natural_number = [ i for i  in range(0,number + 1) if i % 3 == 0 or i % 5 == 0]
            return sum(natural_number)
        else:   
            raise ValueError("Error: El número debe ser mayor o igual a cero")
    except TypeError:
        return "Error: El argumento debe ser un número"
    except ValueError as e:
        return str(e)

#6 Crea una función que tome dos listas como entrada y devuelva una lista que contenga 
# todos los elementos que se encuentran en ambas listas. 

def merge_lst(lst_number1, lst_number2):
    """
    Toma dos listas como entrada y devuelve una lista que contiene todos los elementos que se encuentran en ambas listas.
    
    Parámetros:
    - lst_number1: Una lista de números enteros o decimales.
    - lst_number2: Una lista de números enteros o decimales.
    
    Retorna:
    - Una lista que contiene todos los elementos que se encuentran en ambas listas.
    
    Raises:
    - ValueError: Si las listas contienen elementos que no son números enteros o decimales.
    """
    if not all(isinstance(num, (int, float)) for num in lst_number1 + lst_number2):
        raise ValueError("Error: Las listas deben contener solo números enteros o decimales.")
    lst_merge = [element for element in lst_number1 if element in lst_number2]
    return ordered_lst(lst_merge)


# 7. Escribe una función que tome una cadena de texto como entrada y devuelva la misma cadena de texto invertida. 
def invertir_cadena(cadena):
    """
    Toma una cadena de texto como entrada y devuelve la misma cadena de texto invertida.
    
    Parámetros:
    - cadena: Una cadena de texto.
    
    Retorna:
    - La cadena de texto invertida.
    """
    return cadena[::-1]


#8. Crea una función que tome un número como entrada y devuelva el factorial de ese número. 
# El factorial de un número es el producto de todos los enteros positivos desde 1 hasta el número 
# en cuestión. (0.5 punto)


def factorial(number):
    """
    Toma un número como entrada y devuelve el factorial de ese número.
    El factorial de un número es el producto de todos los enteros positivos desde 1 hasta el número en cuestión.
    
    Parámetros:
    - number: Un número entero no negativo.
    
    Retorna:
    - El factorial del número dado.
    """
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)


if __name__=="__main__":
    # 1 ejercicio 
    print("ejercicio 1: ",evaluate(20))
    #  2 ejercicio 
    print("ejercicio 2: ",sum_num_pairs([5,4,3,6,85,8,4,6,92,546,21,1]))
    # 3 ejercicio 
    print("ejercicio 3: ",count_word("hola soy daniel"))
    # 4 ejercicio 
    print("ejercicio 4: ",ordered_lst([3,4,8,-1,50,-3,55]))
    # 5 ejercicio
    print("ejercicio 5: ",sum_natural_num(20))
    # 6 ejercicio
    print("ejercicio 6: ",merge_lst(lst_number1=[1,5,6,8,7,9,2],lst_number2=[1,8,5,33,55,7]))
    #7 ejercicio
    print("ejercicio 7: ",invertir_cadena("hola soy daniel"))
    #8 ejercicio
    print("ejercicio 8: ",factorial(5))
