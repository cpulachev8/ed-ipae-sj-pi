from Model import Alumno, Curso

est_datos = Curso("ED-0001", "Estructura de Datos")
mod_datos = Curso("MD-0002", "Modelamiento de Datos")
alumno1 = Alumno("SIST-0001", "Claudio Pérez")
alumno1.inscribir_curso(est_datos)
alumno1.inscribir_curso(mod_datos)
alumno1.ingresar_notas()
alumno1.calcular_promedio_cursos()
alumno1.listar_cursos()