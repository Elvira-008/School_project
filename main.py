"""
Скрипт для заполнения базы данных тестовыми данными.
Запуск: python main.py

"""

import os
import sys
import django
from datetime import date, time, timedelta
import random

# --- Настройка Django ---
# Если запускаете НЕ через shell, раскомментируйте строки ниже:
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BASE_DIR, "myproject"))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from school_app.models import (
    UserProfile, School, Subject, ClassGroup,
    StudentProfile, Teacher, Lesson, Grade,
    QuarterGrade, Homework, Book, Attendance
)

print("🚀 Начинаем заполнение базы данных...")

# ──────────────────────────────────────────
# 1. ШКОЛА
# ──────────────────────────────────────────
school, _ = School.objects.get_or_create(
    name_school="Средняя школа №1 имени Манаса",
    defaults={
        "address_school": "г. Бишкек, ул. Чуй 123",
        "phonenumbers": "+996312123456",
        "create_at": date(2000, 9, 1),
    }
)
print(f"✅ Школа: {school}")

# ──────────────────────────────────────────
# 2. ПРЕДМЕТЫ
# ──────────────────────────────────────────
subjects_data = [
    "Математика", "Русский язык", "Физика",
    "История", "Английский язык", "Биология",
]
subjects = []
for name in subjects_data:
    subj, _ = Subject.objects.get_or_create(
        subject_name=name,
        school=school,
        defaults={"photo_subject": ""}
    )
    subjects.append(subj)
    print(f"  📚 Предмет: {subj}")

# ──────────────────────────────────────────
# 3. КЛАССЫ (5А–11Б)
# ──────────────────────────────────────────
class_names = [
    ("5А", "2024-2025"), ("5Б", "2024-2025"),
    ("6А", "2024-2025"), ("6Б", "2024-2025"),
    ("7А", "2024-2025"), ("8А", "2024-2025"),
    ("9А", "2024-2025"), ("10А", "2024-2025"),
    ("11А", "2024-2025"),
]
class_groups = []
for cname, cyear in class_names:
    cg, _ = ClassGroup.objects.get_or_create(
        class_name=cname,
        defaults={"school": school, "class_year": cyear}
    )
    class_groups.append(cg)
    print(f"  🏫 Класс: {cg}")

# ──────────────────────────────────────────
# 4. УЧИТЕЛЯ (реальные кыргызские имена)
# ──────────────────────────────────────────
teachers_info = [
    ("Айгуль",   "Асанова",     "Бекова",    "математика",   subjects[0]),
    ("Нурлан",   "Джакыпов",    "Маматов",   "рус_язык",     subjects[1]),
    ("Гульнара", "Токтосунова", "Осмонова",  "физика",       subjects[2]),
    ("Бакыт",    "Эркинбаев",   "Сыдыков",   "история",      subjects[3]),
    ("Мээрим",   "Сатыбалдиева","Абдиева",   "английский",   subjects[4]),
    ("Зарина",   "Кулова",      "Мамытова",  "биология",     subjects[5]),
]

teacher_objects = []
for first, last, maiden, login_base, subj in teachers_info:
    login = f"teacher_{login_base}"
    user, created = UserProfile.objects.get_or_create(
        login=login,
        defaults={
            "username": login,
            "full_name": f"{last} {first} {maiden}",
            "role": "teacher",
            "phone_number": f"+99670{random.randint(1000000,9999999)}",
        }
    )
    if created:
        user.set_password("Test1234!")
        user.save()

    # Нужен хотя бы один урок для Teacher.lesson
    # Создадим временный урок-заглушку и заменим ниже
    lesson_stub, _ = Lesson.objects.get_or_create(
        school=school,
        subject=subj,
        class_group=class_groups[0],
        date=date.today(),
        start_time=time(8, 0),
        end_time=time(8, 45),
    )
    teacher_obj, _ = Teacher.objects.get_or_create(
        teacher_name=user,
        defaults={
            "lesson": lesson_stub,
            "school": school,
            "subject_teacher": subj,
        }
    )
    teacher_objects.append((teacher_obj, subj))
    print(f"  👩‍🏫 Учитель: {user.full_name} → {subj.subject_name}")

