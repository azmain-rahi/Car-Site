from django.shortcuts import render, redirect
from django.urls import reverse
from . import models

# Create your views here.

def list_view(request):
    all_cars_object = models.car.objects.all()
    context = {'all_cars': all_cars_object}
    return render(request,'cars/list.html', context=context)


def add_view(request):
    if request.POST:
        brand = request.POST['brand']
        year = int(request.POST['year'])
        models.car.objects.create(brand=brand, year=year)
        return redirect(reverse('cars:list'))
    else:
        return render(request,'cars/add.html')

def delete_view(request,topic=None):
    if request.POST:
        pk = int(request.POST['pk'])
        try:
            models.car.objects.get(pk=pk).delete()
            return redirect(reverse('cars:list'))
        except:
            not_found_msg = "pk is not matched and can't delete" 
            return redirect(reverse('cars:not_found', args=[not_found_msg]))
    elif topic is not None:
        my_dic = {'have_use':topic}
        return render(request,'cars/delete.html',context=my_dic)
    else:
        return render(request,'cars/delete.html')