from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from rest_framework.pagination import CursorPagination

from .filters import EventFilter
from .models import Event, EventStatus
from .serializers import EventSerializer


class EventCursorPagination(CursorPagination):
    """Класс пагинации с помощью курсора, сделан для  демонстрации,
    на данный момент тут достаточно обычной LimitOffsetPagination, она указана в settings.py по дефолту
    """

    page_size = 10
    ordering = "-date"
    cursor_query_param = "cursor"
    page_size_query_param = "page_size"
    max_page_size = 100


class EventListView(generics.ListAPIView):
    """Класс представления списка мероприятий"""

    queryset = Event.objects.select_related("place").filter(status=EventStatus.OPEN)
    serializer_class = EventSerializer
    pagination_class = EventCursorPagination

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    filterset_class = EventFilter
    ordering_fields = ["date", "name"]
    ordering = ["date"]
