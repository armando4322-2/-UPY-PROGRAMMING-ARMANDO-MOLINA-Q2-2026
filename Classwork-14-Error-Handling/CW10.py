# INPUT
# Ask for username and password, retry until correct

usuarios = {
    'jperez': {'password': '1234', 'rol': 'student', 'nombre': 'Juan Pérez'},
    'amartin': {'password': '1234', 'rol': 'student', 'nombre': 'Ana Martin'},
    'ltrochez': {'password': '1234', 'rol': 'student', 'nombre': 'Luisa Trochez'},
    'adiaz': {'password': '1234', 'rol': 'student', 'nombre': 'Abraham Díaz'},
    'sescamilla': {'password': '1234', 'rol': 'student', 'nombre': 'Stephan Escamilla'},
    'jrojas': {'password': '1234', 'rol': 'student', 'nombre': 'Jesse Rojas'},
    'jpedrozo': {'password': '1234', 'rol': 'professor', 'nombre': 'Jorge Pedrozo'},
    'dgamboa': {'password': '1234', 'rol': 'coordinator', 'nombre': 'Didier Gamboa'},
}

materias = ('Mathematics', 'Programming', 'English II', 'Social-Emotional Skills',
            'Computer and Server Architecture', 'Calculus')

calificaciones = {
    'jperez': {'Mathematics': 9.0, 'Programming': 9.2, 'English II': 8.5,
               'Social-Emotional Skills': 7.0, 'Computer and Server Architecture': 6.8, 'Calculus': 7.5},
    'amartin': {'Mathematics': 9.0, 'Programming': 8.0, 'English II': 7.5,
                'Social-Emotional Skills': 9.0, 'Computer and Server Architecture': 6.0, 'Calculus': 9.5},
    'ltrochez': {'Mathematics': 10, 'Programming': 8.9, 'English II': 8.9,
                 'Social-Emotional Skills': 9.0, 'Computer and Server Architecture': 9.0, 'Calculus': 8.7},
    'adiaz': {'Mathematics': 9.0, 'Programming': 9.7, 'English II': 9.5,
              'Social-Emotional Skills': 9.0, 'Computer and Server Architecture': 9.0, 'Calculus': 9.5},
    'sescamilla': {'Mathematics': 9.0, 'Programming': 8.7, 'English II': 8.5,
                   'Social-Emotional Skills': 7.0, 'Computer and Server Architecture': 9.6, 'Calculus': 8.5},
    'jrojas': {'Mathematics': 9.0, 'Programming': 8.7, 'English II': 8.5,
               'Social-Emotional Skills': 6.0, 'Computer and Server Architecture': 8.0, 'Calculus': 9.5},
}

# LOGIN MENU
acceso = False
while not acceso:
    usuario = input('Usuario: ')
    contraseña = input('Contraseña: ')

    if usuario in usuarios and usuarios[usuario]['password'] == contraseña:
        acceso = True
    else:
        print('Wrong user/password!\n')

rol = usuarios[usuario]['rol']
nombre = usuarios[usuario]['nombre']
print(f"\nBienvenid@!, {nombre} ({rol})\n")

# PROCESS + OUTPUT
if rol == 'student':
    print('School Report')

    aprobadas = set()
    for materia in materias:
        calif = calificaciones[usuario][materia]
        print(f'{materia}: {calif}')
        if calif >= 7.0:
            aprobadas.add(materia)

    pendientes = set(materias) - aprobadas

    print('')
    print(f'Approved: {aprobadas if aprobadas else "None"}')
    print(f'Pending: {pendientes if pendientes else "None"}')

elif rol == 'professor':
    print('Students:')
    for clave_usuario in usuarios:
        if usuarios[clave_usuario]['rol'] == 'student':
            print(f"- {clave_usuario}: {usuarios[clave_usuario]['nombre']}")

    print('\nSubjects:')
    for materia in materias:
        print(f'- {materia}')

    while True:
        alumno = input('\nStudent (username): ')

        try:
            if alumno not in calificaciones:
                raise KeyError(alumno)

            materia = input('Subject: ')

            if materia not in materias:
                raise KeyError(materia)

            nuevo_valor = input('New grade: ')
            valor_anterior = calificaciones[alumno][materia]

            print(f"\nDo you confirm (yes/no)?\n{materia}: {valor_anterior} ==> {nuevo_valor}")
            confirmar = input().strip().lower()

        except KeyError as error:
            if str(error).strip("'") == alumno:
                print('Ese usuario no existe')
            else:
                print('Esa materia no existe')
            break

        if confirmar == 'yes':
            calificaciones[alumno][materia] = float(nuevo_valor)
            print('Grade updated.')
            otra = input('\nGrade another student? (yes/no): ').strip().lower()
            if otra != 'yes':
                break
        elif confirmar == 'no':
            print('Grade not updated.')
            otra = input('\nGrade another student? (yes/no): ').strip().lower()
            if otra != 'yes':
                break
        else:
            break

elif rol == 'coordinator':
    print('Professors:')
    for clave_usuario in usuarios:
        if usuarios[clave_usuario]['rol'] == 'professor':
            print(f"- {clave_usuario}: {usuarios[clave_usuario]['nombre']}")

    print('\nStudents:')
    for clave_usuario in usuarios:
        if usuarios[clave_usuario]['rol'] == 'student':
            print(f"- {clave_usuario}: {usuarios[clave_usuario]['nombre']}")

    print('\nRecords:')
    for alumno in calificaciones:
        print(f"\n{usuarios[alumno]['nombre']} ({alumno}):")
        for materia in materias:
            print(f'  {materia}: {calificaciones[alumno][materia]}')
