from django.urls import path
from .views import EmployeeView
urlpatterns = [
    path('', EmployeeView.as_view()),
    path('<str:pk>', EmployeeView.as_view()),
    # path('getdata/', entryview),
    # path('getdata/<str:pk>', entrydetailview ),
]
