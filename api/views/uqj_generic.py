from django_filters import NumberFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from course.models.models import UserQuestionJunction
from api.pagination import BasePagination
from api.serializers import UQJSerializer

from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response


class UQJFilterSet(FilterSet):
    question_event = NumberFilter(field_name='question__event')
    question = NumberFilter(field_name='question')

    class Meta:
        model = UserQuestionJunction
        fields = ['question', 'question_event']


class UQJGenericViewSet(viewsets.GenericViewSet):
    """
    Query Parameters
    + Standard ordering is applied on the field 'last_viewed'
    """
    serializer_class = UQJSerializer
    permission_classes = [IsAuthenticated, ]
    pagination_class = BasePagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, ]
    ordering_fields = ['last_viewed', ]
    filter_class = UQJFilterSet

    @action(detail=True, methods=['post'], url_path='switch-favorite')
    def switch_favorite(self, request, pk=None):
        """
        Updates "is_favorite" for UserQuestionJunction
        """
        status = request.data.get('status')
        junction_id = request.data.get('id')
        uqj = get_object_or_404(UserQuestionJunction, id=junction_id)
        uqj.is_favorite = status
        uqj.save()
        return Response(request.data)
