import psycopg

DBNAME = None
USER = None
PASSWORD = None
HOST = None
PORT = None


class DatabaseOperations:
    # shared connection variable
    conn = None

    # close the connection when this object is destroyed
    def __del__(self):
        if self.conn is not None:
            self.conn.close()

    # Connects to database and stores connection in shared connection variable
    def connect(self, dbname, user, password, host, port):
        self.conn = psycopg.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )

    def getAllStudents(self):
        if self.conn is None:
            print("Not connected to database")
            return

        # executes SELECT query on database
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM students")
            return cursor.fetchall()

    def addStudent(self, first_name, last_name, email, enrollment_date):
        with self.conn.cursor() as cursor:
            # executes INSERT statement to add student to Database
            cursor.execute(
                "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                (first_name, last_name, email, enrollment_date))

    def updateStudentEmail(self, student_id, new_email):
        with self.conn.cursor() as cursor:
            # executes UPDATE statement to update the email for a given student
            cursor.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))

    def deleteStudent(self, student_id):
        with self.conn.cursor() as cursor:
            # executes DELETE statement to delete a given student
            cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))


if __name__ == '__main__':
    databaseOperations = DatabaseOperations()
    databaseOperations.connect(DBNAME, USER, PASSWORD, HOST, PORT)

    menu_choice = None

    while menu_choice != "q":
        # menu
        print()
        print("1 - Print all students")
        print("2 - Add a student")
        print("3 - Update a student's email address")
        print("4 - Delete a student")
        print("q - Exit")
        menu_choice = input(">>> ")

        # calling corresponding function
        if menu_choice == "1":
            all_students = databaseOperations.getAllStudents()
            for row in all_students:
                print(row)

        if menu_choice == "2":
            databaseOperations.addStudent(
                input("First Name: "),
                input("Last Name: "),
                input("Email: "),
                input("Enrollment Date (yyyy-mm-dd): ")
            )

        if menu_choice == "3":
            databaseOperations.updateStudentEmail(
                input("Student ID: "),
                input("New Email: ")
            )

        if menu_choice == "4":
            databaseOperations.deleteStudent(
                input("Student ID: ")
            )

