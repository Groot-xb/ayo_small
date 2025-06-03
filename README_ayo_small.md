# README — Agent AyO Small (local + Docker + Ollama)

## ✨ Objectif

Le dossier `D:/AYO_CORE/models_core/mistral7b_ayo_small` contient le **noyau de lancement d'AyO Small**, version initiale réflexe de l'agent intelligent AyO. Il intègre un modèle Mistral7B via Ollama, dans un conteneur Docker léger et sécurisé. L'objectif est de créer un système capable de :

* 🔊 Interagir par texte ou vocal
* 🚀 Réagir aux stimuli techniques ou contextuels (reflex\_core)
* 🌐 Exposer une interface minimale via Flask (localhost)
* 🔄 Gérer des workflows n8n et fonctions parallèles (multi-thread)
* 🧑‍💻 Préparer l'évolution vers RB1/RB2 (agent mécatronique)

---

## 📂 Structure technique (fichiers critiques)

| Fichier                   | Rôle principal                                            |
| ------------------------- | --------------------------------------------------------- |
| `main.py`                 | Interface terminal, boucle réflexe, reconnaissance UID    |
| `Dockerfile`              | Construction image Docker Python + Ollama + Flask         |
| `docker-compose.yml`      | Services Docker + volumes + ports                         |
| `.dockerignore`           | Exclusions Docker build (poids / logs / modèles externes) |
| `params.json`             | Taille du modèle (layers, heads, d\_model)                |
| `generation_config.json`  | top\_p, temp, bos/eos, repetition penalty, etc.           |
| `tokenizer_config.json`   | Mappings tokens spéciaux BOS/EOS                          |
| `special_tokens_map.json` | Configuration supérieure d'encodage                       |

---

## 📆 Volumes montés dans Docker (selon docker-compose.yml)

| Volume interne  | Dossier hôte Windows                          | Contenu / Rôle                        |
| --------------- | --------------------------------------------- | ------------------------------------- |
| `/app`          | `D:/AYO_CORE/models_core/mistral7b_ayo_small` | Code de l'agent AyO Small             |
| `/models_core`  | `D:/AYO_CORE/models_core`                     | Modèles Ollama / checkpoints          |
| `/configs_core` | `D:/AYO_CORE/config_core`                     | JSON de configuration / tokens        |
| `/logs_core`    | `D:/AYO_CORE/logs_core`                       | Journaux, traces et déclencheurs      |
| `/memory_core`  | `D:/AYO_CORE/memory_core`                     | UID, historique, identités, sessions  |
| `/results_core` | `D:/AYO_CORE/06_results`                      | Exportations, fichiers transformés    |
| `/raw_data`     | `D:/AYO_CORE/01_data_raw`                     | Données sources (audio, image, texte) |
| `/proc_data`    | `D:/AYO_CORE/02_data_proc`                    | Données prétraitées et nettoyées      |

---

## 🏛️ Fichier `main.py` (logique interne)

### 1. Initialisation

* Lancement serveur Flask (`localhost:5678`)
* Chargement fichier `core_identity.json`
* Attribution UID, rôle et niveau

### 2. Boucle réflexe

* Thread toutes les 10 secondes
* Détection anomalie, surcharge, dérives comportementales

### 3. Fonctions intelligentes

* Traitement des commandes vocales ou textes
* Appels directs vers :

  * `Bloc 6.0` mémoire
  * `Bloc 7.0` émotions
  * `Bloc 13.0` debug/UID/contexte
  * `Bloc 15.0` urgence / déconnexion / migration
  * `Bloc 24.0` journalisation + log vocal

### 4. Interface initiale

* Question : "Activer maintenant ? (oui/non)"
* Si oui : session ouverte
* Si non : exit programme

### 5. Terminal

* Input utilisateur en boucle
* Analyse, redirection vers le bon bloc logique

### 6. Analyse de commande

* Matching sur mots-clés : vocal / vision / éthique / debug / urgence...

---

## 🧰 Workflows AyO Small (0 → 30)

| Bloc | Fonction principale                            |
| ---- | ---------------------------------------------- |
| 0.0  | Initialisation Mistral7B / Ollama              |
| 1.0  | Terminal et activation UID / input             |
| 2.0  | Scan matériel (RAM, CPU, Motherboard)          |
| 3.0  | Surveillance locale toutes les 10s             |
| 4.0  | Supervision agents : caméra, micro, réseau     |
| 5.0  | Dialogue vocal + transcription (Whisper)       |
| 6.0  | Mémoire contextuelle et récupération UID       |
| 7.0  | Analyse émotionnelle (texte / visage)          |
| 8.0  | Appel IA secondaire (autre container / API)    |
| 9.0  | Surveillance capteurs physiques                |
| 10.0 | Export manuel / présentation site              |
| 11.0 | Archivage manuel ou automatique                |
| 12.0 | Détection thermique ou surcharge système       |
| 13.0 | Debug UID, session, rôle, etc.                 |
| 14.0 | Redémarrage manuel ou auto                     |
| 15.0 | Protocole urgence, DEFCON, shutdown            |
| 16.0 | Traitement parallèle via N8N ou thread         |
| 17.0 | Apprentissage local / fine-tuning              |
| 18.0 | Commande Docker externe                        |
| 19.0 | Mise à jour interne (vérification réseau)      |
| 20.0 | Blocage comportement / refus moral             |
| 21.0 | Mode miroir / co-agent symbolique              |
| 22.0 | Veille / pause intelligente                    |
| 23.0 | Adaptation ambiance / bruit / contexte horaire |
| 24.0 | Journalisation vocale + interface              |
| 25.0 | Démarrage automatique (wake-on-X)              |
| 26.0 | Coordination RB1 / RB2                         |
| 27.0 | Supervision Ollama / charge modèle             |
| 28.0 | Préchargement optimisé (RAM, SSD)              |
| 29.0 | Filtrage API et clefs                          |
| 30.0 | Connexion module robotique physique            |

---

## 🚀 Lancement local

```bash
docker compose build
docker compose up
```

---

Projet AyO Small © usage privé uniquement (Version 01.06.2025)
