# Classwork 08 - Numerical Integration
# Armando Karin Molina Marrufo

import math

# INPUT - Ask user for interval, function, and integration method
try:
    a_input = input("Write the left endpoint of the interval: ")
    a = float(eval(a_input.replace("pi", "math.pi")))

    b_input = input("Write the right endpoint of the interval: ")
    b = float(eval(b_input.replace("pi", "math.pi")))

    if a == b:
        raise ZeroDivisionError("Left and right endpoints cannot be equal.")

    f_x = input("Write the function to integrate: ")
    method = input("Select the Integration Method (LRM/RRM/MPM/TRM): ")

    if method not in ("LRM", "RRM", "MPM", "TRM"):
        raise ValueError(f"'{method}' is not a valid method. Choose LRM, RRM, MPM, or TRM.")

    # PROCESS - Calculate area using the selected numerical method
    area = 0.0
    n = 1000
    h = (b - a) / n
    shift = 0
    constant = 0

    if method == "RRM":
        shift = 1
    elif method == "MPM":
        constant = h / 2

    if method == "TRM":
        f_x0 = eval(f_x, {"math": math, "x": a})
        f_x1 = eval(f_x, {"math": math, "x": b})
        sum_inter = 0.0
        for i in range(1, n):
            xi = a + i * h
            sum_inter += eval(f_x, {"math": math, "x": xi})
        area = (h / 2) * (f_x0 + 2 * sum_inter + f_x1)
    else:
        for i in range(0 + shift, n + shift):
            xi = a + i * h + constant
            height = eval(f_x, {"math": math, "x": xi})
            area += height * h

    # OUTPUT - Print the integration result
    print(f"The integration of {f_x} is {area:.2f}")

except ValueError as e:
    print(f"Error: {e}")
except SyntaxError:
    print("Error: Invalid function expression. Use valid Python math syntax (e.g. math.sin(x)).")
except NameError:
    print("Error: Unknown variable in function. Use 'x' as the variable.")
except ZeroDivisionError as e:
    print(f"Error: {e}")
