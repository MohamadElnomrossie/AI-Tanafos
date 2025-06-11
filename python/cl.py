
class student():
    __student_name=''
    __student_age=0
    __student_gpa=0
    __student_gender=''
    # constructor
    def __init__(self,name='ssss'):
        print('running')
        self.__student_name=name
        
    
    def __student_info(self):
        print(f"Name : {self.__student_name}")
        print(f"Age : {self.__student_age}")
        print(f"GPA : {self.__student_gpa}")
        print(f"Gender : {self.__student_gender}")

    def set_name(self,name):
        self.__student_name=name
    def get_name(self):
        return self.__student_name
    def save_data(self):
        pass