from django.forms import Form, ModelForm, MultipleChoiceField, SelectMultiple

from main.models import Task
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

        students = CustomUser.objects.filter(user_type='student').exclude(courses=course)
        
        self.fields['options'].choices = [(str(student.id), student) for student in students if not student.is_superuser]


class AssignmentUpload(ModelForm):
    class Meta:
        model = Task
        exclude = []
