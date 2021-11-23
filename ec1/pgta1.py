hours = int(input("Ingrese Horas: "))
minutes = int(input("Ingrese minutos: "))
duration = int(input("Ingrese duración en minutos: "))

min_aux = (minutes + duration % 60)
hour_aux = hours + (min_aux // 60) + ((duration - duration % 60) // 60)

hour_end = hour_aux % 24
min_end = min_aux % 60

print("El evento finaliza {}:{}".format(f"{hour_end:02d}", f"{min_end:02d}"))