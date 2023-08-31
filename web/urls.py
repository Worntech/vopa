from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name = "home"),
    path("signup/",views.signup,name = "signup"),
    path("signin/",views.signin,name = "signin"),
    path('logout', views.logout, name = "logout"),
    path("news/",views.news,name = "news"),
    path("newspost/",views.newspost,name = "newspost"),
    path('viewnews/<str:pk>/', views.viewnews.as_view(), name = "viewnews"),
    path('updatenews/<int:id>/', views.updatenews, name = "updatenews"),
    path('deletenews/<int:id>/', views.deletenews, name = "deletenews"),
    
    path("annouce/",views.annouce,name = "annouce"),
    path("annoucepost/",views.annoucepost,name = "annoucepost"),
    path('viewannouce/<str:pk>/', views.viewannouce.as_view(), name = "viewannouce"),
    path('updateannouce/<int:id>/', views.updateannouce, name = "updateannouce"),
    path('deleteannouce/<int:id>/', views.deleteannouce, name = "deleteannouce"),
    
    
    path("books/",views.books,name = "books"),
    path("constitution/",views.constitution,name = "constitution"),
    path("contact/",views.contact,name = "contact"),
    path("about/",views.about,name = "about"),
    path("contactpost/",views.contactpost,name = "contactpost"),
    path("contactlist/",views.contactlist,name = "contactlist"),
    path("viewcontact/<int:id>/",views.viewcontact,name = "viewcontact"),
    path('deletecontact/<int:id>/', views.deletecontact, name = "deletecontact"),
    path("uploadconstitution/",views.uploadconstitution,name = "uploadconstitution"),
    path("constitution/",views.constitution,name = "constitution"),
    path('deleteconstitution/<int:id>/', views.deleteconstitution, name = "deleteconstitution"),
    path("files/",views.files,name = "files"),
    path("filesdisplay/",views.filesdisplay,name = "filesdisplay"),
    path('deletefiles/<int:id>/', views.deletefiles, name = "deletefiles"),
    path('viewfiles/<int:id>/', views.viewfiles, name = "viewfiles"),
    path("leader/",views.leader,name = "leader"),
    
    path("subscribers/",views.subscribers,name = "subscribers"),
]