from django.urls import path
import Pages.views

urlpatterns=[
    path("pag/<str:slug>", Pages.views.PageReq, name="PagePy")
]