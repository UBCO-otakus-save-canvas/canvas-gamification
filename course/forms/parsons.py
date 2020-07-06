from django import forms
from django.forms import Textarea
from django.template.loader import render_to_string

from course.widgets import JSONEditor
from course.fields import JSONFormField

from course.forms.forms import ProblemCreateForm
from course.models.parsons_question import ParsonsQuestion


class ParsonsQuestionForm(ProblemCreateForm):
    class Meta:
        model = ParsonsQuestion
        fields = (
            'title', 'difficulty', 'category', 'text', 'lines', 'junit_template', 'variables')
        exclude = ('answer',)

    answer = None

    lines = JSONFormField(
        widget=JSONEditor(schema=render_to_string('schemas/lines.json')),
        help_text="""
            It should be an array of lines.
            A valid example:
            [
                "static class Calculator {",
                "public int add(int x, int y) {",
                "return x + y;",
                "}",
                "}"
            ]
            """
    )

    junit_template = forms.CharField(
        label="JUnit Template",
        widget=Textarea(attrs={
            'class': 'form-control'
        }),
        help_text="""
            Please provide a JUnit template to evaluate the code.
            Identify where to insert the solution by "{{code}}"
            """
    )