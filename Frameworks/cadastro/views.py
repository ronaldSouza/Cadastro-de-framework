from django.shortcuts import render, redirect
from .models import Framework
from .forms import frameworkForm

# Create your views here.

def index(request):
    return render(request, 'index.html')


def crud(request):
    framework = Framework.objects.all()

    form = frameworkForm()

    context = {
        'form': form
    }

    return render(request, 'crud.html', context)


def create(request):
    form = frameworkForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list')


def read(request):

    frameworks = Framework.objects.all()

    return render(request, 'listagem.html', {'frameworks': frameworks})

def consulta(request):

    frameworks = Framework.objects.all()

    return render(request, 'consulta.html', {'frameworks': frameworks})

def search(request):

    frameworks = Framework.objects.filter(name__icontains=request.GET.get('search', ''), )

    return render(request, 'consulta.html', {'frameworks': frameworks})
