from rest_framework import serializers
from .models import Member,Detail,Activity


class activitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id','start_time', 'end_time']

class detailSerializer(serializers.ModelSerializer):
    track_activity = activitySerializer(many=True, read_only=True)

    class Meta:
        model = Detail
        extra_kwargs = {'track_activity': {'write_only': True}}

        fields = ['id','real_name', 'tz', 'track_activity']

# class memberForSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Detail
#         fields = ['id','id_name','real_name', 'tz']

class memberSerializer(serializers.ModelSerializer):
    member_activity = detailSerializer(many=True, read_only=True)

    class Meta:
        model = Member
        fields = ['id','member_name', 'member_activity']




