# INPUT
# Read grid dimensions, iteration limit, and complex-plane boundaries
# from config.txt


class ConfigError(Exception):
    pass


config = {}

try:
    file = open("config.txt", "r")
except FileNotFoundError:
    print("No se encontro el archivo config.txt")
    raise SystemExit

try:
    for line in file:
        line = line.strip()
        if line == "":
            continue
        try:
            parameter, value = line.split("=")
        except ValueError:
            raise ConfigError("El archivo de configuracion esta mal formado")
        config[parameter] = float(value) if "." in value else int(value)
except ConfigError as error:
    file.close()
    print(error)
    raise SystemExit
else:
    file.close()

try:
    width, height, max_iter = config["ancho"], config["alto"], config["max_iter"]
    for clave in ("real_min", "real_max", "imag_min", "imag_max"):
        if clave not in config:
            raise KeyError(clave)
except KeyError as error:
    print(f"Falta el parametro {error} en config.txt")
    raise SystemExit
except ConfigError as error:
    print(error)
    raise SystemExit

try:
    output = open("mandelbrot.csv", "w")
    output.write("row,column,iterations\n")

    # PROCESS
    # For every point in the grid:
    #   1. map the pixel position to a point c on the complex plane
    #   2. apply the escape-time rule (z = z*z + c) until it escapes
    #      or the iteration limit is reached
    #   3. write the resulting iteration count to the output file

    for row in range(height):
        for column in range(width):
            real = config["real_min"] + (column / width) * (config["real_max"] - config["real_min"])
            imag = config["imag_min"] + (row / height) * (config["imag_max"] - config["imag_min"])
            c = complex(real, imag)

            z = 0 + 0j
            iterations = 0

            while (abs(z) <= 2) and (iterations < max_iter):
                z = z * z + c
                iterations += 1

            # OUTPUT
            # Save one row per grid point: row, column, iterations
            output.write(f"{row},{column},{iterations}\n")

    output.close()

except TypeError:
    print("Los parametros 'ancho' y 'alto' deben ser numeros enteros")
