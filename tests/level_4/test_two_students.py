from functions.level_4.two_students import get_student_by_tg_nickname



def test__get_student_by_tg_nickname__returns_matching_student(create_student):
    student_1 = create_student(telegram_account='@victorivanov')
    student_2 = create_student(telegram_account='@alexkorolev')
    student_3 = create_student(telegram_account='@mikhailpetrov')

    assert get_student_by_tg_nickname(telegram_username = 'alexkorolev', 
                                      students = [student_1, student_2, student_3]) == create_student(telegram_account='@alexkorolev')

#вероятно фабрика юзеров тут избыточна, но хотелось попробовать
def test__get_student_by_tg_nickname__returns_student_ignoring_at(create_students, create_student):
    students = create_students(count=3, telegram_account='@alexkorolev')
    assert get_student_by_tg_nickname(telegram_username = 'alexkorolev', 
                                      students = students) == create_student(telegram_account='@alexkorolev')
    
def test__get_student_by_tg_nickname__returns_student_with_account_without_at(create_students, create_student):
    students = create_students(count=3, telegram_account='@alexkorolev')
    assert get_student_by_tg_nickname(telegram_username = 'alexkorolev', 
                                      students = students) == create_student(telegram_account='@alexkorolev')