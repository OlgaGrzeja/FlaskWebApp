# Deploying Python Flask App on Heroku, czyli jak zrobić swoją apke online :grin:

## Wymagane oprogamowania :smile: :
* Python 3.6+ 
* Git i git credentials(instaluja się razem z gitem)
* Visual Studio Code
* Heroku Client
---
## Instalacja Klienta Heroku :sunglasses:
* W konsoli(cmd lub gitbash) wpisz ``` heroku --version ``` aby sprawdzić czy masz juz heroku, powinno wypisać coś w stylu heroku/x.y.z .
* Jeżeli nie masz heroku, zainstaluj Heroku [Link do instalatora Heroku](https://devcenter.heroku.com/articles/heroku-cli).
* Załóż konto na stronie heroku. 
---
## Logowanie się do heroku z użyciem terminala :alien:
1. Otwórz swój projekt w **Visual Studio Code** (z uruchomionym venvem i zainstalowanym flaskiem tak jak robiliśmy to wcześniej)
2. Wpisz do konsoli ``` heroku login ```, powinno poprosic Cię o login i hasło do Twojego konta z heroku.

---
## Przygotowanie aplikacji :pray:
1. Sprawdź czy w Twoim folderze znajduje się plik **requirements.txt**, jeżeli nie wykonaj komende ``` pip freeze > requirements.txt ```
2. w konsoli wpisz ``` pip install gunicorn ```, doinstaluje to serwer [gunicorn](https://gunicorn.org) który będzie potrzebny aby nasza aplikacja działała porpawnie na heroku.
3. Jeszcze raz wykonaj komende ``` pip freeze > requirements.txt ``` i sprawdź czy dodalo do pliku **gunicorn'a**.
4. Utwórz plik o nazwie **Procfile** (bez żadnego roszerzenia) i wpisz do niego ``` web: gunicorn app:app `` (komenda web w heroku służy to uruchomienia serwera a app:app  to od lewej nazwa modułu(naszego folderu) i nazwa naszej aplikacji.
---
## Dodawanie apki do heroku :metal:
1. Wpisz do konsoli ``` heroku create twoja-nazwa-aplikacji ``` nazwa musi byc unikatowa, wygenruje ci to dwa linki jeden jest to link do twojej strony a drugi jest linkiem do repozytorium gita na heroku tam przesyłać będziemy naszą aplikację.
2. Wpisz do konsoli ``` git remote -v ``` zauważ, że masz dodatkowego fetcha i pusha do heroku
3. Zcomituj wszystkie wczesniejsze zmiany
4. Wpisz do konsoli ``` git push heroku nazwa_twojej_gałęzi_na_gicie:master ```

---
# Linki pomocnicze i inne tutoriale :key:
#### [Medium tutorial](https://medium.com/the-andela-way/deploying-a-python-flask-app-to-heroku-41250bda27d0)
#### [Dokumentacja Heroku](https://devcenter.heroku.com/categories/reference)
#### [Heroku quick start dla Pythona](https://devcenter.heroku.com/articles/getting-started-with-python)
#### [Wujek Google](www.google.pl) :sheep: