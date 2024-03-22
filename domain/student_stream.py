from domain.student_group import StudentGroup

# Task 1: Create a StudentStream class
class StudentStream:
    def __init__(self, stream_number):
        self.stream_number = stream_number
        self.student_groups = []

    def add_group(self, student_group):
        self.student_groups.append(student_group)

    # Task 2: Implement Iterable interface for StudentStream class
    def __iter__(self):
        return iter(self.student_groups)

# Task 3: Implement sorting for StudentGroup based on the number of students
# Python does not have a Comparable interface, but we can implement the necessary comparison methods
class StudentGroup(StudentGroup):
    def __lt__(self, other):
        return len(self.group) < len(other.group)

    def __gt__(self, other):
        return len(self.group) > len(other.group)

    def __eq__(self, other):
        return len(self.group) == len(other.group)

# Example usage:
stream = StudentStream(1)
# Add groups to the stream...
stream.add_group(group5830)
# ...additional groups would be added here

# Iterate through the groups in the stream
for group in stream:
    print(group)
    for student in group:
        print(student)

# Sort the groups and print them
sorted_groups = sorted(stream.student_groups)
for group in sorted_groups:
    print(group)
    for student in group:
        print(student)