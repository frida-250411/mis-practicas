def calcular_saldo_final(depositos, tasa_interes):
    if len(depositos) == 0:
        return 0.0

    saldo_anterior = calcular_saldo_final(depositos[:-1], tasa_interes)
    saldo_nuevo = (saldo_anterior + depositos[-1]) * (1 + tasa_interes)
    return saldo_nuevo

depositos = [1000, 2000, 1500]
tasa = 0.05

resultado = calcular_saldo_final(depositos, tasa)
print("Saldo final:", resultado)
