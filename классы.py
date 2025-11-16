class Bachelor:
    def __init__(self, surname='Не определен', speciality='Не определен', course=0, expelled=False):
        self.__surname = surname
        self.__speciality = speciality
        self.__course = course
        self.__expelled = expelled
        self.__password = 'admin'

    def show_all_info(self):
        print({'surname': self.__surname, 'speciality': self.__speciality, 'course': self.__course, 'expelled': self.__expelled})

    @property
    def surname(self):
        return self.__surname

    @property
    def speciality(self):
        return self.__speciality

    @property
    def course(self):
        return self.__course

    @property
    def get_password(self):
        return self.__password

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @speciality.setter
    def speciality(self, speciality):
        self.__speciality = speciality

    @course.setter
    def course(self, course):
        self.__course = course

    def expell(self):
        self.__expelled = True

    def change_student_data(self, code_of_change, change=''):
        if 1 <= code_of_change <= 5:
            match code_of_change:
                case 1:
                    self.__surname = change
                case 2:
                    self.__speciality = change
                case 3:
                    if 1 <= int(change) <= 4:
                        self.__course = int(change)
                        print('Успешно')
                    else:
                        print('Неверный номер курса')
                case 4:
                    self.__expelled = True
                case 5:
                    self.__password = change
        else:
            return 'Неверный код изменения'

    def get_academic_status(self):
        if self.__expelled:
            return 'Отчислен'
        elif self.__course == 1:
            return 'Первокурсник'
        elif self.__course == 2:
            return 'Второкурсник'
        elif self.__course == 3:
            return 'Третьекурсник'
        elif self.__course == 4:
            return 'Выпускник'
        else:
            return 'Не определен'

    def years_until_graduation(self):
        if self.__expelled:
            return 'Студент отчислен'
        return 4 - self.__course

    def is_same_group(self, other_student):
        return (self.__speciality == other_student.__speciality and
                self.__course == other_student.__course and
                not self.__expelled and not other_student.__expelled)

    def is_same_speciality(self, other_student):
        return (self.__speciality == other_student.__speciality and
                not self.__expelled and not other_student.__expelled)

    def compare_by_course(self, other_student):
        if other_student.__expelled or self.__expelled:
            return 'Сравнить невозможно. Один из студентов был отчислен'

        if self.__course > other_student.__course:
            return f'{self.__surname} старше {other_student.__surname}'
        elif self.course < other_student.course:
            return f'{self.__surname} младше {other_student.__surname}'
        else:
            return 'Студенты на одном курсе'


class Menu:
    def __init__(self, student: Bachelor, other_student: Bachelor):
        self.student = student
        self.other_student = other_student

    def show_menu(self):

        print('МЕНЮ. ВВЕДИТЕ ТОЛЬКО ЧИСЛО')
        print('1. Показать информацию')
        print('2. Изменить данные студента')
        print('3. Отчислить студента')
        print('4. Получить академический статус')
        print('5. Получить кол-во лет до окончания учёбы')
        print('6. Находятся ли студенты в одной группе')
        print('7. Обучаются ли студенты по одной специальности')
        print('8. Находятся ли студенты на одном курсе')
        print('9. Выход')

    def run(self):
        while True:
            self.show_menu()
            choice = input('Выберите действие: ')

            match choice:
                case '1':
                    self.student.show_all_info()
                case '2':
                    password = input('Введите пароль: ')
                    if password == self.student.get_password:

                        print('Что вы хотите изменить? Введите только число')
                        print('1. Изменить фамилию')
                        print('2. Изменить специальность')
                        print('3. Изменить курс')
                        print('4. Поменять пароль')

                        change_code = int(input())
                        change = input('Введите изменение: ')
                        self.student.change_student_data(change_code, change)
                    else:
                        print('Пароль неверен')
                case '3':
                    self.student.expell()
                    print('Студент отчислен')
                case '4':
                    academic_status = self.student.get_academic_status()
                    print(academic_status)
                case '5':
                    years_to_end = self.student.years_until_graduation()
                    print(years_to_end)
                case '6':
                    if self.student.is_same_group(self.other_student):
                        print('В одной группе')
                    else:
                        print('Не в одной группе')
                case '7':
                    if self.student.is_same_speciality(self.other_student):
                        print('На одной специальности')
                    else:
                        print('Не на одной специальности')
                case '8':
                    status_comparing_course = self.student.compare_by_course(self.other_student)
                    print(status_comparing_course)
                case '9':
                    break


class Main:
    student1 = Bachelor('Fedorov', 'DAID', 1)
    student2 = Bachelor('Sergeev', 'MSD',  2)
    all_students = [student1, student2]

    try:
        n = int(input('Выберите номер студента (1-Fedorov, 2-Sergeev) '))

        if n == 1:
            student1_interact = Menu(student1, student2)
            student1_interact.run()
        elif n == 2:
            student2_interact = Menu(student2, student1)
            student2_interact.run()
        else:
            print('Ошибка при введении номера')

    except ValueError:
        print('Введено не число')



if __name__ == '__main__':
    Main()
