from django import forms

class PlaceSearchForm(forms.Form):
    search = forms.CharField(help_text="Enter the name of the place to search.", max_length=60)

    def clean_search(self):
        search = self.cleaned_data['search']
        return search

class PlaceAddForm(forms.Form):
    name = forms.CharField(help_text="Enter the name of the place.", max_length=60)
    address = forms.CharField(help_text="Enter the address of the place", max_length=256)

    def clean_name(self):
        return name

    def clean_address(self):
        return address