from django.conf.urls import url

from logiccalculator.views import calculate_logic

app_name = 'logiccalculator'
urlpatterns = [
    url(r'home/',calculate_logic,name='home')
]