from django.db import models


class Subject(models.Model):
    # Поле для хранения названия предмета
    name = models.CharField(
        max_length=20,
        null=False,
        verbose_name='Название предмета'
    )

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
        ordering = ['name']  # Сортировка по названию предмета

    def __str__(self):
        """Возвращает строковое представление предмета."""
        return self.name

    def __repr__(self):
        """Возвращает строковое представление объекта предмета для отладки."""
        return f'<Subject(name="{self.name}")>'
