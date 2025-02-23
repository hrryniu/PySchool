import sqlite3

#łączenie do bazy danych, sqlite to baza lokalna
connection = sqlite3.connect("todo.db")

def create_table(connection): #przy każdym uruchomieniu program będzie chciał tworzyć baze danych jesli taki plik już będzie istniał to program da nam błąd. ale dzięki funkcji try except, unikamy wywalenia pliku
    try:
        cur = connection.cursor()
        cur.execute("""CREATE TABLE task(task text)""")     #tworzymy tabelę task z jedną tabelą o nazwię task i formacie tekstowym
    except:
        pass

def show_task(connection):
    print("pokazujemy zadania")
    cur = connection.cursor()
    cur.execute("""SELECT rowid, task FROM task""")
    result = cur.fetchall()

    for row in result:
        print(str(row[0])+ ". " + row[1])


def add_task(connection):
    print("dodajemy zdanie")
    task = input("Wpisz treść zadania: ")
    if task == "0":
         print("Powrót do menu")
    else:
         cur = connection.cursor()
         cur.execute("""INSERT INTO task(task) VALUES(?)""",(task,))
         connection.commit()
         print("Dodano zadanie!")


def delete_task(connection):
    task_index = int(input("Podaj indeks zadania do usunięcia: "))
    cur = connection.cursor()
    rows_deleted = cur.execute("""DELETE FROM task WHERE rowid=?""",(task_index,)).rowcount
    connection.commit()
    if rows_deleted ==0:
        print("Takie zadanie nie istanieje!")
    else:
         print("Usunięto zadanie!")

create_table(connection)

while True:

    print()
    print("1. Pokaż zadania")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Wyjdź")

    user_choice = int(input("Wybierz liczbę: "))
    print()

    if user_choice == 1:
        show_task(connection)

    if user_choice == 2:
        add_task(connection)

    if user_choice == 3:
        delete_task()

    if user_choice == 4:
        break

connection.close()