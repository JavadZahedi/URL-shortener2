from rest_framework import viewsets
from rest_framework.permissions import AllowAny

class CustomModelViewSet(viewsets.ModelViewSet):
    permission_classes = {
        'default': (AllowAny,)
    }

    def get_permissions(self):
        default_classes = self.permission_classes['default']
        classes = self.permission_classes.get(self.action, default_classes)
        return [permission() for permission in classes]

    def get_serializer_class(self):
        default_class = self.serializer_classes['default']
        return self.serializer_classes.get(self.action, default_class)