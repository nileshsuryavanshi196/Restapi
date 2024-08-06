from django.urls import path
from app import views
from app.views import Viewsapi,Createapi,Updateapi,Deleteapi

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('recipeform/',views.recipeform,name='recipeform'),
    path('searchrecipe/',views.searchrecipe,name='searchrecipe'),
    path("updaterecipe/<recipe_id>", views.updaterecipe, name="updaterecipe"),
    path("removerecipe/<recipe_id>", views.removerecipe, name="removerecipe"),
    path('viewsapi/',Viewsapi.as_view(),name='Viewsapi'),
    path('createapi/',Createapi.as_view(),name='Createapi'),
    path('updateapi/<int:recipe_id>',Updateapi.as_view(),name='Updateapi'),
    path('deleteapi/<int:recipe_id>',Deleteapi.as_view(),name='Deleteapi'),
]