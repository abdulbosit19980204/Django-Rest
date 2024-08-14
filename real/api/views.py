from django.shortcuts import get_object_or_404, render
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import TodoModel
from .serializers import TodoModelSerializer


class TodoViewSet(viewsets.ViewSet):
    def list(self, request):
        print(request.stream)
        queryset = TodoModel.objects.all()
        serializer = TodoModelSerializer(queryset, many=True)
        return Response({"data": serializer.data, "ok": True}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        todo = get_object_or_404(TodoModel, pk=pk)
        serializer = TodoModelSerializer(todo)
        return Response({"data": serializer.data, "ok": True}, status=status.HTTP_200_OK)
