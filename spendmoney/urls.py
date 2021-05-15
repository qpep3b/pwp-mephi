from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(),name='login'),
    path('app',views.index,name='index'),
    path('add_income',views.add_income,name='add_income'),
    path('add_expense',views.add_expense,name='add_expense'),
    path('graph_points', views.graph_points),
    path('pie_graph', views.pie_graph),
    path('accounts/',include('django.contrib.auth.urls')),
    path('logout',views.logout_view,name='logout'),
    path('sign_up',views.sign_up,name="sign up")
]