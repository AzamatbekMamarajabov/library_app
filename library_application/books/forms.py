from django import forms


class SearchForm(forms.Form):
    """This class is for Search Form to search specific informations """
    search = forms.CharField(required=False)