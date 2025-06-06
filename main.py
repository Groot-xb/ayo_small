from flask import Flask, render_template
from threading import Thread
import time
import json
import os
import importlib.util
 
# === FLASK INITIALISATION ===
app = Flask(__name__)

@app.route("/")
def status():
    return render_template("index.html", uid=UID, statut=statut_utilisateur)

def start_server():
    app.run(host="0.0.0.0", port=5678)

UID = "AUCUN"
statut_utilisateur = "inconnu"
autorisation_aaron = {}
phrases_securite = []
defcon_status = 0

try:
    with open(os.path.join("memory_core", "core_identity.json"), "r") as f:
        identite = json.load(f)
        UID = identite.get("uid", UID)
        statut_utilisateur = identite.get("statut", statut_utilisateur)
        autorisation_aaron = identite.get("profils_biologiques", {}).get("aaron", {})
        phrases_securite = identite.get("regles_de_validation", {}).get("phrase_securite", [])
except:
    print("[⚠️ AVERTISSEMENT] Fichier d'identité introuvable ou invalide.")

try:
    with open(os.path.join("07_watchdog", "status_defcon.json"), "r") as f:
        defcon_status = json.load(f).get("niveau_actuel", 0)
except:
    defcon_status = 0

try:
    spec = importlib.util.spec_from_file_location("core_profiles", os.path.join("logs_core", "boot", "sessions", "core_profiles.py"))
    profiles_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(profiles_module)
    profils_systeme = profiles_module.PROFILS_SYSTEME
except:
    profils_systeme = {}
    print("[⚠️ AVERTISSEMENT] core_profiles.py non chargé (profils non reconnus)")

if UID == "ALPHA_BETA_GAMMA":
    print("🔐 Créateur légitime reconnu : contrôle absolu activé.")

session_active = True

# === SECTION 2 — SURVEILLANCE SYSTEME ===
reflexe_counter = 0

def verifier_phrase_securite(entree_utilisateur: str):
    for phrase in phrases_securite:
        if phrase.strip().lower() in entree_utilisateur.strip().lower():
            print(f"[🔐 PHRASE SÉCURITÉ DÉTECTÉE] : '{phrase}' → déclenchement d'autorité !")
            return True
    return False

def boucle_reflexe():
    global reflexe_counter
    while session_active:
        reflexe_counter += 1
        print(f"[REFLEXE] Vérification de l’environnement… 🌀 Réflexe #{reflexe_counter}")
        time.sleep(30)

Thread(target=boucle_reflexe, daemon=True).start()

# === SECTION 3 — FONCTIONS INTELLIGENTES ===
def supervision_agents(): print("[4.0] Supervision agents / périphériques")
def dialogue_vocal(): print("[5.0] Dialogue vocal / TTS")
def traitement_multimodal(): print("[6.0] Traitement image ou vision")
def analyse_emotionnelle(): print("[7.0] Profil émotionnel analysé")
def appel_ia_secondaire(): print("[8.0] Appel IA secondaire via Docker/API")
def surveillance_iot(): print("[9.0] Surveillance capteurs ou IoT")
def archivage(): print("[10.0] Archivage déclenché")
def alerte_thermique(): print("[12.0] Alerte thermique / batterie / stockage")
def etat_agent(): print(f"[13.0] UID: {UID} | Statut: {statut_utilisateur} | DEFCON: {defcon_status}")
def reboot(): print("[14.0] Reboot manuel ou programmé")
def protocole_urgence():
    if UID != "ALPHA_BETA_GAMMA":
        print("[⛔ REFUS] Protocole d’urgence bloqué.")
        return
    print("[15.0] Protocole d’urgence → shutdown + backup")
def traitement_parallele(): print("[16.0] Traitement parallèle (n8n/thread)")
def apprentissage(): print("[17.0] Fine-tuning / apprentissage local")
def commande_docker(): print("[18.0] Commande Docker externe")
def maj_interne(): print("[19.0] Vérification mise à jour interne")
def blocage_comportement(): print("[20.0] Filtrage comportemental actif")
def simulation_dualite(): print("[21.0] Mode miroir (co-agent)")
def mode_veille(): print("[22.0] Mise en veille automatique")
def adaptation_contexte(): print("[23.0] Ambiance sonore adaptative")
def journalisation(): print("[24.0] Journalisation vocale/interface")
def gestion_memoire(): print("[MEMOIRE] Bloc mémoire pas encore codé mais déclenché")
def debug_session(): print("[DEBUG] Bloc debug actif — aucune action encore définie")

def etat_synthese():
    print(f"\n[🔎 ÉTAT] UID={UID} — STATUT={statut_utilisateur} — DEFCON={defcon_status}\n")

# === SECTION 4 — INTERACTION INITIALE ===
print("AyO Small est prêt. Activation automatique (mode Docker).")
reponse = "oui"

# ⚠️ Lance le serveur Flask uniquement après confirmation
Thread(target=start_server, daemon=True).start()

print(f"Activation acceptée. UID : {UID}, Rôle : {statut_utilisateur}")

# === SECTION 5 — BOUCLE PRINCIPALE ===
def main():
    print("Terminal prêt. Tape une commande ou 'exit' pour quitter.")
    while session_active:
        try:
            cmd = input(">>> ")
            if verifier_phrase_securite(cmd):
                print("[⚠️] Phrase de sécurité détectée.")
                continue
            analyser_commande(cmd)
        except KeyboardInterrupt:
            print("\nInterruption manuelle détectée.")
            break

# === SECTION 6 — ANALYSE COMMANDE ===
def analyser_commande(cmd: str):
    cmd_lower = cmd.lower()
    if statut_utilisateur == "enfant" and any(bloc in cmd_lower for bloc in autorisation_aaron.get("blocs_interdits", [])):
        print("[REFUS] Commande interdite pour ton profil.")
        return

    if "état" in cmd_lower: etat_synthese()
    elif "peripherique" in cmd_lower: supervision_agents()
    elif "vocal" in cmd_lower: dialogue_vocal()
    elif "vision" in cmd_lower: traitement_multimodal()
    elif "emotion" in cmd_lower: analyse_emotionnelle()
    elif "ia secondaire" in cmd_lower: appel_ia_secondaire()
    elif "capteur" in cmd_lower: surveillance_iot()
    elif "archive" in cmd_lower: archivage()
    elif "thermique" in cmd_lower: alerte_thermique()
    elif "mémoire" in cmd_lower: gestion_memoire()
    elif "debug" in cmd_lower: debug_session()
    elif "reboot" in cmd_lower: reboot()
    elif "urgence" in cmd_lower: protocole_urgence()
    elif "parallèle" in cmd_lower: traitement_parallele()
    elif "apprentissage" in cmd_lower: apprentissage()
    elif "docker" in cmd_lower: commande_docker()
    elif "mise à jour" in cmd_lower: maj_interne()
    elif "comportement" in cmd_lower: blocage_comportement()
    elif "social" in cmd_lower or "co-agent" in cmd_lower: simulation_dualite()
    elif "veille" in cmd_lower: mode_veille()
    elif "adaptation" in cmd_lower: adaptation_contexte()
    elif "journal" in cmd_lower: journalisation()
    elif "status" in cmd_lower: etat_synthese()
    elif "workflow" in cmd_lower or "liste" in cmd_lower:
        print("[LISTE] Blocs disponibles : 4.0 → 30.0")
    else:
        print(f"Commande reçue : '{cmd}' — inconnue.")

if __name__ == "__main__":
    main()
