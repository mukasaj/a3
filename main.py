
class DatabaseOperations:

    def connect(self):
        pass
    #TODO: retrieves and displays all records from the students table
    def getAllStudents(self):
        pass

    #TODO: inserts a new student records into the students table
    def addStudent(self, first_name, last_name, email, enrollment_date):

    #TODO: updates the email address for a student with the specified student_id
    def updateStudentEmail(self, student_id, new_email):

    #TODO: deletes the record of the student with the specified student_id
    def deleteStudent(self, student_id):
    pass

if __name__ == '__main__':
    databaseOperations = DatabaseOperations()
    databaseOperations.connect()

    all_students = databaseOperations.getAllStudents()
    print(all_students)

    databaseOperations.updateStudentEmail()
    all_students = databaseOperations.getAllStudents()
    print(all_students)

    databaseOperations.updateStudentEmail()
    all_students = databaseOperations.getAllStudents()
    print(all_students)

    databaseOperations.deleteStudent()
    all_students = databaseOperations.getAllStudents()
    print(all_students)