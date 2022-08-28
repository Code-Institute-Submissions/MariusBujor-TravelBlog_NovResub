from django.shortcuts import render, redirect
from .models import Wish
from .forms import WishForm
from django.contrib import messages


def create_wish(request):
    if request.method == 'POST':
        form = WishForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = Wish.objects.all()
            messages.success(request, ("Your location that you want to visit has been added to List !"))
            return render(request, "wish/wish.html", {'all_items': all_items})

    else:
        all_items = Wish.objects.all()
        return render(request, "wish/wish.html", {'all_items': all_items})


def delete(request, wish_id):
    item = Wish.objects.get(pk=wish_id)
    item.delete()
    messages.success(request, ('Location Has Been Deleted !'))
    return redirect('wish_create')


def cross_off(request, wish_id):
    item = Wish.objects.get(pk=wish_id)
    item.completed = True
    item.save()
    return redirect('wish_create')


def uncross(request, wish_id):
    item = Wish.objects.get(pk=wish_id)
    item.completed = False
    item.save()
    return redirect('wish_create')
