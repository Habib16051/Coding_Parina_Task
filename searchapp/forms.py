from django import forms


class KhojSearchForm(forms.Form):
    input_values = forms.CharField(
        label="Input Values: ")
    search_value = forms.IntegerField(label="Search Value: ")
