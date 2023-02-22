from django.urls import include, path
from rest_framework import routers
from users.views import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)

#/users  ~ get 
#/users/{id} ~ get by id
#/users/   post
#/users/ put
#/users/id/ delete
urlpatterns = [
    path('', include(router.urls)),
]
