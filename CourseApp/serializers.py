from .models import Course
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class CourseSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = ['id', 'title', 'course_code']

    def save(self, username, **kwargs):

        new_course = Course(
            title = self.validated_data['title'],
            course_code = self.validated_data['course_code'],
        )
        new_course.tutor = User.objects.get(username=username)
        new_course.save()