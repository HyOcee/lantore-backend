from django.urls import path
from ros import views
from ros.views import (
    change_password,
    delete_hotspot_user,
    get_user_connected_devices,
    get_user_stats,
    get_active_users,
    disable_user,
    fetch_data_usage,
)

urlpatterns = [
    path("ros/ping", views.RosViews.as_view({"get": "ping"})),
    path("ros/users", views.RosViews.as_view({"get": "users"})),
    path("ros/profile", views.RosViews.as_view({"post": "profile", "get": "profile"})),
    path(
        "ros/hotspot-user",
        views.RosViews.as_view({"post": "hotspot_user"}),
    ),
    path("ros/user-stats/", get_user_stats, name="user-stats"),
    path("ros/active-users/", get_active_users, name="active-user"),
    path("ros/disable-user/", disable_user, name="disable-user"),
    path("ros/data-usage/", fetch_data_usage, name="fetch_data_usage"),
    path(
        "ros/user-connected-devices/",
        get_user_connected_devices,
        name="get-user-connected-devices",
    ),
    path("ros/delete-hotspot-user", delete_hotspot_user, name="delete_hotspot_user"),
    path("ros/change-user-password", change_password, name="change_password"),
]
