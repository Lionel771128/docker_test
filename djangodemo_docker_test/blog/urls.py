from django.urls import path
from .views import post_list,post_form,post_record, add_record

urlpatterns = [
    path("",post_list,name="post_list"),
    # path("",post_form,name="post_form"),
    path("add_record", add_record,name="add_record"),
    path("<int:id>",post_record, name='post_record'),
]