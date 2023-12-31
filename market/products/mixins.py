from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class ListMixin(mixins.ListModelMixin,
                GenericViewSet):
    pass
