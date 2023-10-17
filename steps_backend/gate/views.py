from rest_framework import generics
from .models import Entry
from .serializers import EntrySerializer

class EntryCreateView(generics.CreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
