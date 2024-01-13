from .forms import ExpenseSearchForm
from .models import Expense, Category
from .reports import summary_per_category
from django.core.paginator import Paginator
from django.views.generic.list import ListView


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

            if name:
                queryset = queryset.filter(name__icontains=name)
            if date_from and date_to:
                queryset = queryset.filter(date__range=[date_from, date_to])
            if date_from:
                queryset = queryset.filter(date__gte=date_from)
            if date_to:
                queryset = queryset.filter(date__lte=date_to)
            if categories:
                queryset = queryset.filter(category__in=categories)

        sort = self.request.GET.get('sort')
        if sort:
            queryset = queryset.order_by(sort)

        return super().get_context_data(
            form=form,
            object_list=queryset,
            summary_per_category=summary_per_category(queryset),
            **kwargs)


class CategoryListView(ListView):
    """
    View displaying a list of categories.

    Attributes:
        model (Category): The model for the view.
        paginate_by (int): Number of items per page.
    """

    model = Category
    paginate_by = 5
