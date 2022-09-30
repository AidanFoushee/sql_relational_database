from operator import contains
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

# def get_name(cursor):
#     cursor.execute("SELECT fname, lname FROM ward")
#     results = cursor.fetchall()
#     for index in range(len(results)):
#         print(f"{index+1}. {results[index][0]} {results[index][1]}")
#     choice = int(input("Select> "))
#     return results[choice - 1][0] + results[choice-1][1]

def sort_oldest_youngest(cursor, gender):
    cursor.execute('SELECT fname, lname, age FROM ward WHERE gender = ? ORDER BY age DESC', gender)
    results = cursor.fetchall()
    for i in range(len(results)):
        print(f'{i+1}. {results[i][0]} {results[i][1]} {results[i][2]}')
    print()

def sort_youngest_oldest(cursor, gender):
    cursor.execute('SELECT fname, lname, age FROM ward WHERE gender = ? ORDER BY age', gender)
    results = cursor.fetchall()
    for i in range(len(results)):
        print(f'{i+1}. {results[i][0]} {results[i][1]} {results[i][2]}')
    print()

choice = 0
while choice != 6:
    print('1. Display ward')
    print('2. Add member')
    print('3. Update member calling')
    print('4. Sort members')
    print('5. Delete member')
    print('6. Quit')
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

    elif choice == 3:
        fname = input('First name: ')
        lname = input('Last name: ')
        calling = input('What is their new calling: ')
        values = (calling, fname, lname)
        cursor.execute('UPDATE ward SET calling = ? WHERE fname = ? AND lname = ?', values)
        connection.commit()
        print()

    elif choice == 4:
        print('1. Sort only men')
        print('2. Sort only women')
        print('3. Sort both men and women')
        choice = int(input('-> '))
        print()

        if choice == 1:
            print('1. Sort by oldest to youngest')
            print('2. Sort by youngest to oldest')
            choice = int(input('-> '))
            print()
            if choice == 1:
                sort_oldest_youngest(cursor, 'M')
            else:
                sort_youngest_oldest(cursor, 'M')

        elif choice == 2:
            print('1. Sort by oldest to youngest')
            print('2. Sort by youngest to oldest')
            choice = int(input('-> '))
            print()
            if choice == 1:
                sort_oldest_youngest(cursor, 'F')
            else:
                sort_youngest_oldest(cursor, 'F')

        elif choice == 3:
            print('1. Sort by oldest to youngest')
            print('2. Sort by youngest to oldest')
            choice = int(input('-> '))
            print()
            if choice == 1:
                cursor.execute('SELECT fname, lname, age FROM ward ORDER BY age DESC')
                results = cursor.fetchall()
                for i in range(len(results)):
                    print(f'{i+1}. {results[i][0]} {results[i][1]} {results[i][2]}')
                print() 
            else:
                cursor.execute('SELECT fname, lname, age FROM ward ORDER BY age')
                results = cursor.fetchall()
                for i in range(len(results)):
                    print(f'{i+1}. {results[i][0]} {results[i][1]} {results[i][2]}')
                print()

    elif choice == 5:
        #name = get_name(cursor)
        fname = input('First name of the person you want to delete: ')
        lname = input('Last name of the person you want to delete: ')
        values = (fname, lname)
        cursor.execute('DELETE FROM ward WHERE fname = ? AND lname = ?', values)
        connection.commit()
        print()

connection.close()