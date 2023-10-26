# Create dictionaries for room numbers, instructors, and meeting times
room_numbers = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

meeting_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

# Prompt user for a course number
course_number = input("Please enter a course number: ")

# Check if the course number exists in the dictionaries
if course_number in room_numbers and course_number in instructors and course_number in meeting_times:
    room_number = room_numbers[course_number]
    instructor = instructors[course_number]
    meeting_time = meeting_times[course_number]

    # Display the information
    print(f"Course: {course_number}")
    print(f"Room Number: {room_number}")
    print(f"Instructor: {instructor}")
    print(f"Meeting Time: {meeting_time}")
else:
    print("Course not found.")
