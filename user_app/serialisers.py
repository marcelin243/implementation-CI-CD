from rest_framework import serializers
from .models import utilisateur

# SERIALIZERS  utilisateur
# =====================================
class utilisateurSerializers(serializers.ModelSerializer):
    class Meta:
        model=utilisateur
        fields="__all__"      