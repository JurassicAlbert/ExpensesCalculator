from django import forms
from .models import Expense, Category


class ExpenseSearchForm(forms.ModelForm):
    date_from = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date', 'data-clear-btn': 'true'}))
    date_to = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date', 'data-clear-btn': 'true'}))
    categories = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Category.objects.filter(expense__isnull=False).distinct())

    class Meta:
        model = Expense
        fields = ('name', 'date_from', 'date_to', 'categories')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['date_from'].required = False
        self.fields['date_to'].required = False
        self.fields['categories'].required = False