# ──────────────────────────────────────────
# 5. УЧЕНИКИ — 5-6 на каждый класс
# ──────────────────────────────────────────
students_pool = [
    # (имя, фамилия, отчество)
    ("Айдар",    "Маматов",      "Эркинович"),
    ("Бегимай",  "Асанова",      "Нурланова"),
    ("Данияр",   "Токтосунов",   "Бакытович"),
    ("Гулзат",   "Омурова",      "Азизовна"),
    ("Эрлан",    "Сыдыков",      "Темирович"),
    ("Мээрим",   "Джакыпова",    "Бекова"),
    ("Нурбек",   "Кулов",        "Маратович"),
    ("Айсулуу",  "Эркинбаева",   "Акматовна"),
    ("Тимур",    "Абдиев",       "Нурланович"),
    ("Салтанат", "Осмонова",     "Манасовна"),
    ("Жаныбек",  "Мамытов",      "Кайратович"),
    ("Назгуль",  "Сатыбалдиева", "Темировна"),
    ("Алмаз",    "Бейшенов",     "Нурбекович"),
    ("Жылдыз",   "Токонова",     "Азизовна"),
    ("Рустам",   "Кадыров",      "Бакытович"),
    ("Перизат",  "Аманова",      "Эрлановна"),
    ("Адилет",   "Жунусов",      "Айдарович"),
    ("Кыялай",   "Усупова",      "Нурбекова"),
    ("Санжар",   "Мырзаев",      "Темирович"),
    ("Айжан",    "Болотова",     "Манасовна"),
    ("Улан",     "Исаков",       "Жаныбекович"),
    ("Гулира",   "Тилекова",     "Кайратовна"),
    ("Бакыт",    "Эшматов",      "Рустамович"),
    ("Нурай",    "Кенжебаева",   "Адилетовна"),
    ("Жоодар",   "Алымбеков",    "Санжарович"),
    ("Акмарал",  "Суранова",     "Уланова"),
    ("Ырыскул",  "Дуйшеев",      "Бакытович"),
    ("Айдана",   "Пазылова",     "Жылдызовна"),
    ("Медет",    "Торобеков",    "Адилетович"),
    ("Зулайха",  "Мамиева",      "Алмазовна"),
    ("Канат",    "Сейткали",     "Улановин"),
    ("Айпери",   "Раимбекова",   "Медетовна"),
    ("Нурдоолот","Осмоналиев",   "Жоодарович"),
    ("Бурул",    "Акматова",     "Каналовна"),
    ("Тилек",    "Джумабаев",    "Нурдоолотович"),
    ("Чолпон",   "Ибраева",      "Тилековна"),
    ("Арстанбек","Кожобеков",    "Медетович"),
    ("Малика",   "Аскарова",     "Чолпоновна"),
    ("Эмиль",    "Турсунов",     "Арстанбекович"),
    ("Жаркын",   "Садырова",     "Эмилевна"),
    ("Акбар",    "Нурматов",     "Тилекович"),
    ("Динара",   "Жолдошева",    "Акбаровна"),
    ("Мирлан",   "Бакыров",      "Жаркынович"),
    ("Гулбара",  "Сопубекова",   "Мирлановна"),
    ("Асель",    "Карабекова",   "Акбаровна"),
    ("Омурбек",  "Дженишбеков",  "Талантович"),
    ("Айнура",   "Сатарова",     "Омурбековна"),
    ("Талант",   "Бообеков",     "Кубатович"),
    ("Жибек",    "Сулайманова",  "Талантовна"),
    ("Кубат",    "Мукашев",      "Мирланович"),
    ("Назира",   "Аширова",      "Кубатовна"),
    ("Руслан",   "Эсенгулов",    "Жоодарович"),
    ("Венера",   "Байгазиева",   "Русланова"),
    ("Нурсат",   "Кенешов",      "Адилетович"),
    ("Айзат",    "Токторова",    "Нурсатовна"),
]

