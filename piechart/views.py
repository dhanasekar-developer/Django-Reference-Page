from django.shortcuts import render,redirect
from . models import Chart
from . forms import ProductForm

# Create your views here.

def piechart(request):
    products = Chart.objects.all()

    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('charts:piechart')
    else:
        form = ProductForm()

    context = {
        'products': products,
        'form': form,
    }

    return render(request, 'charts/piechart.html', context)