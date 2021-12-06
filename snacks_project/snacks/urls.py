from django.urls import path

from snacks.views import HomeView ,AboutUsViews, SnackDetailView,SnackListView

urlpatterns = [
    path('', HomeView.as_view(),name= "home"),
    path('AboutUs/',AboutUsViews.as_view(),name="about-us"),
    path('snack-list/',SnackListView.as_view(),name="snack_list"),
    path("<int:pk>",SnackDetailView.as_view(),name="snack_detail"),
]