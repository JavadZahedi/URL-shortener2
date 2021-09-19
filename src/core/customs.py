from rest_framework import viewsets, pagination
from rest_framework.response import Response

class CustomModelViewSet(viewsets.ModelViewSet):

    def get_permissions(self):
        default_classes = self.permission_classes['default']
        classes = self.permission_classes.get(self.action, default_classes)
        return [permission() for permission in classes]

    def get_serializer_class(self):
        default_class = self.serializer_classes['default']
        return self.serializer_classes.get(self.action, default_class)


class CustomPagination(pagination.PageNumberPagination):
    
    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'page_size': self.page_size,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })