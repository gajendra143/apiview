from django.db import models

# Create your models here.

# model for members
class Member(models.Model):
    member_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.member_name)

#user details model
class Detail(models.Model):
    id_name = models.IntegerField(unique=True)
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=100)
    activity_peroid = models.ForeignKey(Member, related_name='member_activity', on_delete=models.CASCADE, null=True)


    def __str__(self):
        return str(self.real_name)

# user activity model
class Activity(models.Model):
    detail = models.ForeignKey(Detail,related_name='track_activity', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return str(self.detail)
