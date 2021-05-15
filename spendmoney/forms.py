from django import forms
from django.contrib import messages


class IncomeForm(forms.Form):
    amount = forms.FloatField(label='Сумма')
    date_added = forms.DateField(label='Дата')


class ExpenseForm(forms.Form):
    expense_name = forms.CharField(label='Название')
    amount = forms.FloatField(label='Сумма')
    date_added = forms.DateField(label='Дата')
    category_id = forms.IntegerField(label='Категория')


def form_errors_message(request, form):
    errors = form.errors.get_json_data()
    print(errors)
    for error in errors:
        messages.error(request, "{}: {}".format(form.fields[error].label, errors[error][0]["message"]))
