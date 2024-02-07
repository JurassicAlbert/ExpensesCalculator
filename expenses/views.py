from django.db.models import Q
from .forms import ExpenseSearchForm
from .models import Expense, Category
from django.views.generic.list import ListView
from .reports import (summary_per_category, summary_per_year_month,
                      expenses_per_category, expenses_total_amount)


class ExpenseListView(ListView):
    """
    View displaying a list of expenses.

    Attributes:
        model (Expense): The model for the view.
        paginate_by (int): Number of items per page.

    Methods:
        get_context_data: Retrieve the context data for rendering the view.
    """

    model = Expense
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Get the context data for rendering the expense list view.

        Args:
            object_list (QuerySet): List of objects.

        Returns:
            dict: Context data for rendering the view.
        """
        queryset = object_list if object_list is not None else self.object_list

        form = ExpenseSearchForm(self.request.GET)
        if form.is_valid():

            name = form.cleaned_data.get('name', '').strip()
            date_from = form.cleaned_data.get('date_from')
            date_to = form.cleaned_data.get('date_to')
            categories = form.cleaned_data.get('categories')

            filters = Q()
            if name:
                filters &= Q(name__icontains=name)
            if date_from and date_to:
                filters &= Q(date__range=[date_from, date_to])
            if date_from:
                filters &= Q(date__gte=date_from)
            if date_to:
                filters &= Q(date__lte=date_to)
            if categories:
                filters &= Q(category__in=categories)

            queryset = queryset.filter(filters)

        sort = self.request.GET.get('sort')
        if sort:
            queryset = queryset.order_by(sort)

        return super().get_context_data(
            form=form,
            object_list=queryset,
            total_amount=expenses_total_amount(queryset),
            summary_per_category=summary_per_category(queryset),
            summary_per_year_month=summary_per_year_month(queryset),
            **kwargs)


class CategoryListView(ListView):
    """
    View displaying a list of categories.

    Attributes:
        model (Category): The model for the view.
        paginate_by (int): Number of items per page.
        template_name (str): Name of the template for rendering the view.
    """

    model = Category
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Get the context data for rendering the category list view.

        Args:
            object_list (QuerySet): List of objects.

        Returns:
            dict: Context data for rendering the view.
        """
        queryset = object_list if object_list is not None else self.object_list

        queryset = expenses_per_category(queryset)

        return super().get_context_data(
            object_list=queryset,
            **kwargs
        )
