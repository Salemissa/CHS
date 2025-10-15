from django.db import models
from django.contrib.auth.models import AbstractUser
class Utilisateur(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        verbose_name='permissions spécifiques'
    )
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        verbose_name='groupes spécifiques'
    )

    def __str__(self):
        return self.username

class CHSModel(models.Model):
    # Informations personnelles
    num_dossier = models.CharField(max_length=50, unique=True, verbose_name="Numéro de dossier")
    nom = models.CharField(max_length=255, verbose_name="Nom et prénom")
    quartier = models.CharField(max_length=255, verbose_name="Quartier")
    REVENU_CHOICES = [
        ('moins_25000', '< 25 000 UM'),
        ('25k_30k', '25 000–30 000 UM'),
        ('plus_31k', '>= 31 000 UM'),
    ]
    revenu_mensuel = models.CharField(max_length=20, choices=REVENU_CHOICES, blank=True, verbose_name="Montant mensuel", default='')
    revenu_mensuelle = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Revenu mensuelle (UM)")
    WILAYA_CHOICES = [
        ('adrar', 'Adrar'),
        ('assaba', 'Assaba'),
        ('brakna', 'Brakna'),
        ('dakhlet_nouadhibou', 'Dakhlet Nouadhibou'),
        ('gorgol', 'Gorgol'),
        ('guidimaka', 'Guidimaka'),
        ('hodh_ech_chargui', 'Hodh Ech Chargui'),
        ('hodh_el_gharbi', 'Hodh El Gharbi'),
        ('inchiri', 'Inchiri'),
        ('nouakchott_nord', 'Nouakchott Nord'),
        ('nouakchott_ouest', 'Nouakchott Ouest'),
        ('nouakchott_sud', 'Nouakchott Sud'),
        ('tagant', 'Tagant'),
        ('tiris_zemmour', 'Tiris Zemmour'),
        ('trarza', 'Trarza'),
    ]
    wilaya = models.CharField(max_length=50, choices=WILAYA_CHOICES, blank=True, verbose_name="Wilaya")

    MOUGHATAA_CHOICES = [
        ('nouakchott', 'Nouakchott'),
        ('boutilimit', 'Boutilimit'),
        ('kaedi', 'Kaédi'),
        ('selibaby', 'Sélibaby'),
        ('aioun', 'Aioun'),
        ('atâr', 'Atâr'),
        ('ouadane', 'Ouadane'),
        ('chinguetti', 'Chinguetti'),
        ('oualata', 'Oualata'),
        ('tidjikja', 'Tidjikja'),
        ('nema', 'Néma'),
        ('timbedra', 'Timbedra'),
        ('kiffa', 'Kiffa'),
        ('magta_lahjar', 'Magta-Lahjar'),
        ('boghe', 'Boghé'),
        ('bababe', 'Bababé'),
        ('mbagne', 'Mbagne'),
        ('alekh', 'Aleg'),
        ('mederdra', 'Mederdra'),
        ('akjoujt', 'Akjoujt'),
        ('tevragh_zeina', 'Tevragh-Zeina'),
        ('rosso', 'Rosso'),
        ('keur_massene', 'Keur Massène'),
        ('riyad', 'Riyad'),
        ('lexeiba', 'Lexeiba'),
        ('nouadhibou', 'Nouadhibou'),
        ('adre', 'Adre'),
        ('monguel', 'Monguel'),
        ('djiguenni', 'Djiguenni'),
        ('amakhtiar', 'Amakhtiar'),
        ('moudjeria', 'Moudjeria'),
        ('timbedgha', 'Timbedgha'),
        ('barkeol', 'Barkéol'),
        ('guerou', 'Guérou'),
        ('diadjibine_semme', 'Diadjibine-Semmé'),
        ('oudalan', 'Oudalan'),
        ('sori_mal', 'Sori-Mal'),
        ('aghchorguit', 'Aghchorguit'),
        ('fderik', 'Fderik'),
        ('bir_moghrein', 'Bir Moghrein'),
        ('zoueratt', 'Zoueratt'),
        ('tichitt', 'Tichitt'),
        ('mbera', 'Mbera'),
        ('rachid', 'Rachid'),
        ('oumpouere', 'Oumpouere'),
        ('jinah', 'Jinah'),
        ('el_mina', 'El Mina'),
        ('dar_naim', 'Dar Naïm'),
        ('toujouonine', 'Toujouonine'),
        ('kobenni', 'Kobenni'),
        ('barrage', 'Barrage'),
        ('sebkha', 'Sebkha'),
    ]
    moughataa = models.CharField(max_length=50, choices=MOUGHATAA_CHOICES, blank=True, verbose_name="Moughataa")

    nni = models.CharField(max_length=10, verbose_name="NNI", blank=True, unique=True)
    age = models.IntegerField(verbose_name="Âge")



    sexe_CHOICES = [
        ('homme', 'Homme'),
        ('femme', 'Femme'),
    ]
    sexe = models.CharField(max_length=10, choices=sexe_CHOICES,default='homme', verbose_name="Sexe")
    
    Situation_matrimoniale_choices = [
        ('marie', 'Marié(e)'),
        ('celibataire', 'Celibataire'),
        ('veuf_veuve', 'Veuf/Veuve'),
        ('divorce_separe', 'Divorcé/Separé'),
    ]
    situation_matrimoniale = models.CharField(max_length=20, choices=Situation_matrimoniale_choices,default='celibataire', verbose_name="Situation matrimoniale")

    # Conditions sociales et familiales
    ROLE_CHOICES = [
        ('chef_menage', 'Chef de ménage '),
        ('membre', 'Membre'),
        ('autre', 'Autre'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, verbose_name="Statut dans le ménage")

    situation_de_vie_CHOICES = [
        ('famille_parente', 'Avec parenté directe'),
        ('famille_non_parente', 'Sans parenté directe'),
        ('seul_errant', 'Seul / errant'),
    ]
    situation_de_vie = models.CharField(max_length=20, choices=situation_de_vie_CHOICES, verbose_name="Situation de cohabitation")

    TEL_CHOICES = [
        ('oui', 'Oui'),
        ('non', 'Non'),
    ]
    tel = models.CharField(max_length=3, choices=TEL_CHOICES, verbose_name="Téléphone portable")

    enf05 = models.IntegerField(default=0, verbose_name="Enfants 0-5 ans")
    Orphelins_dans_le_ménage = models.IntegerField(default=0, verbose_name="Orphelin(s)")
    personne_a_charge = models.IntegerField(default=0, verbose_name="Autres personnes à charge")

    # Habitat
    HAB_TYPE_CHOICES = [
        ('tente', 'Tente'),
        ('hangar', 'Hangar'),
        ('baraque', 'Baraque'),
        ('banco', 'Maison en banco'),
        ('zinc', 'Maison en zinc'),
        ('beton', 'Maison en béton armé'),
    ]
    hab_type = models.CharField(max_length=20, choices=HAB_TYPE_CHOICES, verbose_name="Type d'habitat")

    PIECES_CHOICES = [
        ('1_2', '1-2'),
        ('3_4', '3-4'),
        ('5p', '5 et +'),
    ]
    pieces = models.CharField(max_length=10, choices=PIECES_CHOICES, verbose_name="Nombre de pièces")

    PROPRIETE_CHOICES = [
        ('prete', 'Prêté'),
        ('location', 'Location'),
        ('proprietaire', 'Propriétaire'),
    ]
    propriete = models.CharField(max_length=20, choices=PROPRIETE_CHOICES, verbose_name="Statut de propriété")

    ECLAIRAGE_CHOICES = [
        ('bougie', 'Bougie / Lampe / Torche'),
        ('electricite', 'Électricité'),
    ]
    eclairage = models.CharField(max_length=20, choices=ECLAIRAGE_CHOICES, verbose_name="Éclairage")

    EAU_CHOICES = [
        ('adduction', "Adduction d'eau"),
        ('reserve', 'Réserve d\'eau'),
        ('charrette', 'Charrettes'),
        ('puits', 'Puits'),
    ]
    eau = models.CharField(max_length=20, choices=EAU_CHOICES, verbose_name="Approvisionnement en eau")

    LATRINE_CHOICES = [
        ('oui', 'Oui'),
        ('non', 'Non'),
    ]
    latrine = models.CharField(max_length=3, choices=LATRINE_CHOICES, verbose_name="Latrines")

    EMPLOI_CHOICES = [
        ('emploi', 'Ayant un emploi'),
        ('sans_emploi', 'Sans emploi'),
    ]
    emploi = models.CharField(max_length=20, choices=EMPLOI_CHOICES, default='sans_emploi', verbose_name="Situation")

    NATURE_EMPLOI_CHOICES = [
        ('fixe', 'Fixe'),
        ('temporaire', 'Temporaire'),
        ('saisonnier', 'Saisonnier'),
    ]
    nature_emploi = models.CharField(max_length=20, choices=NATURE_EMPLOI_CHOICES, blank=True, verbose_name="Nature de l'emploi")

   

    RAISON_CHOMAGE_CHOICES = [
        ('incapacite', 'Incapacité à travailler'),
        ('chomage', 'Chômage'),
    ]
    raison_chomage = models.CharField(max_length=20, choices=RAISON_CHOMAGE_CHOICES, blank=True, verbose_name="Motif")

    SOUTIEN_CHOICES = [
        ('proche', 'Proche parent'),
        ('autres', 'Voisins / autres'),
    ]
    soutien = models.CharField(max_length=20, choices=SOUTIEN_CHOICES, verbose_name="Principal soutien de la famille")

    # Avoirs fonciers
    FONCIER_CHOICES = [
        ('commercial', 'Commercial'),
        ('agricole', 'Agricole'),
        ('habitation', 'Pour habitation'),
        ('neant', 'Néant'),
    ]
    foncier = models.CharField(max_length=20, choices=FONCIER_CHOICES, verbose_name="Type")

    # Avoirs pastoraux
    camelins = models.IntegerField(default=0, verbose_name="Chameaux")
    bovins = models.IntegerField(default=0, verbose_name="Bovins")
    ovins = models.IntegerField(default=0, verbose_name="Ovins/Caprins")

    # Santé
    malades = models.IntegerField(default=0, verbose_name="Malades de longue durée")
    handicapes = models.IntegerField(default=0, verbose_name="Personnes handicapées")
    poly = models.IntegerField(default=0, verbose_name="Polyhandicapés")

    # Calculés
    score = models.IntegerField(default=0, verbose_name="Score total")
    decision = models.CharField(max_length=50, verbose_name="Décision")

    # Métadonnées
    date_jour = models.DateField(auto_now_add=True, verbose_name="Date")

    @property
    def wilaya_label(self):
        return dict(self.WILAYA_CHOICES).get(self.wilaya, self.wilaya)

    def calculate_score(self):
        s = 0
        if self.role == 'chef_homme':
            s += 6
        elif self.role == 'chef_femme':
            s += 8
        elif self.role == 'membre':
            s += 3

        if self.situation_de_vie == 'famille_parente':
            s += 5
        elif self.situation_de_vie == 'famille_non_parente':
            s += 8
        elif self.situation_de_vie == 'seul_errant':
            s += 10

        s += 1 if self.tel == 'oui' else 5

        s += self.enf05 * 1
        s += self.Orphelins_dans_le_ménage * 2
        s += self.personne_a_charge * 1

        if self.hab_type == 'tente':
            s += 8
        elif self.hab_type in ['hangar', 'baraque']:
            s += 6
        elif self.hab_type == 'banco':
            s += 5
        elif self.hab_type == 'zinc':
            s += 3
        elif self.hab_type == 'beton':
            s += 2

        if self.pieces == '1_2':
            s += 4
        elif self.pieces == '3_4':
            s += 1

        if self.propriete == 'prete':
            s += 4
        elif self.propriete == 'location':
            s += 2
        elif self.propriete == 'proprietaire':
            s += 1

        if self.eclairage == 'bougie':
            s += 4
        elif self.eclairage == 'electricite':
            s += 1

        if self.eau == 'adduction':
            s += 0
        elif self.eau == 'reserve':
            s += 2
        elif self.eau == 'charrette':
            s += 4
        elif self.eau == 'puits':
            s += 6

        if self.latrine == 'oui':
            s += 2
        elif self.latrine == 'non':
            s += 6

        if self.emploi == 'emploi':
            if self.nature_emploi == 'fixe':
                s += 0
            elif self.nature_emploi == 'temporaire':
                s += 4
            elif self.nature_emploi == 'saisonnier':
                s += 6
            if self.revenu_mensuel == 'moins_25000':
                s += 6
            elif self.revenu_mensuel == '25k_30k':
                s += 3
        else:
            if self.raison_chomage == 'incapacite':
                s += 10
            elif self.raison_chomage == 'chomage':
                s += 6

        if self.soutien == 'proche':
            s += 6
        elif self.soutien == 'autres':
            s += 10

        if self.foncier == 'commercial':
            s += 0
        elif self.foncier == 'agricole':
            s += 2
        elif self.foncier == 'habitation':
            s += 4
        elif self.foncier == 'neant':
            s += 8

        if self.camelins == 0:
            s += 5
        elif 1 <= self.camelins <= 4:
            s += 2

        if self.bovins == 0:
            s += 6
        elif self.bovins <= 3:
            s += 3
        elif self.bovins <= 5:
            s += 2

        if self.ovins <= 2:
            s += 10
        elif self.ovins <= 5:
            s += 6
        elif self.ovins <= 10:
            s += 2

        s += self.malades * 2
        s += self.handicapes * 2
        s += self.poly * 4

        self.score = s
        if s > 80:
            self.decision = 'Indigent • فقير مستحق'
        else:
            self.decision = 'Non indigent • غير فقير'

    @classmethod
    def get_next_num_dossier(cls):
        try:
            last = cls.objects.order_by('-id').first()
            if last and last.num_dossier.startswith('CHS-'):
                try:
                    num = int(last.num_dossier.split('-')[1]) + 1
                except ValueError:
                    num = 1
            else:
                num = 1
            return f"CHS-{num:03d}"
        except Exception as e:
            # Log the exception and return a default value
            print(f"Error generating next dossier number: {e}")
            return "CHS-000"

    def save(self, *args, **kwargs):
        try:
            if not self.num_dossier:
                self.num_dossier = self.get_next_num_dossier()
            self.calculate_score()
            super().save(*args, **kwargs)
        except Exception as e:
            # Log the exception for debugging purposes
            print(f"Error saving CHSModel instance: {e}")
            raise

    def __str__(self):
        return f"{self.nom} - {self.num_dossier}"

    class Meta:
        verbose_name = "Modèle CHS"
        verbose_name_plural = "Modèles CHS"