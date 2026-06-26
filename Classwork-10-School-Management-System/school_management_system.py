# Classwork 10 - School Management System
# Armando Karin Molina Marrufo

# PROCESS - Define all system data before starting logic

# Users dictionary: username -> {password, role, name}
users = {
    'jperez':   {'password': '1234', 'role': 'student',     'name': 'Juan Pérez'},
    'dromo':    {'password': '1234', 'role': 'student',     'name': 'Daniela Romo'},
    'mjuarez':  {'password': '1234', 'role': 'student',     'name': 'Mauricio Juárez'},
    'mlopez':   {'password': '1234', 'role': 'student',     'name': 'María López'},
    'euc':      {'password': '1234', 'role': 'student',     'name': 'Ernesto Uc'},
    'cbalam':   {'password': '1234', 'role': 'student',     'name': 'Carlos Balam'},
    'jpedrozo': {'password': '1234', 'role': 'professor',   'name': 'Jorge Pedrozo'},
    'dgamboa':  {'password': '1234', 'role': 'coordinator', 'name': 'Didier Gamboa'},
}

# Subjects tuple - fixed set, never changes during execution
subjects = (
    'Discrete Mathematics',
    'Programming',
    'English II',
    'Differential Calculus',
    'Probability and Statistics',
    'Computer and Server Architecture',
    'Socio-Emotional Skills and Conflict Management',
)

# Grades dictionary: student username -> {subject: grade}
grades = {
    'jperez':  {
        'Discrete Mathematics': 8.5, 'Programming': 9.2, 'English II': 9.0,
        'Differential Calculus': 7.8, 'Probability and Statistics': 8.3,
        'Computer and Server Architecture': 6.8,
        'Socio-Emotional Skills and Conflict Management': 9.5,
    },
    'dromo':   {
        'Discrete Mathematics': 9.0, 'Programming': 6.7, 'English II': 9.4,
        'Differential Calculus': 6.2, 'Probability and Statistics': 9.1,
        'Computer and Server Architecture': 6.5,
        'Socio-Emotional Skills and Conflict Management': 9.8,
    },
    'mjuarez': {
        'Discrete Mathematics': 7.5, 'Programming': 8.0, 'English II': 8.5,
        'Differential Calculus': 7.0, 'Probability and Statistics': 7.8,
        'Computer and Server Architecture': 6.2,
        'Socio-Emotional Skills and Conflict Management': 8.9,
    },
    'mlopez':  {
        'Discrete Mathematics': 9.5, 'Programming': 9.8, 'English II': 9.2,
        'Differential Calculus': 9.0, 'Probability and Statistics': 9.6,
        'Computer and Server Architecture': 9.4,
        'Socio-Emotional Skills and Conflict Management': 10.0,
    },
    'euc':     {
        'Discrete Mathematics': 8.2, 'Programming': 6.9, 'English II': 8.8,
        'Differential Calculus': 6.0, 'Probability and Statistics': 6.4,
        'Computer and Server Architecture': 8.1,
        'Socio-Emotional Skills and Conflict Management': 9.0,
    },
    'cbalam':  {
        'Discrete Mathematics': 8.8, 'Programming': 9.0, 'English II': 8.5,
        'Differential Calculus': 6.6, 'Probability and Statistics': 8.9,
        'Computer and Server Architecture': 8.7,
        'Socio-Emotional Skills and Conflict Management': 9.2,
    },
}

# ============================================================
# LOGIN - Validate credentials with while loop (unlimited attempts)
# ============================================================

# PROCESS - Initialize login variables
logged_in = False
current_user = ''
role = ''
name = ''

while not logged_in:

    # INPUT - Ask for username and password
    current_user = input('User: ')
    password = input('Password: ')

    # PROCESS - Check if username exists and password matches
    if current_user in users and users[current_user]['password'] == password:
        logged_in = True
        role = users[current_user]['role']
        name = users[current_user]['name']
    else:
        # OUTPUT - Notify wrong credentials and loop again
        print('Wrong username or password. Try again.\n')

