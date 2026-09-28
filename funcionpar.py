def calcular_area_triangulo(base,altura):
    area=(base*altura)/2
    return area
resultado=calcular_area_triangulo(10,5)
print(f"El area del triangulo es: {resultado}")

def saludar_personal(nombre,edad):
    print(f"Hola{nombre},tienes{edad}años")
saludar_personal("Carlos",20)