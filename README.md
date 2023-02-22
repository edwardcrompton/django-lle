# Running this locally

Followed Django installation steps from here: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment#installing_the_virtual_environment_software

Start the virtual environment

> mkvirtualenv my_django_environment

Install Django

> pip3 install django~=4.0

* What does installation do? Where does Django get installed?

Tried to install from requirements.txt

> pip3 install -r requirements.txt

* Some of these packages are huge. May be far too much bloat here - possibly because I'm installing the Github codebase version. Try to strip down to only the required packages.

# GitHub Codespaces ♥️ Django

Welcome to your shiny new Codespace running Django! We've got everything fired up and running for you to explore Django.

You've got a blank canvas to work on from a git perspective as well. There's a single initial commit with the what you're seeing right now - where you go from here is up to you!

Everything you do here is contained within this one codespace. There is no repository on GitHub yet. If and when you’re ready you can click "Publish Branch" and we’ll create your repository and push up your project. If you were just exploring then and have no further need for this code then you can simply delete your codespace and it's gone forever.

To run this application:

```python
python manage.py runserver
```
