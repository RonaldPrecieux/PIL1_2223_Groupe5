from django.contrib import admin
from showtimeplan.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'Email') # liste les champs que nous voulons sur l'affichage de la liste
admin.site.register(User, UserAdmin) # nous modifions cette ligne, en ajoutant un deuxième argument
