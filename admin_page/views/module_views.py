
from django.contrib.auth.models import User
from django.utils import timezone
from .module_log import *
from django.core.exceptions import ObjectDoesNotExist
from .module_admin import (
    checkmdp
)

from upload.models import (
    RefEtudes,
    JonctionUtilisateurEtude,
    RefEtapeEtude,
    RefInfocentre,
    JonctionEtapeSuivi,
    SuiviUpload,
    DossierUpload
)


def gestionetape(dict_etape_nom, dict_etape_value, nbr_etape):
    if len(dict_etape_nom) == 0 or len(dict_etape_value) != nbr_etape:
        if len(dict_etape_value) != nbr_etape:
            nw_dict = {
                "Aucune_etape": "Une erreur sur les étapes lors de l'enregistrement de ces données ont été relevé"
            }
            error = True
        else:
            nw_dict = {
                "Aucune_etape": "Aucune étape enregistré dans les bases de données"
            }
            error = True

        return [error, nw_dict]
    else:
        etape_etude = dict_etape_value
        error = False

        return [error, etape_etude]


def etudeRecente(etude_recente, dossier_all):
    list_centre = []
    try:
        for inf in dossier_all:
            item = RefInfocentre.objects.get(user=inf.user.id)
            if item not in list_centre:
                list_centre.append(item)
    except ObjectDoesNotExist:
        indic_error = "erreur"
    return list_centre


def etudeTris(dossier_all):
    list_centre = []
    for inf in dossier_all:
        item = RefInfocentre.objects.get(user=inf.user.id)
        if item not in list_centre:
            list_centre.append(item)
    return list_centre


def gestionEtudeRecente(etude_recente, dossier_all, list_centre):
    list_etude = RefEtudes.objects.all()
    str_etude = []
    str_centre = []
    str_dict = {}

    for centre in list_centre:

        str_dict_centre = {}
        str_dict_centre["id"] = centre.id
        str_dict_centre["nom"] = str(centre.nom) + str(centre.numero)
        str_centre.append(str_dict_centre)

    for etude in list_etude:
        str_dict = {}

        try:
            var_id = etude_recente.etude.etude.id
        except:
            var_id = -1

        if etude.id == var_id:
            str_dict["id"] = str(etude.id)
            str_dict["option"] = "selected"
            str_dict["nom"] = etude.nom
            str_etude.append(str_dict)
        else:
            str_dict["id"] = str(etude.id)
            str_dict["option"] = ""
            str_dict["nom"] = etude.nom
            str_etude.append(str_dict)
    return [str_centre, str_etude]


def gestionEtudeTris(etude_change, dossier_all, list_centre):
    list_etude = RefEtudes.objects.all()
    str_etude = []
    str_centre = []
    str_dict = {}

    for centre in list_centre:

        str_dict_centre = {}
        str_dict_centre["id"] = centre.id
        str_dict_centre["nom"] = str(centre.nom) + str(centre.numero)
        str_centre.append(str_dict_centre)

    for etude in list_etude:
        str_dict = {}
        if etude.id == etude_change.id:
            str_dict["id"] = str(etude.id)
            str_dict["option"] = "selected"
            str_dict["nom"] = etude.nom
            str_etude.append(str_dict)
        else:
            str_dict["id"] = str(etude.id)
            str_dict["option"] = ""
            str_dict["nom"] = etude.nom
            str_etude.append(str_dict)
    return [str_centre, str_etude]


def dictUpload(dict_upload, files):
    nbr_files = SuiviUpload.objects.filter(
        dossier=files.dossier.id
    ).count()
    name_etude = SuiviUpload.objects.filter(dossier=files.dossier.id)[
        :1
    ]
    var_qc = DossierUpload.objects.get(id=name_etude[0].dossier.id)

    dict_upload["id_"] = files.id
    dict_upload["Etudes"] = var_qc.controle_qualite.nom
    dict_upload["Etudes_id"] = var_qc.id
    dict_upload["id"] = name_etude[0].id_patient
    dict_upload["nbr_upload"] = nbr_files

    return dict_upload


