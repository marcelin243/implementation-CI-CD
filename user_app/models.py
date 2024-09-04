from django.db import models

# MODEL contr_moyen_payement_communes
# ==========================
class utilisateur(models.Model):
    id=models.AutoField(primary_key=True,db_column='id')
    nom=models.CharField(max_length=255,null=False,db_column="nom")
    prenom=models.CharField(max_length=100,null=False,db_column="prenom")
    adresse=models.CharField(max_length=100,null=False,db_column="adresse")
    
    class Meta:
        db_table = 'utilisateur'
         
    def __str__(self):
        return self.nom