random.shuffle(students_pool)
student_index = 0
all_students_by_class = {}  # class_group -> [StudentProfile]

PER_CLASS = 6  # учеников на класс

for cg in class_groups:
    class_students = []
    for i in range(PER_CLASS):
        if student_index >= len(students_pool):
            break
        first, last, mid = students_pool[student_index]
        student_index += 1
        login = f"student_{last.lower()}_{cg.class_name.lower()}_{i}"
        user, created = UserProfile.objects.get_or_create(
            login=login,
            defaults={
                "username": login,
                "full_name": f"{last} {first} {mid}",
                "role": "student",
                "phone_number": f"+99655{random.randint(1000000,9999999)}",
            }
        )
        if created:
            user.set_password("Student123!")
            user.save()

        sp, _ = StudentProfile.objects.get_or_create(
            user_student=user,
            defaults={"school": school, "class_group": cg}
        )
        class_students.append(sp)

    all_students_by_class[cg.id] = class_students
    print(f"  🎒 Класс {cg.class_name}: добавлено {len(class_students)} учеников")

# ──────────────────────────────────────────
# 6. УРОКИ — по 2 урока на предмет для каждого класса
# ──────────────────────────────────────────
today = date.today()
lesson_objects = {}  # (class_group_id, subject_id) -> [Lesson]

slot_times = [
    (time(8, 0),  time(8, 45)),
    (time(9, 0),  time(9, 45)),
    (time(10, 0), time(10, 45)),
    (time(11, 0), time(11, 45)),
    (time(12, 0), time(12, 45)),
    (time(13, 0), time(13, 45)),
]

for cg in class_groups:
    for idx, subj in enumerate(subjects):
        lessons_for_pair = []
        for day_offset in [0, 7]:  # сегодня и неделю назад
            lesson_date = today - timedelta(days=day_offset)
            start_t, end_t = slot_times[idx % len(slot_times)]
            lesson, _ = Lesson.objects.get_or_create(
                school=school,
                subject=subj,
                class_group=cg,
                date=lesson_date,
                start_time=start_t,
                end_time=end_t,
            )
            lessons_for_pair.append(lesson)
        lesson_objects[(cg.id, subj.id)] = lessons_for_pair

print(f"  📅 Уроки созданы")

# ──────────────────────────────────────────
# 7. ОЦЕНКИ И ПОСЕЩАЕМОСТЬ
# ──────────────────────────────────────────
numeric_grades = ["2", "3", "4", "5"]
attendance_statuses = ["present", "present", "present", "absent"]  # 75% присутствие

for cg in class_groups:
    students = all_students_by_class.get(cg.id, [])
    for subj in subjects:
        teacher_obj, _ = next(
            ((t, s) for t, s in teacher_objects if s == subj),
            (teacher_objects[0][0], subjects[0])
        )
        lessons = lesson_objects.get((cg.id, subj.id), [])

        for student in students:
            for lesson in lessons:
                grade_val = random.choice(numeric_grades)
                grade, _ = Grade.objects.get_or_create(
                    student=student,
                    subject=subj,
                    teacher=teacher_obj,
                    defaults={"value_choices": grade_val}
                )

                att_status = random.choice(attendance_statuses)
                Attendance.objects.get_or_create(
                    grade=grade,
                    student=student,
                    lesson=lesson,
                    defaults={"status": att_status}
                )

print("  📝 Оценки и посещаемость добавлены")

