from django.contrib import admin
from django.urls import path
from webapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('areaofrightcylinder/',views.rightcylinder,name="areaofrightcylinder"),
    path('',views.rightcylinder,name="areaofrightcylinderroot")
]