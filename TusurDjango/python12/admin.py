from django.contrib import admin
from django_primer.models import Student, Subject, Score


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email')
    search_fields = ('name', 'surname', 'email')


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'value')
    search_fields = ('student__name', 'student__surname', 'subject__name')
    list_filter = ('subject',)
