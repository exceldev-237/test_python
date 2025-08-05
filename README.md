# 📈 Shareholder Management API

Une API construite avec **FastAPI** et **PostgreSQL** pour permettre à un administrateur de gérer les actionnaires, émettre des actions et générer des certificats PDF.

## 🚀 Lancer l'application

Assurez-vous d’avoir :

- Python 3.10+
- PostgreSQL en local (par défaut `postgres:root@localhost:5432/shareholders_db`)
- Les dépendances installées :
```bash
pip install -r requirements.txt
```

Démarrage de l’API :
```bash
uvicorn main:app --reload
```

## 🔐 Authentification JWT

Avant d’utiliser les autres endpoints, récupérez un **JWT token**.

### `POST /api/token/`
**Authentifie un utilisateur et retourne un token JWT.**

- 🔐 Nécessite : username (email), password
- 📤 Body (x-www-form-urlencoded) :
```text
username=admin@example.com
password=admin123
```
- ✅ Réponse :
```json
{
  "access_token": "<token>",
  "token_type": "bearer"
}
```

## 👨‍💼 Admin Endpoints

### `GET /api/shareholders/`
**Liste tous les actionnaires avec leur nombre total d’actions.**

- 🔐 Authentification requise (Admin)
- ✅ Réponse :
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "total_shares": 150
  }
]
```

### `POST /api/shareholders/`
**Créer un nouvel actionnaire.**

- 🔐 Authentification requise (Admin)
- 📤 Body (JSON) :
```json
{
  "name": "Alice Smith",
  "email": "alice@example.com"
}
```
- ✅ Réponse :
```json
{
  "id": 2,
  "name": "Alice Smith",
  "email": "alice@example.com"
}
```

### `POST /api/issuances/`
**Créer une émission d’actions pour un actionnaire existant.**

- 🔐 Authentification requise (Admin)
- 📤 Body (JSON) :
```json
{
  "shareholder_id": 1,
  "shares": 100,
  "price": 12.5,
  "date": "2025-08-05"
}
```
- ✅ Réponse :
```json
{
  "id": 1,
  "shareholder_id": 1,
  "shares": 100,
  "price": 12.5,
  "date": "2025-08-05"
}
```

### `GET /api/issuances/{id}/certificate/`
**Génère un certificat PDF pour une émission d’actions.**

- 🔐 Authentification requise (Admin ou propriétaire)
- 📥 Paramètre : `id` = ID de l’émission
- ✅ Réponse : Téléchargement du fichier PDF

## 👤 Shareholder Endpoints

### `GET /api/issuances/`
**Liste les émissions d’actions de l’actionnaire connecté.**

- 🔐 Authentification requise (Shareholder)
- ✅ Réponse :
```json
[
  {
    "id": 1,
    "shareholder_id": 2,
    "shares": 50,
    "price": 10,
    "date": "2025-08-01"
  }
]
```

## 🛡️ Headers d'authentification

Dans Postman :  
```
Authorization: Bearer <token JWT>
```

## 🧪 Données de test (par défaut)

```json
Admin:
  username: admin@example.com
  password: admin123

Shareholder:
  username: user@example.com
  password: user123
```

## 📂 Arborescence du projet

```
backend/
├── main.py
├── models.py
├── schemas.py
├── crud.py
├── auth.py
├── database.py
└── utils/pdf_generator.py
```

---

Développé par [VotreNom] 🧠