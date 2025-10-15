from django.contrib import admin
from .models import CHSModel,Utilisateur

@admin.register(CHSModel)
class CHSModelAdmin(admin.ModelAdmin):
    list_display = ('nom', 'nni', 'sexe','situation_matrimoniale', 'quartier', 'revenu_mensuelle', 'score', 'decision', 'date_jour')
    search_fields = ['nom', 'nni']
    ordering = ['-date_jour']
    readonly_fields=('score','decision','num_dossier')

    def save_model(self, request, obj, form, change):
        obj.get_next_num_dossier()
        obj.calculate_score()  # Appeler la méthode pour calculer le score et la décision
        super().save_model(request, obj, form, change)
 



@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ['username', 'email']
    ordering = ['username']
    readonly_fields=('password',)
