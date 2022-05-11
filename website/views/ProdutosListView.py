from django.views.generic import ListView
from website.models import Produto


class ProdutosListView(ListView):
    model = Produto

