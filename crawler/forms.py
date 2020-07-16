from django import forms



class SearchForm(forms.Form):
    """
    This is the basic form for the user where he/she will search for his required articles/research Papers.
    """
    # Here we are defining the type of the fields 
    article = forms.CharField(
        max_length=100, required=True, label="Enter article Name:",
        widget=forms.TextInput(attrs={'placeholder': "Enter subject title or Name",
                                    'autofocus': 'autofocus'}))
