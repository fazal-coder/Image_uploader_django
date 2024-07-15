from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image

def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the 'home' view after saving the form

    form = ImageForm()
    img = Image.objects.all()
    context = {'img': img, 'form': form}
    return render(request, 'home.html', context)
