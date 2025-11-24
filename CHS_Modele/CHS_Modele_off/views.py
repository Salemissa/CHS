from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import CHSModel
from .forms import CHSModelForm
import datetime
import json
from django.contrib.auth import authenticate, login, logout

def login_page(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            if not username or not password:
                messages.warning(request, 'Veuillez remplir tous les champs.')
                return render(request, 'auth/login.html')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('chs_dash')  # Rediriger vers la page d'accueil après la connexion
            else:
                messages.warning(request, 'Identifiants invalides. Veuillez réessayer.')
        # For GET requests or if authentication fails, render the login form
        return render(request, 'auth/login.html')
    except Exception as e:
        messages.error(request, f'Une erreur inattendue s\'est produite : {str(e)}')
        return render(request, 'auth/login.html')

def logout_user(request):
    logout(request)
    messages.info(request, 'Vous avez été déconnecté avec succès.')
    return redirect('login_page')

@login_required
def chs_dash(request):
    chs_queryset = CHSModel.objects.all().order_by('-date_jour')
    total_dossiers = chs_queryset.count()
    total_indigents = chs_queryset.filter(decision__icontains='Indigent • فقير مستحق').count()
    total_non_indigents = chs_queryset.filter(decision__icontains='Non indigent').count()

    score_moyenne = chs_queryset.aggregate(avg_score=Avg('score'))['avg_score'] or 0
    score_moyenne = round(score_moyenne, 2) if score_moyenne else 0

    taux_indigence = round((total_indigents / total_dossiers) * 100, 2) if total_dossiers else 0

    chs_page = None
    if total_dossiers:
        paginator = Paginator(chs_queryset, 10)
        page = request.GET.get('page')

        try:
            chs_page = paginator.page(page)
        except PageNotAnInteger:
            chs_page = paginator.page(1)
        except EmptyPage:
            chs_page = paginator.page(paginator.num_pages)

    indigents_par_wilaya = (
        CHSModel.objects.filter(decision__icontains='Indigent')
        .values('wilaya')
        .annotate(total=Count('id'))
        .order_by('-total')
    )

    wilaya_counts = []
    for entry in indigents_par_wilaya:
        label = dict(CHSModel.WILAYA_CHOICES).get(entry['wilaya'], entry['wilaya'])
        wilaya_counts.append({'wilaya': label, 'total': entry['total']})

    return render(request, 'CHS_DASH.html', {
        'chs_page': chs_page,
        'total_dossiers': total_dossiers,
        'total_indigents': total_indigents,
        'total_non_indigents': total_non_indigents,
        'score_moyenne': score_moyenne,
        'taux_indigence': taux_indigence,
        'indigents_par_wilaya': json.dumps(wilaya_counts)
    })

@login_required(login_url='login_page')
def create_chs(request):
    try:
        if request.method == 'POST':
            form = CHSModelForm(request.POST)
            if form.is_valid():
                try:
                    chs = form.save(commit=False)
                    chs.save()  # This will generate num_dossier if needed and calculate score
                    # Vérification de l'enregistrement
                    if chs.pk and chs.score > 0 and chs.num_dossier:
                        messages.success(request, f'Modèle CHS créé avec succès. Numéro: {chs.num_dossier}, Score: {chs.score}.')
                    else:
                        messages.error(request, 'Erreur lors de la création ou du calcul.')
                    return redirect('chs_dash')
                except Exception as e:
                    messages.error(request, f'Une erreur est survenue lors de la sauvegarde : {str(e)}')
            else:
                messages.warning(request, 'Veuillez vérifier les informations saisies.')
        else:
            form = CHSModelForm()
            # Générer un aperçu du numéro de dossier depuis le backend
            try:
                preview_num = CHSModel.get_next_num_dossier()
            except Exception as e:
                preview_num = 'Erreur lors de la génération'
                messages.error(request, f'Une erreur est survenue lors de la génération du numéro de dossier : {str(e)}')
            today_date = datetime.date.today().strftime('%d/%m/%Y')
        return render(request, 'CHS_FOR_OFF.html', {'form': form, 'preview_num': preview_num, 'today_date': today_date})
    except Exception as e:
        messages.error(request, f'Une erreur inattendue s\'est produite : {str(e)}')
        return redirect('chs_dash')



@login_required(login_url='login_page')
def Statistique (request):
    indigents_par_wilaya = (
        CHSModel.objects.filter(decision__icontains='Indigent')
        .values('wilaya')
        .annotate(total=Count('id'))
        .order_by('-total')
    )

    wilaya_counts = []

    for entry in indigents_par_wilaya:
        label = dict(CHSModel.WILAYA_CHOICES).get(entry['wilaya'], entry['wilaya'])
        wilaya_counts.append({'wilaya': label, 'total': entry['total']})

    return render(request, 'Statistique.html', {
        'indigents_par_wilaya': json.dumps(wilaya_counts)
    })