from collections import OrderedDict
from django.db.models import Sum, Value, Count
from django.db.models.functions import Coalesce, ExtractYear, ExtractMonth


def summary_per_category(queryset):
    """
    Calculate the summary of expenses per category.

    Args:
        queryset (QuerySet): List of Expense objects.

    Returns:
        OrderedDict: A dictionary containing category names and their total
        amounts.
    """
    return OrderedDict(sorted(
        queryset
        .annotate(category_name=Coalesce('category__name', Value('-')))
        .order_by()
        .values('category_name')
        .annotate(s=Sum('amount'))
        .values_list('category_name', 's')
    ))


def summary_per_year_month(queryset):
    """
    Calculate the summary of expenses per year-month.

    Args:
        queryset (QuerySet): List of Expense objects.

    Returns:
        list: A list of tuples containing year, month, and total amount for
        each year-month.
    """
    return queryset.values('date__year', 'date__month').annotate(
        year=ExtractYear('date'),
        month=ExtractMonth('date'),
        total_amount=Sum('amount')
    ).order_by('year', 'month').values_list('year', 'month', 'total_amount')


def expenses_per_category(queryset):
    """
    Annotate the number of expenses per category.

    Args:
        queryset (QuerySet): List of Category objects.

    Returns:
        QuerySet: Annotated QuerySet with the number of expenses per category.
    """
    return queryset.annotate(num_expenses=Count('expense'))


def expenses_total_amount(queryset):
    """
    Calculate the total amount of expenses.

    Args:
        queryset (QuerySet): List of Expense objects.

    Returns:
        Decimal: The total amount of expenses.
    """
    return queryset.aggregate(total_amount=Sum('amount'))['total_amount']
