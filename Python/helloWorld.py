import pyfiglet

print(pyfiglet.FigletFont.getFonts())

a = pyfiglet.Figlet(font='big')
print(a.renderText('Hello World!'))
b = pyfiglet.Figlet(font='isometric2')
c = pyfiglet.Figlet(font='isometric3')
d = pyfiglet.Figlet(font='isometric4')

i = 0
while (True):
    if( i % 4 == 0):
        print(a.renderText('Hello World!'))
    elif(i % 4 == 1):
        print(b.renderText('Hello World!'))
    elif (i % 4 == 2):
        print(c.renderText('Hello World!'))
    else:
        print(d.renderText('Hello World!'))
    i += 1