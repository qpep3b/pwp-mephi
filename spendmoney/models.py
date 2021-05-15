from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Sum, FloatField
from django.db.models import Q
from django.db.models.functions import Coalesce


class IncomeManager(models.Manager):
    def get_total_for_user(self, user):
        res = self.filter(
            user=user
        ).aggregate(
            total=Coalesce(
                Sum('amount'), 0, output_field=FloatField()
            )
        )

        return res['total']

class Income(models.Model):
    amount = models.FloatField()
    date_added = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = IncomeManager()


class ExpenseCategory(models.Model):
    name = models.CharField(max_length=64)


class ExpenseManager(models.Manager):    
    def get_total_for_user(self, user):
        res = self.filter(
            user=user
        ).aggregate(
            total=Coalesce(
                Sum('amount'), 0, output_field=FloatField()
            )
        )

        return res['total']
    
    def get_by_categories(self, user):
        user_expenses = self.filter(user=user).prefetch_related('expense_category') \
            .values('category__name').annotate(total=Sum('amount'))

        result = {}
        for row in user_expenses:
            result[row['category__name']] = row['total']
        
        return result


class Expense(models.Model):
    expense_name = models.CharField(max_length=20)
    amount = models.FloatField()
    date_added = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)

    objects = ExpenseManager()