def infoEtape(files):
    etape = JonctionEtapeSuivi.objects.filter(
        upload=files.dossier.id
    ).order_by("etape")
    dict_etape_value = []

    for item in etape:
        if item.etat.id == 4:
            dict_etape_value.append(
                {
                    "val_item": item.date,
                    "val_id": item.id,
                    "block": True,
                }
            )
        else:
            dict_etape_value.append(
                {
                    "val_item": item.etat.nom,
                    "val_id": item.id,
                    "block": False,
                }
            )
    return dict_etape_value


def nomEtape(etude_recente):
    nom_etape = RefEtapeEtude.objects.filter(etude=etude_recente.id)
    dict_etape_nom = []

    for nom in nom_etape:
        dict_etape_nom.append(nom.nom)
    return dict_etape_nom


def nomEtapeTris(etude_change):
    nom_etape = RefEtapeEtude.objects.filter(etude=etude_change.id)
    dict_etape_nom = []

    for nom in nom_etape:
        dict_etape_nom.append(nom.nom)
    return dict_etape_nom


def nwPassword(
    check_mdp, type, nom, numero, username, pass_first, email
):
    if check_mdp:
        nw_user = User.objects.create_user(
            username=username, password=pass_first, email=email
        )
        nw_user.save()
        if int(type) == 0:
            nw_user.is_staff = True
            nw_user.save()
        else:
            if nw_user.is_staff:
                nw_user.is_staff = False
                nw_user.save()
        if len(nom) > 0 and len(numero) > 0:
            date_now = timezone.now()
            nw_centre = RefInfocentre(
                nom=nom, numero=numero, date_ajout=date_now
            )
            nw_centre.save()
            nw_centre.user.add(nw_user)


def editPassword(
    check_mdp, type, username, pass_first, email, user_info
):
    if checkmdp:
        user_info.username = username
        user_info.email = email
        user_info.set_password(pass_first)

        user_info.save()
    else:
        user_info.username = username
        user_info.email = email

    if int(type) == 0:
        user_info.is_staff = True
    else:
        if user_info.is_staff:
            user_info.is_staff = False
    user_info.save()


def joncCentre(user_etude, etude, user_info, user_centre, centre):
    if not user_etude.exists() and int(etude) > 0:
        date_now = timezone.now()
        save_etude = RefEtudes.objects.get(pk=etude)
        nw_jonction = JonctionUtilisateurEtude.objects.create(
            user=user_info,
            etude=save_etude,
            date_autorisation=date_now,
        )
    if not user_centre.exists() and int(centre) > 0:
        date_now = timezone.now()
        save_centre = RefInfocentre.objects.get(pk=centre)
        save_centre.user.add(user_info)


def j_serial(o):
    from datetime import datetime, date

    return (
        str(o).split(".")[0]
        if isinstance(o, (datetime, date))
        else None
    )


def delAuth(type_tab, id_search, req):
    user_current = req.user
    message = ""
    if type_tab == "etude":
        user_etude = JonctionUtilisateurEtude.objects.get(
            id=id_search
        )
        verif_suivi = SuiviUpload.objects.filter(etude=user_etude)
        if not verif_suivi.exists():
            # Enregistrement du log---------------------------------
            # ------------------------------------------------------
            nom_documentaire = (
                " a supprimé l'autorisation : "
                + user_etude.etude.nom
                + " de l'utilisateur "
                + user_current.username
            )
            supprLog(req, nom_documentaire)
            # -----------------------------------------------------
            # -----------------------------------------------------
            user_etude = JonctionUtilisateurEtude.objects.get(
                id__exact=id_search
            ).delete()
            message = (
                "Suppression des autorisations ont été appliquées"
            )
        else:
            message = (
                "Suppression annulée, cet utilisateur à chargé des documents :"
                + str(len(verif_suivi))
                + " document(s) trouvés"
            )
    elif type_tab == "centre":
        verif = RefInfocentre.objects.filter(id=id_search)
        if not verif.exists():
            # Enregistrement du log--------------------------------
            # -----------------------------------------------------
            nom_documentaire = (
                " a supprimé l'autorisation : "
                + user_etude.etude.nom
                + " de l'utilisateur "
                + user_current.username
            )
            supprLog(req, nom_documentaire)
            # ----------------------------------------------------
            # ----------------------------------------------------
            verif.user.remove(id_search)
            message = "Le centre n'est plus lié à cet utilisateur"
        else:
            message = (
                "Cet utilisateur lié à ce centre a chargé des documents ("
                + str(len(verif))
                + " document(s))"
            )
    return message
