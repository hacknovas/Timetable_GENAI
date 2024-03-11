from domain import (
    Class,
    Course,
    Department,
    Instructor,
    MeetingTime,
    Room,
)


class Data(object):
    def __init__(self):
        self.rooms = None
        self.instructors = None
        self.courses = None
        self.depts = None
        self.meeting_times = []  # List to store MeetingTime objects
        self.meeting_time_ids = []  # List to store meeting time IDs (optional)

        self.initialize_from_user_input()

    def initialize_from_user_input(self):
        # Get room information
        self.get_room_data()

        # Get instructor information
        self.get_instructor_data()

        # Get course information
        self.get_course_data()

        # Get department information
        self.get_department_data()

        # Get meeting time information
        self.get_meeting_time_data()

        # Define the number of classes based on departments
        self.number_of_classes = sum([len(x.courses) for x in self.depts])

    def get_room_data(self):
        num_rooms = int(input("Enter the number of rooms: "))
        self.rooms = []
        for i in range(num_rooms):
            room_number = input("Enter room number: ")
            seating_capacity = int(input("Enter seating capacity: "))
            room = Room(number=room_number, seating_capacity=seating_capacity)
            self.rooms.append(room)

    def get_instructor_data(self):
        num_instructors = int(input("Enter the number of instructors: "))
        self.instructors = []
        for i in range(num_instructors):
            instructor_id = input("Enter instructor ID: ")
            instructor_name = input("Enter instructor name: ")
            instructor = Instructor(id=instructor_id, name=instructor_name)
            self.instructors.append(instructor)

    def get_course_data(self):
        num_courses = int(input("Enter the number of courses: "))
        self.courses = []
        for i in range(num_courses):
            course_number = input("Enter course number: ")
            course_name = input("Enter course name: ")
            max_students = int(input("Enter maximum number of students: "))
            instructor_ids = []
            num_instructors = int(
                input("Enter the number of instructors for this course: ")
            )
            for j in range(num_instructors):
                instructor_id = input("Enter instructor ID: ")
                instructor_ids.append(instructor_id)
            instructors = [
                instructor for instructor in self.instructors if instructor.id in instructor_ids
            ]
            course = Course(
                number=course_number,
                name=course_name,
                max_number_of_students=max_students,
                instructors=instructors,
            )
            self.courses.append(course)

    def get_department_data(self):
        num_departments = int(input("Enter the number of departments: "))
        self.depts = []
        for i in range(num_departments):
            dept_name = input("Enter department name: ")
            course_numbers = []
            num_courses = int(input("Enter the number of courses in this department: "))
            for j in range(num_courses):
                course_number = input("Enter course number: ")
                course_numbers.append(course_number)
            courses = [course for course in self.courses if course.number in course_numbers]
            department = Department(name=dept_name, courses=courses)
            self.depts.append(department)

    def get_meeting_time_data(self):
        num_meeting_times = int(input("Enter the number of meeting times: "))
        for i in range(num_meeting_times):
            meeting_time_id = input("Enter meeting time ID (optional): ")
            meeting_time_str = input("Enter meeting time (e.g., MWF 09:00 - 10:00):")

            # Create a MeetingTime object (assuming MeetingTime class definition)
            meeting_time = MeetingTime(id=meeting_time_id, time=meeting_time_str)

            self.meeting_times.append(meeting_time)  # Add MeetingTime object to the list

            # Optionally, store the ID separately
            if meeting_time_id:
                self.meeting_time_ids.append(meeting_time_id)