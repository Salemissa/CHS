import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CHS_Modele.settings')
django.setup()

from django.utils.timezone import now
from CHS_Modele_off.models import CHSModel

def insert_20_dossiers():
    sample_data = [
        {
            'num_dossier': f'CHS-{i:03d}',
            'nom': f'Personne {i}',
            'quartier': 'Quartier B',
            'revenu_mensuel': 'moins_25000',
            'revenu_mensuelle': 15000.00,
            'wilaya': 'nouakchott_ouest',
            'moughataa': 'tevragh_zeina',
            'nni': f'9876543210{i:02d}',
            'age': 25 + i,
            'sexe': 'homme' if i % 2 == 0 else 'femme',
            'situation_matrimoniale': 'marie',
            'role': 'chef_menage',
            'situation_de_vie': 'famille_non_parente',
            'tel': 'oui',
            'enf05': i % 4,
            'Orphelins_dans_le_ménage': i % 3,
            'personne_a_charge': i % 5,
            'hab_type': 'zinc',
            'pieces': '1_2',
            'propriete': 'prete',
            'eclairage': 'bougie',
            'eau': 'puits',
            'latrine': 'non',
            'emploi': 'sans_emploi',
            'nature_emploi': '',
            'raison_chomage': 'chomage',
            'soutien': 'autres',
            'foncier': 'neant',
            'camelins': 0,
            'bovins': 1,
            'ovins': 2,
            'malades': 1,
            'handicapes': 0,
            'poly': 0,
            'score': 0,
            'decision': 'Non indigent',
            'date_jour': now().date()
        }
        for i in range(1, 21)
    ]

    for data in sample_data:
        dossier = CHSModel(**data)
        dossier.save()

if __name__ == "__main__":
    insert_20_dossiers()