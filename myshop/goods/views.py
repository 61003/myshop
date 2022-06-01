from django.views.generic import ListView
from .models import Goods, Category



class GoodsList(ListView):
    model = Goods
    queryset = Goods.objects.prefetch_related('category').all()

    def get_template_names(self):
        return ['goods_list.html']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        category = Category.objects.all()
        context.update({
            'category': category
        })
        return context


class CategoryGoodsList(GoodsList):
    model = Goods

    def get_template_names(self):
        return ['category.html']

    def get_queryset(self):
        category_id = self.kwargs['id']
        return Goods.objects.filter(category=category_id)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        category_id = self.kwargs['id']
        category = Category.objects.filter(id=category_id).first()
        context.update({
            'category': {'category_name': category.category_name}
        })
        return context