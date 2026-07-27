# Classwork 16 - Recursive Functions
# Armando Karin Molina Marrufo

import json

# ============================================================
# 1. recursiva(n) — countdown from n to 1
# ============================================================

def recursiva(n):
    # INPUT validation
    if not isinstance(n, int):
        raise TypeError(f"recursiva() expects an integer, got {type(n).__name__}")
    if n < 0:
        raise ValueError(f"recursiva() does not accept negative numbers, got {n}")
    # BASE CASE
    if n == 0:
        return "Done!"
    # RECURSIVE CASE
    print(n)
    return recursiva(n - 1)

# ============================================================
# 2. fibonacci(n) — nth Fibonacci number
# ============================================================

def fibonacci(n):
    # INPUT validation
    if not isinstance(n, int):
        raise TypeError(f"fibonacci() expects an integer, got {type(n).__name__}")
    if n < 0:
        raise ValueError(f"fibonacci() does not accept negative numbers, got {n}")
    # BASE CASE
    if n == 0 or n == 1:
        return n
    # RECURSIVE CASE
    return fibonacci(n - 1) + fibonacci(n - 2)

# ============================================================
# 3. factorial(n) — n!
# ============================================================

def factorial(n):
    # INPUT validation
    if not isinstance(n, int):
        raise TypeError(f"factorial() expects an integer, got {type(n).__name__}")
    if n < 0:
        raise ValueError(f"factorial() does not accept negative numbers, got {n}")
    # BASE CASE
    if n == 0 or n == 1:
        return 1
    # RECURSIVE CASE
    return factorial(n - 1) * n

# ============================================================
# 4. multiplicacion_recursiva(n, m) — n * m via repeated addition
# ============================================================

def multiplicacion_recursiva(n, m):
    # INPUT validation
    if not isinstance(n, int) or not isinstance(m, int):
        raise TypeError("multiplicacion_recursiva() expects two integers")
    if m < 0:
        raise ValueError(f"multiplicacion_recursiva() does not accept negative m, got {m}")
    # BASE CASE
    if m == 0:
        return 0
    # RECURSIVE CASE
    return multiplicacion_recursiva(n, m - 1) + n

# ============================================================
# 5. division_entera_recursiva(dividendo, divisor) — integer division
# ============================================================

def division_entera_recursiva(dividendo, divisor):
    # INPUT validation
    if divisor == 0:
        raise ZeroDivisionError("division_entera_recursiva() does not accept divisor = 0")
    if not isinstance(dividendo, int) or not isinstance(divisor, int):
        raise TypeError("division_entera_recursiva() expects two integers")
    # BASE CASE
    if dividendo - divisor < 0:
        return 0
    # RECURSIVE CASE
    return division_entera_recursiva(dividendo - divisor, divisor) + 1

# ============================================================
# 6. potencia_recursiva(base, exponente) — base ^ exponente
# ============================================================

def potencia_recursiva(base, exponente):
    # INPUT validation
    if not isinstance(exponente, int):
        raise TypeError(f"potencia_recursiva() expects an integer exponent, got {type(exponente).__name__}")
    if exponente < 0:
        raise ValueError(f"potencia_recursiva() does not accept negative exponents, got {exponente}")
    # BASE CASE
    if exponente == 0:
        return 1
    # RECURSIVE CASE
    return potencia_recursiva(base, exponente - 1) * base

# ============================================================
# 7. serie_collatz(n) — Collatz sequence
# ============================================================

