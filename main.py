import sys
import math

ectype = sys.argv.pop(1) # tipo de ecuacion

if ectype == "basico":
    num1 = sys.argv[1]
    num1 = float(num1)
    operat = sys.argv[2]
    num2 = sys.argv[3]
    num2 = float(num2)
    result = None

    if operat == "+": # Si es una suma
        result = num1 + num2
    elif operat == "-": # Si es una resta
        result = num1 - num2
    elif operat == "x" or operat == ".": # Si es una multiplicacion
        result = num1 * num2
    elif operat == "/" or operat == ":": # Si es una division
        if num2 == 0:
            print("No se puede dividir por 0")
            sys.exit(1)
        else:
            result = num1 / num2

    if result is not None:
        print(f"{num1} {operat} {num2} = \n{result}")
    else:
        print("SYNTAX ERROR")
        sys.exit(1)


elif ectype == "pitagoras":
    argv = sys.argv
    ec = argv[1]
    a = float(argv[2])
    b = float(argv[3])

    if ec == "c": # Si el numero desconocido es un cateto
        h = max(a,b)
        c = min(a,b)

        if h <= c:
            print("ERROR: La hipotenusa no puede ser igual o menor a ninguno de los catetos")
            sys.exit(1)

        x = math.sqrt((h**2)-(c**2))

        print(
            "x = cateto desconocido, h = hipotenusa y c = cateto conocido\n" +
            "x² = h² - c²\n" +
            f"x² = {h}² - {c}²\n" +
            f"x² = {h**2} - {c**2}\n" +
            f"x² = {(h**2)-(c**2)}\n" +
            f"x = ²√{(h**2)-(c**2)}\n" +
            f"x = {x}\nEl cateto desconocido es {x}"
        )
    elif ec == "h": # Si el numero desconocido es la hipotenusa
        x = math.sqrt((a**2)+(b**2))

        print(
            "x = la hipotenusa desconocida, c1 = cateto 1 y c2 = cateto 2\n" +
            "x² = c1² + c2²\n" +
            f"x² = {a}² + {b}²\n" +
            f"x² = {a**2} + {b**2}\n" +
            f"x² = {(a**2)+(b**2)}\n" +
            f"x = ²√{(a**2)+(b**2)}\n" +
            f"x = {x}\nLa hipotenusa desconocida es {x}"
        )
    else: # Si no se especifico
        print("ERROR: No se especifico si el numero desconocido es un (c)ateto o la (h)ipotenusa")
        sys.exit(1)

elif ectype == "eval":
    argv = sys.argv
    try:
        result = eval(argv[1])
        print(f"{argv[1]} =\n{result}")
    except Exception as e:
        print(f"Error intentando calcular usando eval: {e}")
        sys.exit(1)