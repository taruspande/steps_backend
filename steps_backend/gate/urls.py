from django.urls import path
from .views import EntryCreateView

urlpatterns = [
    path('entries/create/', EntryCreateView.as_view(), name='entry-create'),
]
