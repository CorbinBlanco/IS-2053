# course_name = "Intoduction to Python"
#
# course_instructor = "Dan Schumacher"
#
# num_students = str(39)
#
# print(course_name)
# print(course_instructor)
# print(num_students)
#
# print(f"Course Name: {course_name}, \n Instructor: {course_instructor}, \n Number of Students: {num_students}")
#
# print()
# print()
#
# print(type(course_name))
# print(type(course_instructor))
# print(type(num_students))
#

class Users:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __init__(self, host, port):
        self.host = host
        self.port = port

user1 = Users("user1", "pass")
print(user1)

c1 = Users("192.168.0.10", "22")
print(c1)
print(c1.username)
print(c1.port)

