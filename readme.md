### Librairie

* [![Django][django]][Django-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]

<p align="right">(<a href="#readme-top">Revenir en haut</a>)</p>

### Installation

1. Aller sur https://github.com/louispelarrey/library-django/tree/main
2. Cloner le repository
   ```sh
   git clone https://github.com/louispelarrey/library-django/tree/main
   ```
3. Lancer le build
   ```sh
   docker composer build
   ```
4. Lancer les containers
   ```sh
   docker composer up -d
   ```
5. Se connecter au container php
   ```sh
   docker exec -it [id container] /bin/sh
   ```
6. Lancer les migrations
   ```sh
   python3 manage.py makemigrations
   python manage.py migrate
   ```
7. Lancer les fixtures
   ```sh
   python manage.py loaddata */fixtures/*.json
   ```
<p align="right">(<a href="#readme-top">Revenir en haut</a>)</p>

## Usage

Pour se connecter en tant qu'admin :

1. Aller sur http://localhost:8000/admin/login/?next=/admin/
2. Se connecter avec "Admin" et le mot de passe "password"

Pour se connecter en tant que client :

1. Aller sur http://localhost:8000/members/login_user/
2. Se connecter avec "ClientOne" et le mot de passe "password"

Pour se connecter en tant que libraire :

1. Aller sur http://localhost:8000/members/login_user/
2. Se connecter avec "BooksellerOne" et le mot de passe "password"

<p align="right">(<a href="#readme-top">Revenir en haut</a>)</p>