# Running this locally

Followed Django installation steps from here: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment#installing_the_virtual_environment_software

Start the virtual environment

> mkvirtualenv my_django_environment

Install Django

> pip3 install django~=4.0

* What does installation do? Where does Django get installed?

Install from requirements.txt

> pip3 install -r requirements.txt

Run the server

> python3 manage.py runserver

## Adding a place

Go to: http://127.0.0.1:8000/add/search/

Search for a place.

When I click add I should be taken to a form prepopulated with information about that place.
- OSM id
- Type of place
- Full address of the place
- Postcode

I can then save the form and the place will be added to the database.

Once saved in the database, I can associate a sound file with the place in order to pronounce it.

# GitHub Codespaces ♥️ Django

Welcome to your shiny new Codespace running Django! We've got everything fired up and running for you to explore Django.

You've got a blank canvas to work on from a git perspective as well. There's a single initial commit with the what you're seeing right now - where you go from here is up to you!

Everything you do here is contained within this one codespace. There is no repository on GitHub yet. If and when you’re ready you can click "Publish Branch" and we’ll create your repository and push up your project. If you were just exploring then and have no further need for this code then you can simply delete your codespace and it's gone forever.

To run this application:

```python
python manage.py runserver
```
