# urls.py
from django.urls import path
# from books.views import PublisherList
from .views import *

urlpatterns = [
    path('', QuoteList.as_view(), name='quote_list'),
    path('quote/<int:pk>/', QuoteDetailView.as_view(), name='quote_detail'),
    path('create/', QuoteCreate.as_view(), name='quote_create'),
    path('update/<int:pk>', QuoteUpdate.as_view(), name='quote_update'),
    path('delete/<int:pk>', QuoteDelete.as_view(), name='quote_delete'),
]