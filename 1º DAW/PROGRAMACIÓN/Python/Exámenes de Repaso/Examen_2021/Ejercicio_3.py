alumnos = [
    {
        "nombre": "Enrique",
        "apellidos": "García, Migueza",
        "dni": "12345678K",
        "email": "egarciamigueza@safareyes.es"
    },
    {
        "nombre": "Paloma",
        "apellidos": "Machado, López",
        "dni": "12345678Z",
        "email": "pmachadolopez@hotmail.es"
    },
    {
        "nombre": "Antonio",
        "apellidos": "Romero, Domínguez",
        "dni": "12345678A",
        "email": "aromerodominguez@safareyes.es"
    }
]

#a) Lista de alumnos cuyo dominio de email pertenece al centro
def alumnos_por_dominio(lista_alumnos, dominio):
    return [alumno for alumno in lista_alumnos if alumno['email'].split('@')[1] == dominio]

resultado_a = alumnos_por_dominio(alumnos, "safareyes.es")
print(resultado_a)

#b) Primer alumno de la lista por orden alfabético del primer apellido
def primer_alumno_por_apellido(lista_alumnos):
    return sorted(lista_alumnos, key=lambda x: x['apellidos'].split(',')[0])[0]

resultado_b = primer_alumno_por_apellido(alumnos)
print(resultado_b)

#c) Primer alumno de la lista por orden alfabético de la letra del DNI
def primer_alumno_por_dni(lista_alumnos):
    return sorted(lista_alumnos, key=lambda x: x['dni'][-1])[0]

resultado_c = primer_alumno_por_dni(alumnos)
print(resultado_c)
