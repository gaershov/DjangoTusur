from collections import defaultdict

from django.views.generic.base import TemplateView

from .models import Score


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        
        # Получаем все оценки из базы данных
        all_scores = Score.objects.all()
        
        # Создаем словарь для хранения статистики по студентам и предметам
        student_statistics = defaultdict(dict)
        
        # Создаем множество для хранения всех предметов
        all_subjects = set()
        
        # Заполняем словарь статистики и множество предметов
        for score in all_scores:
            subject_name = score.subject.name
            all_subjects.add(subject_name)
            student_statistics[score.student][subject_name] = score.value
        
        # Сортируем предметы в алфавитном порядке
        sorted_subjects = sorted(all_subjects)
        
        # Форматируем статистику студентов
        formatted_student_statistics = [
            {
                'student': student,
                'scores': [f'{scores[subject]:.1f}' for subject in sorted_subjects]
            }
            for student, scores in student_statistics.items()
        ]
        
        # Обновляем контекст представления
        context.update(
            {
                'subjects': sorted_subjects,
                'student_statistics': formatted_student_statistics
            }
        )
        return context
