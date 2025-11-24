function calculateScore() {
    let s = 0;

    const role = document.getElementById('id_role').value;
    const sexe = document.getElementById('id_sexe').value;
    if (role === 'chef_menage') {
        s += sexe === 'homme' ? 6 : 8;
    } else if (role === 'membre') {
        s += 3;
    }

    const situation_de_vie = document.getElementById('id_situation_de_vie').value;
    if (situation_de_vie === 'famille_parente') {
        s += 5;
    } else if (situation_de_vie === 'famille_non_parente') {
        s += 8;
    } else if (situation_de_vie === 'seul_errant') {
        s += 10;
    }

    const tel = document.getElementById('id_tel').value;
    s += tel === 'oui' ? 1 : 5;

    const enf05 = parseInt(document.getElementById('id_enf05').value) || 0;
    s += enf05 * 1;

    const orphelins = parseInt(document.getElementById('id_Orphelins_dans_le_ménage').value) || 0;
    s += orphelins * 2;

    const personne_a_charge = parseInt(document.getElementById('id_personne_a_charge').value) || 0;
    s += personne_a_charge * 1;

    const hab_type = document.getElementById('id_hab_type').value;
    if (hab_type === 'tente') {
        s += 8;
    } else if (['hangar', 'baraque'].includes(hab_type)) {
        s += 6;
    } else if (hab_type === 'banco') {
        s += 5;
    } else if (hab_type === 'zinc') {
        s += 3;
    } else if (hab_type === 'beton') {
        s += 2;
    }

    const pieces = document.getElementById('id_pieces').value;
    if (pieces === '1_2') {
        s += 4;
    } else if (pieces === '3_4') {
        s += 1;
    }

    const propriete = document.getElementById('id_propriete').value;
    if (propriete === 'prete') {
        s += 4;
    } else if (propriete === 'location') {
        s += 2;
    } else if (propriete === 'proprietaire') {
        s += 1;
    }

    const eclairage = document.getElementById('id_eclairage').value;
    if (eclairage === 'bougie') {
        s += 4;
    } else if (eclairage === 'electricite') {
        s += 1;
    }

    const eau = document.getElementById('id_eau').value;
    if (eau === 'adduction') {
        s += 0;
    } else if (eau === 'reserve') {
        s += 2;
    } else if (eau === 'charrette') {
        s += 4;
    } else if (eau === 'puits') {
        s += 6;
    }

    const latrine = document.getElementById('id_latrine').value;
    s += latrine === 'oui' ? 2 : 6;

    const emploi = document.getElementById('id_emploi').value;
    if (emploi === 'emploi') {
        const nature_emploi = document.getElementById('id_nature_emploi').value;
        if (nature_emploi === 'fixe') {
            s += 0;
        } else if (nature_emploi === 'temporaire') {
            s += 4;
        } else if (nature_emploi === 'saisonnier') {
            s += 6;
        }
        const revenu_mensuel = document.getElementById('id_revenu_mensuel').value;
        if (revenu_mensuel === 'moins_25000') {
            s += 6;
        } else if (revenu_mensuel === '25k_30k') {
            s += 3;
        }
    } else {
        const raison_chomage = document.getElementById('id_raison_chomage').value;
        if (raison_chomage === 'incapacite') {
            s += 10;
        } else if (raison_chomage === 'chomage') {
            s += 6;
        }
    }

    const soutien = document.getElementById('id_soutien').value;
    if (soutien === 'proche') {
        s += 6;
    } else if (soutien === 'autres') {
        s += 10;
    }

    const foncier = document.getElementById('id_foncier').value;
    if (foncier === 'commercial') {
        s += 0;
    } else if (foncier === 'agricole') {
        s += 2;
    } else if (foncier === 'habitation') {
        s += 4;
    } else if (foncier === 'neant') {
        s += 8;
    }

    const camelins = parseInt(document.getElementById('id_camelins').value) || 0;
    if (camelins === 0) {
        s += 5;
    } else if (camelins >= 1 && camelins <= 4) {
        s += 2;
    } // 5+ : 0

    const bovins = parseInt(document.getElementById('id_bovins').value) || 0;
    if (bovins === 0) {
        s += 6;
    } else if (bovins >= 1 && bovins <= 3) {
        s += 3;
    } else if (bovins >= 4 && bovins <= 5) {
        s += 2;
    } // 6+ : 0

    const ovins = parseInt(document.getElementById('id_ovins').value) || 0;
    if (ovins >= 0 && ovins <= 2) {
        s += 10;
    } else if (ovins >= 3 && ovins <= 5) {
        s += 6;
    } else if (ovins >= 6 && ovins <= 10) {
        s += 2;
    } // 11+ : 0

    const malades = parseInt(document.getElementById('id_malades').value) || 0;
    s += malades * 2;

    const handicapes = parseInt(document.getElementById('id_handicapes').value) || 0;
    s += handicapes * 2;

    const poly = parseInt(document.getElementById('id_poly').value) || 0;
    s += poly * 4;

    // Update display
    document.getElementById('score').textContent = s;
    const decisionEl = document.getElementById('decision');
    if (s > 90) {
        decisionEl.textContent = 'Indigent • فقير مستحق';
        decisionEl.className = 'status bad';
    } else {
        decisionEl.textContent = 'Non indigent • غير فقير';
        decisionEl.className = 'status ok';
    }
}

// Add event listeners to all inputs
document.addEventListener('DOMContentLoaded', function() {
    const inputs = document.querySelectorAll('input, select');
    inputs.forEach(input => {
        input.addEventListener('input', calculateScore);
        input.addEventListener('change', calculateScore);
    });
    // Initial calculation
    calculateScore();
});