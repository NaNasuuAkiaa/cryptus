from PIL import Image
import sys
import math

argumentos = sys.argv

listadechars = 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáÁéÉíÍóÓúÚ1234567890.,:;- _{}[]!|"@·#$~%€&¬/()=?¿\'\\'

if str(argumentos) != "['main.py', 'enc']" and str(argumentos) != "['main.py', 'dec']":
    print("no valid arguments (enc/dec)")
elif argumentos[1] == "dec":
    imagen = Image.open("image.png")
    codigofinal = ""
    x, y = imagen.size
    for i in range(x):
        for j in range(y):
            r, g, b = imagen.getpixel((i, j))
            r = int(int(r)/3)
            g = int(int(g)/3)
            b = int(int(b)/3)
            if r == 85 or g == 85 or b == 85:
                print(codigofinal)
                exit()
            codigofinal = codigofinal + listadechars[r]+listadechars[g]+listadechars[b]
    print(codigofinal)
elif argumentos[1] == "enc":
    fraseaencojer = input("frase --> ")
    if math.sqrt(len(fraseaencojer)/3) <= 25:
        tipo = 1
        imagen = Image.new("RGB", (25, 25), (255,255,255))
    elif math.sqrt(len(fraseaencojer)/3) <= 50:
        tipo = 2
        imagen = Image.new("RGB", (50, 50), (255,255,255))
    elif math.sqrt(len(fraseaencojer)/3) <= 75:
        tipo = 3
        imagen = Image.new("RGB", (75, 75), (255,255,255))

    lencount = 0
    x, y = imagen.size
    for i in range(x):
        for j in range(y):
            if lencount == len(fraseaencojer):
                imagen.save("image.png")
                exit()
            r = int(listadechars.find(fraseaencojer[int(lencount)]))*3
            lencount+=1
            if lencount == len(fraseaencojer):
                imagen.save("image.png")
                exit()
            g = int(listadechars.find(fraseaencojer[int(lencount)]))*3
            lencount+=1
            if lencount == len(fraseaencojer):
                imagen.save("image.png")
                exit()
            b = int(listadechars.find(fraseaencojer[int(lencount)]))*3
            lencount+=1
            imagen.putpixel((i, j), (r, g, b))
    imagen.save("imagen.png")
    print(str(tipo))