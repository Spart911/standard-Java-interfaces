from domain.student_group import StudentGroup

class StudentStream:
    def __init__(self, stream_number):
        self.stream_number = stream_number
        self.student_groups = []

    def add_group(self, student_group):
        self.student_groups.append(student_group)

    def __iter__(self):
        return iter(self.student_groups)

    def __str__(self):
            students_str = ', '.join(str(student) for student in self.group)
            return f"StudentGroup ID: {self.idGroup}, Number of Students: {len(self.group)}, Students: [{students_str}]"

class StudentGroup(StudentGroup):
    def __lt__(self, other):
        if len(self.group) != len(other.group):
            return len(self.group) < len(other.group)
        else:
            return self.idGroup < other.idGroup

    def __gt__(self, other):
        return len(self.group) > len(other.group)

    def __eq__(self, other):
        return len(self.group) == len(other.group)

stream = StudentStream(1)
stream.add_group(group)

sorted_groups = sorted(stream.student_groups)
for group in sorted_groups:
    print(group)

print(stream)
