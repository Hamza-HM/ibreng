from ibreng.fitness.views import ExcerciseViewSet, SetViewSet, WorkoutViewSet

from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from ibreng.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("sets", SetViewSet)
router.register("exercices", ExcerciseViewSet)
router.register("workouts", WorkoutViewSet)


app_name = "api"
urlpatterns = router.urls
