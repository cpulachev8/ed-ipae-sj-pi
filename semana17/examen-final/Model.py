
class Notas:

    def __init__(self, nota, peso) -> None:
        self.nota = nota
        self.peso = peso

    def valida_nota(self) -> bool:
        return self.nota >= 0 and self.nota <= 20

class Curso:

    def __init__(self, cod_curso, nombre) -> None:
        self.cod_curso = cod_curso
        self.nombre = nombre
        self.estado = ""
        self.promedio = 0.0
        self.notas = []
        self.inicializar_curso()
    
    def inicializar_curso(self):
        print("*** CONFIGURANDO CURSO {}".format(self.nombre))
        for i in range(4):
            nota = Notas(0, float(input("Ingrese peso Nota {}: ".format(i+1))) / 100)
            self.agregar_nota(nota)

    def print(self):
        print("Curso: {} - {} - {} - {}".format(self.cod_curso, self.nombre, self.promedio, self.estado))

    def agregar_nota(self, nota: Notas):
        if len(self.notas) < 4 and nota.valida_nota():
            self.notas.append(nota)
        else:
            print("No se permite ingresar más de 4 notas o Nota es inválida")

        if len(self.notas) == 4:
            t_peso = 0.0
            for n in self.notas:
                t_peso += n.peso
            
            if t_peso != 1:
                print("El peso de las notas es incorrecto")

    def calcular_estado(self):
        promedio = 0.0
        for n in self.notas:
            promedio += n.nota * n.peso
        self.promedio = promedio
        if promedio >= 13:
            self.estado = "APROBADO"
        else:
            self.estado = "DESAPROBADO"

class Alumno:

    def __init__(self, cod_alumno, nombre) -> None:
        self.cod_alumno = cod_alumno
        self.nombre = nombre
        self.cursos = []
    
    def inscribir_curso(self, curso: Curso):
        self.cursos.append(curso)

    def listar_cursos(self):
        for c in self.cursos:
            c.print()

    def ingresar_notas(self):
        for c in self.cursos:
            print("*** NOTAS DE {}".format(c.nombre))
            for i in range(4):
                c.notas[i].nota = float(input("Ingrese Nota: "))

    def calcular_promedio_cursos(self):
        for c in self.cursos:
            c.calcular_estado()
