from user_app.views import utilisateurAPIView


from django.urls import path,include
from rest_framework import routers
router=routers.DefaultRouter()

router.register(r'api/utilisateur', utilisateurAPIView)

urlpatterns = [
    path('', include(router.urls)),  # Inclure les URLs du routeur
]