# ──────────────────────────────────────────
# 8. ЧЕТВЕРТНЫЕ ОЦЕНКИ
# ──────────────────────────────────────────
for cg in class_groups:
    students = all_students_by_class.get(cg.id, [])
    for student in students:
        for subj in subjects:
            for qnum in ["I", "II", "III"]:
                QuarterGrade.objects.get_or_create(
                    student=student,
                    subject=subj,
                    quarter_number=qnum,
                    defaults={
                        "quarter_choices": random.choice(["3", "4", "5"]),
                        "school_year": "2024-2025",
                    }
                )

print("  📊 Четвертные оценки добавлены")

# ──────────────────────────────────────────
# 9. ДОМАШНИЕ ЗАДАНИЯ
# ──────────────────────────────────────────
homework_titles = {
    "Математика":       ["Решить задачи §12 №1-5", "Контрольная работа по теме «Уравнения»"],
    "Русский язык":     ["Написать сочинение на тему «Моя школа»", "Упр. 45, 46 — списать и разобрать"],
    "Физика":           ["Решить задачи на законы Ньютона (стр. 87)", "Лабораторная работа №3"],
    "История":          ["Составить хронологию событий 1917 года", "Прочитать §18-19, ответить на вопросы"],
    "Английский язык":  ["Написать эссе 'My future profession' (150 слов)", "Выучить слова Unit 7"],
    "Биология":         ["Зарисовать клетку и подписать органеллы", "Доклад о фотосинтезе"],
}

for cg in class_groups:
    for subj in subjects:
        lessons = lesson_objects.get((cg.id, subj.id), [])
        titles = homework_titles.get(subj.subject_name, ["Выполнить задание из учебника"])
        for lesson, title in zip(lessons, titles):
            Homework.objects.get_or_create(
                lesson=lesson,
                title=title,
                defaults={
                    "deadline": lesson.date + timedelta(days=7),
                    "file_url": "",
                }
            )

print("  📋 Домашние задания добавлены")

# ──────────────────────────────────────────
# 10. УЧЕБНИКИ
# ──────────────────────────────────────────
books_data = [
    ("Алгебра 7",            "Алимов Ш.А.",      "Математика",       7,  "https://example.com/algebra7.pdf"),
    ("Геометрия 8",          "Атанасян Л.С.",     "Математика",       8,  "https://example.com/geo8.pdf"),
    ("Русский язык 6",       "Баранов М.Т.",      "Русский язык",     6,  "https://example.com/rus6.pdf"),
    ("Физика 9",             "Перышкин А.В.",     "Физика",           9,  "https://example.com/phys9.pdf"),
    ("История КР 8",         "Плоских В.М.",      "История",          8,  "https://example.com/hist8.pdf"),
    ("English 7 Spotlight",  "Virginia Evans",    "Английский язык",  7,  "https://example.com/eng7.pdf"),
    ("Биология 6",           "Пасечник В.В.",     "Биология",         6,  "https://example.com/bio6.pdf"),
]

for title, author, subj_name, grade_lvl, url in books_data:
    subj = next((s for s in subjects if s.subject_name == subj_name), subjects[0])
    Book.objects.get_or_create(
        title=title,
        defaults={
            "author": author,
            "subject": subj,
            "grade_level": grade_lvl,
            "file_url": url,
        }
    )

print("  📖 Учебники добавлены")

# ──────────────────────────────────────────
# ИТОГ
# ──────────────────────────────────────────
print("\n" + "="*50)
print("✅ База данных успешно заполнена!")
print(f"   Школ:           {School.objects.count()}")
print(f"   Предметов:      {Subject.objects.count()}")
print(f"   Классов:        {ClassGroup.objects.count()}")
print(f"   Учеников:       {StudentProfile.objects.count()}")
print(f"   Учителей:       {Teacher.objects.count()}")
print(f"   Уроков:         {Lesson.objects.count()}")
print(f"   Оценок:         {Grade.objects.count()}")
print(f"   Посещаемостей:  {Attendance.objects.count()}")
print(f"   Дом. заданий:   {Homework.objects.count()}")
print(f"   Учебников:      {Book.objects.count()}")
print("="*50)