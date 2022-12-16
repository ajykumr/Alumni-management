from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('form/', views.registerform, name="form"),
    path('a/', views.BookListView.as_view(), name="formss"),
    path('form1/', views.registerform1, name="formsss"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('signin/', views.signin_page, name="signin"),
    path('success/', views.registraion_success, name="registraion_success"),
    path('account-success/', views.account_success, name="account_success"),
    path('records/', views.records, name="records"),
    path('humans.txt/', views.humanstxt, name="humanstxt"),
    path('dashboard/approved/', views.dashboard_approved, name="dashboard_approved"),
    path('dashboard/all/', views.dashboard_all, name="dashboard_all"),
    path('dashboard/rejected/', views.dashboard_rejected, name="dashboard_rejected"),
    path('dashboard/pending/', views.dashboard_pending, name="dashboard_pending"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('documentation/', views.documentation, name="documentation"),
    path('view/<str:pk>/', views.view_alumni, name="view_alumni"),
    path('view1/<str:pk>/', views.view_alumni1, name="view_alumni1"),
    path('update/<str:pk>/', views.update_alumni, name="update_alumni"),
    path('delete/<str:pk>/', views.delete_alumni, name="delete_alumni"),
    path('account/', views.accountview, name="accountView"),
    path('account/update/', views.accountUpdate, name="accountUpdate"),
]
