from django.shortcuts import render
from django.http import Http404
from .models import Owner
from .models import Car
from .forms import CarOwnerForm
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView


def detail(request, user_id):
    try:
        user = Owner.objects.get(pk=user_id)
    except Owner.DoesNotExist:
        raise Http404("Car owner doesn't exist!")
    return render(request, "owner.html", {'owner': user})


class OwnersList(ListView):
    model = Owner
    template_name = 'owners.html'

    queryset = model.objects.all()

    def get_queryset(self):
        id = self.request.GET.get('id')

        if id:

            try:
                id = int(id)
                queryset = self.queryset.filter(id=id)

            except ValueError:
                queryset = self.model.objects.none()

            return queryset

        return self.queryset


class OwnersRetrieveList(DetailView):
    model = Owner
    template_name = 'owner.html'


class CarsRetrieveList(DetailView):
    model = Car
    template_name = 'car.html'


class CarsList(ListView):
    model = Car
    template_name = 'cars.html'

    queryset = model.objects.all()

    def get_queryset(self):
        id = self.request.GET.get('id')

        if id:

            try:
                id = int(id)
                queryset = self.queryset.filter(id=id)

            except ValueError:
                queryset = self.model.objects.none()

            return queryset

        return self.queryset


def addOwner(request):
    context = {}
    form = CarOwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'create_owner.html', context)


class Create(CreateView):
   model = Car
   template_name = 'create_car.html'
   fields = ['number', 'brand', 'model', 'color']

class Delete(DeleteView):
    model = Car
    success_url = '/cars/'
    template_name = 'delete_car.html'

class Edit(UpdateView):
    model = Car
    fields = ['number', 'brand', 'model', 'color']
    success_url = '/cars/'
    template_name = 'edit_car.html'

