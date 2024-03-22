from domain.student_group import StudentGroup

class StudentStream:
    def __init__(self, stream_number):
        self.stream_number = stream_number
        self.student_groups = []

    def add_group(self, student_group):
        self.student_groups.append(student_group)

    def __iter__(self):
        return iter(self.student_groups)

class StudentGroup(StudentGroup):
    def __lt__(self, other):
        return len(self.group) < len(other.group)

    def __gt__(self, other):
        return len(self.group) > len(other.group)

    def __eq__(self, other):
        return len(self.group) == len(other.group)

stream = StudentStream(1)
stream.add_group(group)

for group in stream:
    print(group)
    for student in group:
        print(student)

sorted_groups = sorted(stream.student_groups)
for group in sorted_groups:
    print(group)
    for student in group:
        print(student)
