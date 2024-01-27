from merooslanish import Teacher, Student

teachers = [Teacher(input("Ismiz:"),input('Familyangiz:'),int(input("tajribangiz:")))  for _ in range(int(input("necha nafar o'qituvchi bor:")))]
students=[]
for _ in range(int(input("Necha nafar o'quvchi bor "))):
    student = Student(
        input('Ismiz ?'),
        input("Familyangiz ?"),
        input("universitet nomi?"),
        int(input("Yoshingiz:")),
        input("Jinsizngiz:")

    )
    students.append(student)
    print("Ustoz tanglang")
    counter=1
    for teacher in teachers:
        print(f"Id:{counter} Ism:{teacher.ism.capitalize()}")
        counter+=1
    ustoz=int(input("ustozning Id raqamini kiriting:"))-1
    teachers[ustoz].students.append(student)

yosh_chegarasi=int(input("necha yoshdan kaatta talaabalar ko'rinsin:"))



for teacher in teachers:
    print()
    print(teacher.teacher_tanishtir())

    print('ustozning umimiy o\'quvchilar soni',len(teacher.students))
    print("")
    student_yers = []
    erkak=0
    ayol=0
    for student in teacher.students:
        student_yers.append(student.yosh)

        if student.jinsi=="erkak" or student.jinsi=="Erkak":
            erkak+=1
        elif student.jinsi=="ayol" or student.jinsi=="ayol":
            ayol+=1

    minyers=min(student_yers)
    maxyers=max(student_yers)



    for student in teacher.students:
        if student.yosh == minyers:
            print('eng yosh  o\'quvchisi', minyers)

        if student.yosh == maxyers:
            print('eng katta  o\'quvchisi', maxyers)

    print("Studentlarning o'rtacha yoshi",sum(student_yers)/len(student_yers))
    print("erkak o'quvchilar soni",erkak)
    print("ayol o'quvchilar soni",ayol)
    for student in teacher.students:
        if student.yosh >= yosh_chegarasi:
            print(student.student_tanishtir())







