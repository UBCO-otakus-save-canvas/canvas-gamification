from rest_framework import serializers

from course.models.models import ReportQuestion


class ReportQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReportQuestion
        fields = ['question_id', 'report_timestamp', 'unclear_description', 'test_case_incorrect_answer',
                  'test_case_violate_constraints', 'poor_test_coverage', 'language_specific_issue',
                  'other', 'report_text']
