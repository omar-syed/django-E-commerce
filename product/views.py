from django.shortcuts import render , get_object_or_404
from .models import Product,Category
from django.core.paginator import Paginator
from django.db.models import Q , Count


# Create your views here.

def product_list(request,category_slug=None):
    category = None

    product_list = Product.objects.all()
    products = Product.objects.filter(PRDAvailable=True)
    category_list = Category.objects.annotate(total_products=Count('product')).exclude(CATParent__isnull=True)

#################################################################################

    if category_slug :
        category     = get_object_or_404(Category,CATSlug=category_slug)
        product_list = product_list.filter(PRDCategory=category)


################################################################################

    search_query = request.GET.get('q')
    if search_query :
        product_list = product_list.filter(
            Q(PRDName__icontains=search_query)|
            Q(PRDCategory__CATName__icontains=search_query)
        )   

#################################################################################
    
    paginator = Paginator(product_list, 3) 
    page = request.GET.get('page')
    product_list = paginator.get_page(page)

    context = {'product_list' : product_list,'category_list':category_list}
    return render(request , 'Product/product_list.html' , context)


def product_detail(request , slug):
    #prodcut_detail = Product.objects.get(id=id)
    prodcut_detail = get_object_or_404(Product ,PRDSLug=slug ,PRDAvailable=True)
    context = {'prodcut_detail' : prodcut_detail}
    return render(request , 'Product/product_detail.html' , context)    