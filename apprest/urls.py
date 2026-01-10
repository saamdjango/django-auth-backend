from django.urls import path
from apprest import views

urlpatterns = [
    path("one/",views.viewone, name="one"),
    path("post/",views.post_data, name="post"),
    path("edit/<int:pk>",views.methods, name="edit"),
    # path("login/", views.login_authentication, name="login"),
    path("user/dashboard/",views.user_dashboard),
    path("staff/dashboard/",views.staff_dashboard),
    path("admin/dashboard/",views.admin_dashboard),
    path("role/",views.user_role)
]