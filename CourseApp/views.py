from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import CourseSerializer
from .models import Course

@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_course(request):

    data = request.data
    serializer = CourseSerializer(data=data)
    if serializer.is_valid():
        serializer.save(username=data['username'])
        return Response({"Success": "The course was successfully created"}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_course(request, course_id):

    try:
        get_course_by_id = Course.objects.get(id=course_id, tutor=request.user)
        name = get_course_by_id.title
        get_course_by_id.delete()
        return Response({"Success": f"The course {name} was successfully deleted"}, status=200)
    except Course.DoesNotExist:
        return Response({"Error": f"course with id '{course_id}' not found"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_course(request, course_id):

    try:
        get_course_by_id = Course.objects.get(id=course_id, tutor=request.user)
        serializer = CourseSerializer(get_course_by_id)
        return Response(serializer.data)
    
    except Course.DoesNotExist:
        return Response({"Error": f"course with id '{course_id}' not found"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_all_courses(request):

    get_course_created_by_user = Course.objects.filter(tutor=request.user)
    serializer = CourseSerializer(get_course_created_by_user, many=True)

    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_course(request):

    try:
        get_course_by_id = Course.objects.get(id=request.data.get('course_id'), tutor=request.user)
        
        if request.data.get('course_title'):
            get_course_by_id.title = request.data.get('course_title')

        if request.data.get('course_code'):
            get_course_by_id.course_code = request.data.get('course_code')

        get_course_by_id.save()

        return Response({"Success": f"The course was successfully updated"}, status=200)
    except Course.DoesNotExist:
        return Response({"Error": f"course with id '{request.data.get('course_id')}' not found"}, status=status.HTTP_400_BAD_REQUEST)