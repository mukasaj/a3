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
        try:
            self.conn = psycopg.connect(
                dbname=dbname,
                user=user,
                password=password,
                host=host,
                port=port
            )
        except Exception as e:
            print("Failed to connect to database")
            print(e)

    def getAllStudents(self):
        if self.conn is None:
            print("Not connected to database")
            return

        try:
            # executes SELECT query on database
            with self.conn.cursor() as cursor:
                # Using SELECT command to select all students from students table
                cursor.execute("SELECT * FROM students")
                return cursor.fetchall()
        except Exception as e:
            self.conn.rollback()
            print("Failed to delete student")
            print(e)

    def addStudent(self, first_name, last_name, email, enrollment_date):
        if self.conn is None:
            print("Not connected to database")
            return

        try:
            with self.conn.cursor() as cursor:
                # using INSERT command to add a student to the student table
                cursor.execute(
                    "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                    (first_name, last_name, email, enrollment_date))
        except Exception as e:
            self.conn.rollback()
            print("Failed to delete student")
            print(e)

    def updateStudentEmail(self, student_id, new_email):
        if self.conn is None:
            print("Not connected to database")
            return

        try:
            with self.conn.cursor() as cursor:
                # using the UPDATE command to update an email for a given student_id
                cursor.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
        except Exception as e:
            self.conn.rollback()
            print("Failed to delete student")
            print(e)

    def deleteStudent(self, student_id):
        if self.conn is None:
            print("Not connected to database")
            return

        try:
            with self.conn.cursor() as cursor:
                # Using delete command to delete a student with the given student_id
                cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
        except Exception as e:
            self.conn.rollback()
            print("Failed to delete student")
            print(e)


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
            if all_students is None:
                continue
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

