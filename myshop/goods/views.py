from django.views.generic import ListView
from .models import Goods


class GoodsList(ListView):
    model = Goods
