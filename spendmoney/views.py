from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from .models import Expense, Income, ExpenseCategory
from django.contrib.auth import logout,login
from django.contrib.auth.forms import UserCreationForm
from spendmoney.forms import ExpenseForm, IncomeForm, form_errors_message


def index(request):
    income_items = Income.objects.filter(user=request.user).order_by('-date_added')
    expense_items = Expense.objects.filter(user=request.user).order_by('-date_added')
    budget_total = Income.objects.get_total_for_user(request.user)
    expense_total = Expense.objects.get_total_for_user(request.user)

    categories = ExpenseCategory.objects.order_by('name').all()

    context = {
        'categories': categories,
        'income_items': income_items,
        'expense_items':expense_items,
        'budget':budget_total,
        'expenses': expense_total,
    }

    return render(request,'index.html',context=context)

def add_expense(request):
    print(request.POST)
    form = ExpenseForm(request.POST)
    if form.is_valid():
        Expense.objects.create(
            **form.cleaned_data,
            user=request.user,
        )
    else:
        form_errors_message(request, form)

    return HttpResponseRedirect('app')


def add_income(request):
    form = IncomeForm(request.POST)
    if form.is_valid():
        Income.objects.create(
            **form.cleaned_data,
            user=request.user,
        )
    else:
        form_errors_message(request, form)

    return HttpResponseRedirect('app')


def graph_points(request):
    budget_total = Income.objects.get_total_for_user(request.user)
    expense_total = Expense.objects.get_total_for_user(request.user)

    return JsonResponse({
        'budget': budget_total,
        'expense': expense_total,
    })


def pie_graph(request):
    pie_expenses = Expense.objects.get_by_categories(request.user)

    return JsonResponse(pie_expenses)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if not form.is_valid():
            return render(request,'sign_up.html',{'form':form})

        user=form.save()
        login(request,user)
        return HttpResponseRedirect('app')
            
    else:
        form = UserCreationForm
        return render(request,'sign_up.html',{'form':form})
