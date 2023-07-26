
diametro1=0.07
area1 = (3.14159 / 4) * (diametro1 ** 2)
caudal=0.1
velocidad_1 = caudal / area1
velocidad_2 = 8.84

print(velocidad_1)

a=(860*0.1*9.81*(29.6+((1.05*((velocidad_2**2)-(velocidad_1**2)))/(2*9.81)))/1000)/22.5
print(a)