from django.forms import Form, ModelForm, MultipleChoiceField, SelectMultiple

from main.models import Task, Topic, Homework
from users.models import CustomUser


class ChooseStudentsForm(Form):
    options = MultipleChoiceField(
        widget=SelectMultiple,
        required=False, 
        label="Выберите студентов для добавления в курс"
    )

    def __init__(self, *args, **kwargs):
        course = kwargs.pop('course')
        super().__init__(*args, **kwargs)

        students = CustomUser.objects.filter(user_type='student').exclude(enrolled_courses=course)
        
        self.fields['options'].choices = [(str(student.id), student) for student in students if not student.is_superuser]
        print(self.fields['options'].choices)

class AssignmentUpload(ModelForm):
    class Meta:
        model = Task
        exclude = ['topic']


class TopicCreatingForm(ModelForm):
    class Meta:
        model = Topic
        exclude = ['course']


class HomeworkUploading(ModelForm):
    class Meta:
        model = Homework
        exclude = ['student', 'assignment', 'mark', 'teacher_comment']


class HomeworkRating(ModelForm):
    class Meta:
        model = Homework
        exclude = []
