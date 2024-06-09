from django.db import models


class Student(models.Model):
    # Поле для хранения имени студента
    name = models.CharField(
        max_length=200,
        null=False,
        verbose_name='Имя'
    )
    
    # Поле для хранения фамилии студента
    surname = models.CharField(
        max_length=200,
        null=False,
        verbose_name='Фамилия'
    )
    
    # Поле для хранения электронной почты студента
    email = models.EmailField(
        null=False,
        verbose_name='Электронная почта'
    )

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        unique_together = ('name', 'surname', 'email')  # Уникальная комбинация имя-фамилия-электронная почта

    @property
    def full_name(self):
        """Возвращает полное имя студента."""
        return f'{self.name} {self.surname}'

    def __str__(self):
        """Возвращает строковое представление студента."""
        return f'{self.full_name} ({self.email})'

    def __repr__(self):
        """Возвращает строковое представление объекта студента для отладки."""
        return (f'Student(name="{self.name}", '
                f'surname="{self.surname}", '
                f'email="{self.email}")')
