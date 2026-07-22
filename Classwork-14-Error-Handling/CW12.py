from PIL import Image

# INPUT
# Read config.txt (grid size, max_iter) and mandelbrot.csv (per-pixel data)

config = {}

try:
    file = open("config.txt", "r")
except FileNotFoundError:
    print("No se encontro el archivo config.txt")
    raise SystemExit

lines = file.readlines()
file.close()

for line in lines:
    line = line.strip()
    if line == "":
        continue
    parameter, value = line.strip().split("=")
    config[parameter] = float(value) if "." in value else int(value)

try:
    archivo = open("mandelbrot.csv", "r")
except FileNotFoundError:
    print("No se encontro el archivo mandelbrot.csv")
    raise SystemExit

lineas = archivo.readlines()
archivo.close()

# remove header row
lineas.pop(0)

max_iter = config["max_iter"]
ancho, alto = config["ancho"], config["alto"]

# PROCESS
# For every saved data point, turn the iteration count into a
# grayscale brightness value (0-255) and paint that pixel

img = Image.new("L", (ancho, alto))

for linea in lineas:
    linea = linea.strip()
    if linea == "":
        continue

    try:
        row, column, iterations = linea.split(",")
        row = int(row)
        column = int(column)
        iterations = int(iterations)
    except ValueError:
        print("El archivo mandelbrot.csv esta mal formado")
        raise SystemExit

    if iterations == max_iter:
        brillo = 0
    else:
        brillo = int((iterations / max_iter) * 255)

    try:
        img.putpixel((column, row), brillo)
    except IndexError:
        print("El csv no es consistente con el ancho/alto del config.txt")
        raise SystemExit

# OUTPUT
img.save("mandelbrot.png")
print("DONE")