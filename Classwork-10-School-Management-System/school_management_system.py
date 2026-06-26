# Classwork 10 - Sistema de Gestión Escolar
# Armando Karin Molina Marrufo


# PROCESS - Define all system data before starting logic

# Users dictionary: username -> {password, rol, nombre}
usuarios = {
    'jperez':     {'password': '1234', 'rol': 'alumno',       'nombre': 'Juan Pérez'},
    'amartin':    {'password': '1234', 'rol': 'alumno',       'nombre': 'Ana Martín'},
    'clopez':     {'password': '1234', 'rol': 'alumno',       'nombre': 'Carlos López'},
    'lhernandez': {'password': '1234', 'rol': 'alumno',       'nombre': 'Lucía Hernández'},
    'pgarcia':    {'password': '1234', 'rol': 'alumno',       'nombre': 'Pedro García'},
    'mrojas':     {'password': '1234', 'rol': 'alumno',       'nombre': 'María Rojas'},
    'mlopez':     {'password': '1234', 'rol': 'maestro',      'nombre': 'María López'},
    'rgarcia':    {'password': '1234', 'rol': 'coordinador',  'nombre': 'Rosa García'},
}

# Subjects tuple - fixed set, never changes during execution
materias = ('Matemáticas', 'Programación', 'Inglés')

# Grades dictionary: student username -> {subject: grade}
# Keys must match student usernames in usuarios
calificaciones = {
    'jperez':     {'Matemáticas': 8.5, 'Programación': 9.0, 'Inglés': 7.5},
    'amartin':    {'Matemáticas': 9.0, 'Programación': 8.0, 'Inglés': 8.5},
    'clopez':     {'Matemáticas': 7.0, 'Programación': 7.5, 'Inglés': 6.5},
    'lhernandez': {'Matemáticas': 8.0, 'Programación': 9.5, 'Inglés': 9.0},
    'pgarcia':    {'Matemáticas': 6.5, 'Programación': 8.0, 'Inglés': 7.0},
    'mrojas':     {'Matemáticas': 9.5, 'Programación': 8.5, 'Inglés': 8.0},
}

# ============================================================
# LOGIN - Validate credentials with while loop (unlimited attempts)
# ============================================================

# PROCESS - Initialize login variables
logged_in = False
usuario_actual = ''
rol = ''
nombre = ''

while not logged_in:

    # INPUT - Ask for username
    usuario_actual = input('Usuario: ')

    # INPUT - Ask for password
    password = input('Contraseña: ')

    # PROCESS - Check if username exists and password matches
    if usuario_actual in usuarios and usuarios[usuario_actual]['password'] == password:
        logged_in = True
        rol = usuarios[usuario_actual]['rol']
        nombre = usuarios[usuario_actual]['nombre']
    else:
        # OUTPUT - Notify wrong credentials and loop again
        print('Usuario o contraseña incorrectos. Intente de nuevo.\n')

# OUTPUT - Show welcome message
print(f'\nBienvenido, {nombre} ({rol})\n')

# ============================================================
# ROLE BRANCHING - if/elif/else based on role
# ============================================================

if rol == 'alumno':

    # ----------------------------------------------------------
    # STUDENT MENU
    # ----------------------------------------------------------

    # OUTPUT - Print grade report header
    print(f'Boleta de {nombre}')
    print('-' * 30)

    # PROCESS - Initialize empty sets for approved and pending subjects
    aprobadas = set()

    # PROCESS - Loop over materias tuple to display and evaluate each grade
    for materia in materias:

        # PROCESS - Get grade for this subject from calificaciones
        calificacion = calificaciones[usuario_actual][materia]

        # OUTPUT - Print subject name and its grade
        print(f'{materia}: {calificacion}')

        # PROCESS - Check if grade meets the approval threshold (>= 8.0)
        if calificacion >= 8.0:
            aprobadas.add(materia)

    # PROCESS - Calculate pending subjects using set difference
    pendientes = set(materias) - aprobadas

    # OUTPUT - Print both sets
    print(f'\nMaterias aprobadas: {aprobadas}')
    print(f'Materias pendientes: {pendientes}')

elif rol == 'maestro':

    # ----------------------------------------------------------
    # TEACHER MENU
    # ----------------------------------------------------------

    # OUTPUT - Print list of all students
    print('Lista de alumnos:')
    print('-' * 30)

    # PROCESS - Loop over usuarios and filter by role alumno
    for user in usuarios:
        if usuarios[user]['rol'] == 'alumno':
            # OUTPUT - Print username and full name
            print(f'{user} - {usuarios[user]["nombre"]}')

    print()

    # INPUT - Ask which student to grade (by username)
    alumno_sel = input('Alumno (username): ')

    # INPUT - Ask which subject to update
    materia_sel = input('Materia: ')

    # INPUT - Ask for the new grade value
    nueva_cal = float(input('Nueva calificación: '))

    # PROCESS - Overwrite the grade in calificaciones dictionary
    calificaciones[alumno_sel][materia_sel] = nueva_cal

    # OUTPUT - Confirm the update
    print('Calificación actualizada.')

elif rol == 'coordinador':

    # ----------------------------------------------------------
    # COORDINATOR MENU (read only)
    # ----------------------------------------------------------

    # OUTPUT - Print list of teachers
    print('=== MAESTROS ===')

    # PROCESS - Loop over usuarios and filter by role maestro
    for user in usuarios:
        if usuarios[user]['rol'] == 'maestro':
            # OUTPUT - Print teacher info
            print(f'{user} - {usuarios[user]["nombre"]}')

    print()

    # OUTPUT - Print list of subjects from materias tuple
    print('=== MATERIAS ===')

    # PROCESS - Loop over materias tuple
    for materia in materias:
        # OUTPUT - Print each subject name
        print(materia)

    print()

    # OUTPUT - Print all students and their grades
    print('=== ALUMNOS Y CALIFICACIONES ===')

    # PROCESS - Loop over calificaciones (one entry per student)
    for alumno in calificaciones:

        # OUTPUT - Print student name and username
        print(f'\n{usuarios[alumno]["nombre"]} ({alumno}):')

        # PROCESS - Loop over materias to print every grade
        for materia in materias:
            # OUTPUT - Print subject and grade indented
            print(f'  {materia}: {calificaciones[alumno][materia]}')