def serie_collatz(n):
    # INPUT validation
    if not isinstance(n, int):
        raise TypeError(f"serie_collatz() expects an integer, got {type(n).__name__}")
    if n <= 0:
        raise ValueError(f"serie_collatz() requires a positive integer, got {n}")
    # BASE CASE
    if n == 1:
        print("END!")
        return 0
    # RECURSIVE CASE
    if n % 2 == 0:
        print(n // 2)
        return serie_collatz(n // 2)
    else:
        print(3 * n + 1)
        return serie_collatz(3 * n + 1)

# ============================================================
# 8. aplanar_json(diccionario, clave_padre, separador) — flatten nested dict
# ============================================================

def aplanar_json(diccionario, clave_padre='', separador='.'):
    # INPUT validation
    if not isinstance(diccionario, dict):
        raise TypeError(f"aplanar_json() expects a dict, got {type(diccionario).__name__}")
    elementos = []
    for key, value in diccionario.items():
        nueva_llave = f"{clave_padre}{separador}{key}" if clave_padre else key
        if isinstance(value, dict):
            # RECURSIVE CASE - nested dict
            elementos.extend(aplanar_json(value, nueva_llave, separador).items())
        else:
            # BASE CASE - plain value (including lists, None, bool, etc.)
            elementos.append((nueva_llave, value))
    return dict(elementos)

# ============================================================
# OUTPUT - Test all functions
# ============================================================

print("=" * 50)
print("  Recursive Functions Test")
print("=" * 50)

# --- recursiva ---
print("\n1. recursiva(5):")
try:
    result = recursiva(5)
    print(result)
except (TypeError, ValueError) as e:
    print(f"Error: {e}")

print("\n   recursiva(-3):")
try:
    result = recursiva(-3)
    print(result)
except (TypeError, ValueError) as e:
    print(f"Error: {e}")

# --- fibonacci ---
print("\n2. fibonacci(7):", end=" ")
try:
    print(fibonacci(7))
except (TypeError, ValueError) as e:
    print(f"Error: {e}")

print("   fibonacci(-1):", end=" ")
try:
    print(fibonacci(-1))
except (TypeError, ValueError) as e:
    print(f"Error: {e}")

# --- factorial ---
print("\n3. factorial(5):", end=" ")
try:
    print(factorial(5))
except (TypeError, ValueError) as e:
    print(f"Error: {e}")

print("   factorial(-2):", end=" ")
try:
    print(factorial(-2))
except (TypeError, ValueError) as e:
    print(f"Error: {e}")

# --- multiplicacion_recursiva ---
print("\n4. multiplicacion_recursiva(4, 3):", end=" ")
try:
    print(multiplicacion_recursiva(4, 3))
except (TypeError, ValueError) as e:
    print(f"Error: {e}")

print("   multiplicacion_recursiva(4, -3):", end=" ")
try:
    print(multiplicacion_recursiva(4, -3))
except (TypeError, ValueError) as e:
    print(f"Error: {e}")

# --- division_entera_recursiva ---
print("\n5. division_entera_recursiva(17, 5):", end=" ")
try:
    print(division_entera_recursiva(17, 5))
except (TypeError, ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")

print("   division_entera_recursiva(10, 0):", end=" ")
try:
    print(division_entera_recursiva(10, 0))
except (TypeError, ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")

# --- potencia_recursiva ---
print("\n6. potencia_recursiva(2, 5):", end=" ")
try:
    print(potencia_recursiva(2, 5))
except (TypeError, ValueError) as e:
    print(f"Error: {e}")

print("   potencia_recursiva(2, -2):", end=" ")
try:
    print(potencia_recursiva(2, -2))
except (TypeError, ValueError) as e:
    print(f"Error: {e}")

# --- serie_collatz ---
print("\n7. serie_collatz(6):")
try:
    serie_collatz(6)
except (TypeError, ValueError) as e:
    print(f"Error: {e}")

print("\n   serie_collatz(0):", end=" ")
try:
    serie_collatz(0)
except (TypeError, ValueError) as e:
    print(f"Error: {e}")

# --- aplanar_json ---
print("\n8. aplanar_json({'a': 1, 'b': {'c': 2}}):")
try:
    result = aplanar_json({"a": 1, "b": {"c": 2}})
    print(result)
except TypeError as e:
    print(f"Error: {e}")

print("\n   aplanar_json(['a', 'b', 'c']):", end=" ")
try:
    result = aplanar_json(["a", "b", "c"])
    print(result)
except TypeError as e:
    print(f"Error: {e}")

# --- json_prueba test ---
print("\n   aplanar_json(json_prueba):")
try:
    with open("json_prueba.json", "r") as f:
        content = f.read()
    # Extract the dict (it's assigned as a variable in the file)
    local_vars = {}
    exec(content, local_vars)
    json_prueba = local_vars["json_prueba"]
    result = aplanar_json(json_prueba)
    for k, v in result.items():
        print(f"  {k}: {v}")
except Exception as e:
    print(f"Error: {e}")

print("\n" + "=" * 50)
