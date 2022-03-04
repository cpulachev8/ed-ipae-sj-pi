import datetime

class Country:

    def __init__(self, name, time_zone, current_date: datetime) -> None:
        self.name = name
        self.time_zone = time_zone
        self.current_date = current_date

    def print(self) -> None:
        print("======== Datos del País ========")
        print("Nombre: {}".format(self.name))
        print("Zona Horaria: {}".format(self.time_zone))
        print("Fecha Actual: {}".format(self.current_date.strftime("%d/%m/%Y %I:%M %p")))

    def calculate_current_date(self, sign_basic_tz, number_hours_basic_tz, current_date_basic) -> None:
        # Asignando fecha del país base al país a calcular
        self.current_date = current_date_basic

        # Calculando la fecha actual del país con GMT-0
        if sign_basic_tz == "+":
            self.current_date = self.current_date - datetime.timedelta(hours=number_hours_basic_tz)
        elif sign_basic_tz == "-":
            self.current_date = self.current_date + datetime.timedelta(hours=number_hours_basic_tz)
        
        # Calculando la fecha actual del país con su propio GMT
        sign = self.get_sign_time_zone()
        number_hours = self.get_number_hours_time_zone()
        if sign == "-":
            self.current_date = self.current_date - datetime.timedelta(hours=number_hours)
        elif sign == "+":
            self.current_date = self.current_date + datetime.timedelta(hours=number_hours)
        

    def get_sign_time_zone(self) -> str:
        return self.time_zone[3:4]

    def get_number_hours_time_zone(self) -> int:
        return int(self.time_zone[4::])