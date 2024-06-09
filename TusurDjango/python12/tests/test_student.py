import pytest
from django_primer.models import Student


@pytest.mark.django_db
def test_student_count():
    """Тестирует количество студентов в базе данных."""
    # Создание тестовых данных для студентов
    Student.objects.create(name='Иван', surname='Иванов', email='ivanov.ivan@iivan.com')
    Student.objects.create(name='Петр', surname='Петров', email='petrov.petr@ppetr.com')
    Student.objects.create(name='Сидор', surname='Сидоров', email='sidorov.sidor@ssidor.com')

    student_count = Student.objects.count()
    assert student_count == 3, f'Ожидалось 3 студента, но найдено {student_count}'
