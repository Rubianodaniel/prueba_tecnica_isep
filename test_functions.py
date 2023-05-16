import pytest
from ejecicio1 import (evaluate, sum_num_pairs, count_word, ordered_lst,
                        sum_natural_num,merge_lst)

@pytest.mark.parametrize("number, expected_result", [
    (1, 1),
    (3, "Fizz"),
    (5, "Buzz"),
    (15, "FizzBuzz"),
    (20, "Buzz"),
    (-9, "Fizz"),
    (-10, "Buzz"),
    (-30, "FizzBuzz"),
    (8, 8)
])
def test_evaluate(number, expected_result):
    result = evaluate(number)
    assert result == expected_result



@pytest.mark.parametrize("lst_num, expected_result", [
    ([1, 2, 3, 4, 5], 6),
    ([2, 4, 6, 8, 10], 30),
    ([1, 3, 5, 7, 9], 0),
    ([], 0)
])
def test_sum_num_pairs(lst_num, expected_result):
    result = sum_num_pairs(lst_num)
    assert result == expected_result


@pytest.mark.parametrize("cadena, expected_result", [
    ("Hola cómo estás", 3),
    ("", 0),
    ("Python", 1),
    ("Hola        mundo", 2),
    (1, "Error: No es una cadena de texto")
    
])
def test_count_word(cadena, expected_result):
    assert count_word(cadena) == expected_result



@pytest.mark.parametrize("cadena, expected_result", [
    ("Hola cómo estás", 3),
    ("", 0),
    ("Python", 1),
    ("Hola        mundo", 2),
    (1, "Error: No es una cadena de texto")
])
def test_count_word(cadena, expected_result):
    assert count_word(cadena) == expected_result



@pytest.mark.parametrize("lst_numbers, expected_result", [
    ([4, 2, 7, 1, 5], [1, 2, 4, 5, 7]),
    ([10, 3, 8, 6, 2], [2, 3, 6, 8, 10]),
    ([1], [1]),
    ([], []),
    ([4, "6", 2.5], ValueError),
    (["a", "b", "c"], ValueError)
])
def test_ordered_lst(lst_numbers, expected_result):
    if expected_result == ValueError:
        with pytest.raises(ValueError):
            ordered_lst(lst_numbers)
    else:
        assert ordered_lst(lst_numbers) == expected_result


@pytest.mark.parametrize("number, expected_result", [
    (10, 33),  # 3 + 5 + 6 + 9 + 10 = 33
    (15, 60),  # 3 + 5 + 6 + 9 + 10 + 12 + 15 = 60
    (0, 0),  # No hay números naturales múltiplos de 3 o 5
    (-5, "Error: El número debe ser mayor o igual a cero"),  # Número negativo
    ("abc", "Error: El argumento debe ser un número"),  # Argumento no numérico
    (7.5, "Error: El argumento debe ser un número")  # Argumento no entero
])
def test_sum_natural_num(number, expected_result):
    assert sum_natural_num(number) == expected_result



@pytest.mark.parametrize("lst_number1, lst_number2, expected_result", [
    ([1, 2, 3, 4, 5], [4, 5, 6, 7, 8], [4, 5]),  # Números comunes: 4, 5
    ([1, 2, 3], [4, 5, 6], []),  # Sin números comunes
    ([], [4, 5, 6], []),  # primer lista vacia
    ([1, 2, 3], [], []),  # Segunda lista vacía
    ([], [], []),  # Segunda lista vacía

    ([1, 2, 'a', 4, 5], [4, 'b', 5, 6, 7], ValueError("Error: Las listas deben contener solo números enteros o decimales.")),  # Elementos no numéricos en ambas listas
    ([1, 2, 3], ['a', 'b', 'c'], ValueError("Error: Las listas deben contener solo números enteros o decimales."))  # Elementos no numéricos en una lista
])
def test_merge_lst(lst_number1, lst_number2, expected_result):
    if isinstance(expected_result, ValueError):
        with pytest.raises(ValueError) as e:
            merge_lst(lst_number1, lst_number2)
        assert str(e.value) == str(expected_result)
    else:
        result = merge_lst(lst_number1, lst_number2)
        assert result == expected_result



