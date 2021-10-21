import persona
import datos_encomienda

persona_envia = persona.ingreso()
encomienda = datos_encomienda.ingreso()
persona_recibe = persona.ingreso()

#print("La persona %s con DNI %s está enviando %s a %s con DNI %s"
    #%(persona_envia["nombre"], persona_envia["dni"], encomienda, persona_recibe["nombre"], persona_recibe["dni"]))

print("%s está enviando %s a %s"
    %(persona.ver_datos(persona_envia["nombre"], persona_envia["dni"]),
    encomienda,
    persona.ver_datos(persona_recibe["nombre"], persona_recibe["dni"])))

#registrar datos (100 lineas)

#imprimir ticket (80 lineas)
#def imprimir(nombre, dni, destino, origen, costo):
    # print("Se entregó satisfactoriamente")

#cobrar ticket (250 lineas)

#cambiar estado ticket (50 lineas)

#recojo encomienda (300 lineas)

#impresión de comprobante de encomienda (80 lineas)

#reporte de las encomiendas del día (400 lineas)
