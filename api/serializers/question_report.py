from rest_framework import serializers
from general.models.question_report import QuestionReport


class QuestionReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionReport
        fields = ['question_id', 'created_at', 'updated_at', 'unclear_description', 'test_case_incorrect_answer',
                  'test_case_violate_constraints', 'poor_test_coverage', 'language_specific_issue',
                  'other', 'report_text']
