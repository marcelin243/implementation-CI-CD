from .serialisers import utilisateurSerializers
from .models import utilisateur
from rest_framework import viewsets

#  VIEWS POUR USER MONITEUR TYPE
#===============================
class utilisateurAPIView(viewsets.ModelViewSet):
    queryset = utilisateur.objects.all().order_by('nom')
    serializer_class=utilisateurSerializers
