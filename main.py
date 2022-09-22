import sqlite3

connection = sqlite3.connect('ward.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS ward (
    fname TEXT,
    lname TEXT,
    gender TEXT,
    age INT,
    calling TEXT
)''')

choice = 0
while choice != 5:
    print('1. Display ward')
    print('2. Add member')
    print('3. Update member calling')
    print('4. Delete member')
    print('5. Quit')
    choice = int(input('-> '))
    print()

    if choice == 1:
        cursor.execute('SELECT * FROM ward')

        print('{:<15} {:<15} {:<15} {:<15} {:<15}'.format('FirstName', 'LastName', 'Gender', 'Age', 'Calling'))

        for info in cursor.fetchall():
            print('{:<15} {:<15} {:<15} {:<15} {:<15}'.format(info[0], info[1], info[2], info[3], info[4]))

        print()

    elif choice == 2:
        fname = input('First name: ')
        lname = input('Last name: ')
        gender = input('Gender: ')
        age = int(input('Age: '))
        calling = input('Calling: ')
        values = (fname, lname, gender, age, calling)
        cursor.execute('INSERT INTO ward VALUES (?, ?, ?, ?, ?)', values)
        connection.commit()
        print()


connection.close()