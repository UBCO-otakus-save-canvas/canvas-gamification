from rest_framework import serializers
from accounts.models import MyUser


class UsersCourseCountSerializers(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'role']