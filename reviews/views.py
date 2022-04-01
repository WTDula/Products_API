from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status

@api_view(["GET", "POST"])
def reviews_list(request):
    if request.method == "GET":
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many = True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ReviewSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)