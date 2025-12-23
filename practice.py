# 연습용 클래스 + 리스트 + 함수
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average(self):
        return sum(self.scores) / len(self.scores)


def print_student_avg(student):
    avg = student.average()
    print(f"{student.name}의 평균 점수는 {avg}점입니다.")


# 배열(list)
students = [
    Student("노혀니", [30, 40, 50]),
    Student("김노현", [70, 75, 80])
]

# 함수 실행
for s in students:
    print_student_avg(s)
