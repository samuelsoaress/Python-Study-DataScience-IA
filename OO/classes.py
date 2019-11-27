students = []

class Student:
    school_name = "Springfield Elementary"
    def __init__(self, nome, student_id=332):
        self.nome = name
        self.student_id = student_id
        students.append(self)

    
    def __str__(self): ## Não retorna mais o endereço do objeto mais sim seus atributos valorador
        return "Student" = self.nome

    def get_name_capitalize(self):
        return self.nome.capitalize()

    def get_school_name(self):
        return self.school_name

#EXTENDENDO

class HighSchoolStudent(Student):
    
    school_name = "Springfield High School"

    def get_school_name():
        return "Springfield High School "
