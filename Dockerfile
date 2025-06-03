# Dockerfile pour le conteneur AyO Small
FROM python:3.10-slim

# Définition du dossier de travail dans le conteneur
WORKDIR /app

# Copie du contenu local vers le conteneur (mistral7b_ayo_small)
COPY . .

# Installation des dépendances depuis requirements.txt
# Ce fichier doit contenir Flask, etc. (voir main.py)
RUN pip install --no-cache-dir -r requirements.txt

# Exposition du port Flask utilisé dans main.py
EXPOSE 5678

# Point d'entrée automatique au lancement du conteneur
CMD ["python", "main.py"]