# OUTPUT - Show welcome message
print(f'\nWelcome, {name} ({role})\n')

# ============================================================
# ROLE BRANCHING - if/elif/else based on role
# ============================================================

if role == 'student':

    # ----------------------------------------------------------
    # STUDENT MENU
    # ----------------------------------------------------------

    # OUTPUT - Print grade report header
    print('=' * 30)
    print(' School Report')
    print('=' * 30)

    # PROCESS - Initialize empty set for approved subjects
    approved = set()

    # PROCESS - Loop over subjects tuple to display and evaluate each grade
    for subject in subjects:

        # PROCESS - Get grade for this subject from grades
        grade = grades[current_user][subject]

        # OUTPUT - Print subject name and its grade aligned
        print(f'{subject:<35}: {grade}')

        # PROCESS - Check if grade meets the approval threshold (>= 8.0)
        if grade >= 8.0:
            approved.add(subject)

    # PROCESS - Calculate pending subjects using set difference
    pending = set(subjects) - approved

    # OUTPUT - Print both sets
    print(f'\nApproved: {approved}')
    print(f'Pending : {pending}')

elif role == 'professor':

    # ----------------------------------------------------------
    # PROFESSOR MENU
    # ----------------------------------------------------------

    # OUTPUT - Print list of all students
    print('=' * 30)
    print(' Students')
    print('=' * 30)

    # PROCESS - Loop over users and filter by role student
    for user in users:
        if users[user]['role'] == 'student':
            print(f'User: {user:<10} | Student: {users[user]["name"]}')

    print()

    # PROCESS - Loop to grade multiple students (exit by entering invalid username)
    while True:

        # INPUT - Ask which student to grade
        selected_student = input('Student to grade (username): ')

        # PROCESS - If username is not a valid student, exit the loop
        if selected_student not in grades:
            break

        # OUTPUT - Show list of subjects
        print()
        for subject in subjects:
            print(subject)
        print()

        # INPUT - Ask which subject and new grade
        selected_subject = input('Subject to grade: ')
        new_grade = float(input('New grade: '))

        # OUTPUT - Show old => new grade and ask for confirmation
        old_grade = grades[selected_student][selected_subject]
        print(f'\nDo you confirm (yes/no)?')
        print(f'{selected_subject}: {old_grade} ==> {new_grade}')
        confirmation = input()

        # PROCESS - Update grade only if confirmed
        if confirmation == 'yes':
            grades[selected_student][selected_subject] = new_grade
            print('Grade updated!')
            print(grades[selected_student])
        else:
            print('Write other thing to exit')

        print()

elif role == 'coordinator':

    # ----------------------------------------------------------
    # COORDINATOR MENU (read only)
    # ----------------------------------------------------------

    # OUTPUT - Print list of professors
    print('=' * 30)
    print(' Professors')
    print('=' * 30)

    # PROCESS - Loop over users and filter by role professor
    for user in users:
        if users[user]['role'] == 'professor':
            print(f'User: {user} | Professor: {users[user]["name"]}')

    print()

    # OUTPUT - Print list of students
    print('=' * 30)
    print(' Students')
    print('=' * 30)

    # PROCESS - Loop over users and filter by role student
    for user in users:
        if users[user]['role'] == 'student':
            print(f'User: {user:<10} | Student: {users[user]["name"]}')

    print()

    # OUTPUT - Print full grades table
    print('=' * 30)
    print(' Records')
    print('=' * 30)

    # PROCESS - Build ordered list of student usernames for table columns
    student_list = [u for u in grades]

    # PROCESS - Define column widths
    col_sub = 14
    col_val = 7

    # OUTPUT - Print table header with student usernames
    header = f'{"SUBJECTS":{col_sub}}'
    for student in student_list:
        header += f' | {student:{col_val}}'
    print(header)
    print('-' * (col_sub + len(student_list) * (col_val + 3)))

    # OUTPUT - Print one row per subject with each student's grade
    for subject in subjects:
        row = f'{subject[:col_sub]:{col_sub}}'
        for student in student_list:
            row += f' | {grades[student][subject]:{col_val}}'
        print(row)

