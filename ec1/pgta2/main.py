from telefonia import movistar
from telefonia import claro
from telefonia import entel

main_operator = input("Ingrese operador principal: ")

# llamada 1
nro_tel_1 = input("Teléfono que llamó: ")
dur_call_1 = float(input("Duración llamada: "))
oper_call_1 = input("Operador que llamó: ")

if oper_call_1 == "movistar":
    costo = movistar.call(nro_tel_1, dur_call_1, oper_call_1)
    print("El costo de llamada a {} es: {}".format(nro_tel_1, costo))
elif oper_call_1 == "claro":
    costo = claro.call(nro_tel_1, dur_call_1, oper_call_1)
    print("El costo de llamada a {} es: {}".format(nro_tel_1, costo))
elif oper_call_1 == "entel":
    costo = entel.call(nro_tel_1, dur_call_1, oper_call_1)
    print("El costo de llamada a {} es: {}".format(nro_tel_1, costo))
else:
    print("Operador no encontrado")

# 0.5 min -> 1 min
# 9.2 min -> 10 min
# 5 min -> 5 min