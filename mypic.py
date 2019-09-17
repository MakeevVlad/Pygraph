from graph import *
import numpy as np

def ellipsis(a, b, x0, y0):
    p = ([])
    for x in np.arange(-np.sqrt(a) + x0, np.sqrt(a) + x0, 1):
        p.append([x, np.sqrt(b*(1-(x-x0)**2/a))+y0])
    for x in np.arange(np.sqrt(a) + x0, -np.sqrt(a) + x0, -1):
        p.append([x, -np.sqrt(b*(1-(x-x0)**2/a))+y0])
    polygon(p)

windowSize(700, 600)
canvasSize(700, 600)
penColor('grey')
brushColor('grey')
ellipsis(10000, 1000, 600, 100)

#background
brushColor('#99999C')
penColor('#99999C')
rectangle(0, 250, 700, 0)

brushColor('#000000')
penColor('#000000')
rectangle(0, 700, 700, 250)

#hounted house
brushColor('#000000')
penColor('#000000')
polygon([[25, 160], [75, 130], [275, 130],[325, 160]])

brushColor('#552200')
penColor('#552200')
rectangle(50, 500, 300, 160)

#Top windws
brushColor('#554433')
penColor('#554433')
for i in range(4):
    rectangle(60 + i*65, 300, 90+ i*65, 160)

##Bottom windws
brushColor('#554433')
penColor('#554433')
for i in range(2):
    rectangle(70 + i*85, 450, 110+ i*85, 400)
brushColor('#FFCC33')
penColor('#FFCC33')
rectangle(70 + 2*85, 450, 110+ 2*85, 400)

#Balcony
brushColor('#110000')
penColor('#110000')
rectangle(25, 315, 320, 300)




#Sky
##moon
brushColor('#EEEEEE')
penColor('#EEEEEE')
ellipsis(4000, 4000, 600, 50)

##clouds
brushColor('#444444')
penColor('#444444')
ellipsis(30000, 550, 350, 80)

brushColor('#888888')
penColor('#888888')
ellipsis(20000, 500, 510, 60)

brushColor('#333333')
penColor('#333333')
ellipsis(30000, 400, 700, 120)

run()
