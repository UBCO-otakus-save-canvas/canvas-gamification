# Register your models here.
from django import forms
from django.contrib import admin
from djrichtextfield.widgets import RichTextWidget

from general.models.contact_us import ContactUs
from general.models.action import Action
from general.models.faq import FAQ
from general.models.question_report import QuestionReport


class FAQAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FAQAdminForm, self).__init__(*args, **kwargs)

        self.fields['answer'].widget = RichTextWidget(field_settings='advanced')

    class Meta:
        model = FAQ
        exclude = []


class FAQAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'question')
    form = FAQAdminForm


class ActionAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'description', 'actor', 'token_change', 'status')
    list_filter = ('status',)


class QuestionReportAdmin(admin.ModelAdmin):
    list_filter = ('user__username', 'question')
    list_display = ('user', 'question', 'report_timestamp', 'unclear_description', 'test_case_incorrect_answer',
                    'test_case_violate_constraints', 'poor_test_coverage', 'language_specific_issue',
                    'other', 'report_text')


admin.site.register(FAQ, FAQAdmin)
admin.site.register(Action, ActionAdmin)
admin.site.register(ContactUs)
admin.site.register(QuestionReport, QuestionReportAdmin)
