# Image officielle Python
FROM python:3.11-slim

# Répertoire de travail dans le container
WORKDIR /app

# Installer les dépendances système nécessaires pour psycopg2
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copier requirements et installer dépendances Python
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copier le reste du projet
COPY . .

# Exposer le port Django
EXPOSE 8000

# Commande par défaut pour lancer Django
CMD ["python", "presence_api/manage.py", "runserver", "0.0.0.0:8000"]
