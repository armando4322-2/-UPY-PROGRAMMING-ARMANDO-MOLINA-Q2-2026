# Classwork 07 - UTFSM Verification Digit
# Armando Karin Molina Marrufo

# INPUT - Ask user for the UTFSM student ID (without dash or check digit)
try:
    rol = input("Enter the UTFSM student ID (without dash or check digit): ")

    if len(rol) == 0:
        raise ValueError("Input cannot be empty.")

    # PROCESS - Reverse the ID and calculate verification digit using UTFSM algorithm
    rol_invertido = rol[::-1]
    secuencia = [2, 3, 4, 5, 6, 7]
    suma = 0

    for i, digito in enumerate(rol_invertido):
        multiplicador = secuencia[i % len(secuencia)]
        suma += int(digito) * multiplicador

    modulo = suma % 11
    digito_verificador = 11 - modulo

    # OUTPUT - Print full calculation breakdown and result
    print(f"\nReversed ID:   {rol_invertido}")
    print(f"Total sum:     {suma}")
    print(f"Sum % 11:      {modulo}")
    print(f"11 - {modulo}:        {digito_verificador}")
    print(f"\nFull ID: {rol}-{digito_verificador}")

except ValueError as e:
    print(f"Error: {e} - The student ID must contain only numeric characters.")
