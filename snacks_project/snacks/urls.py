from django.urls import path

from snacks.views import HomeView ,AboutUsViews

urlpatterns = [
    path('', HomeView.as_view(),name= "home"),
    path('AboutUs/',AboutUsViews.as_view(),name="about-us")
]