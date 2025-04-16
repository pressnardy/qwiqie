from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ServiceForm, ImageForm, CreateEscortForm, EditEscortDetails
from django.contrib import messages
from .models import Escort, Image, Service


def index(request):
    escorts = Escort.objects.all()
    context = {
        'escorts': escorts,
    }
    return render(request, "escorts/index.html", context)


def view_escort(request, phone_number):
    """
    view only version of ecort profile targeting escort clients
    """
    escort = get_object_or_404(Escort, phone_number=phone_number)
    servises = escort.services.all()
    images = escort.images.all()
    context = {'escort': escort, 'servises': servises, 'images': images}    
    return render(request, 'escorts/escort.html', context)


def profile(request, phone_number):
    """
    the editable version of the ecort profile for the escort and their account managers
    """
    if not request.user.is_authenticated:
        return redirect('users:login')
    escort = Escort.objects.filter(phone_number=phone_number, created_by=request.user).first()
    if not escort:
        return redirect('users:account')
    services = escort.services.all()
    images = escort.images.all()
    for image in images:
        print(image.image_field.url) 
    context = {'escort': escort, 'services': services, 'images': images}
    return render(request, "escorts/profile.html", context)


def create_escort(request):
    if request.method == "POST":
        form = CreateEscortForm(request.POST or None)
        if form.is_valid():
            form.instance.created_by = request.user
            escort_phone = form.cleaned_data.get('phone_number')
            form.save()
            return redirect("escorts:profile", phone_number=escort_phone)
    form = CreateEscortForm()
    return render(request, 'escorts/create_escort.html', {'form': form})


def delete_escort(request, phone_number):
    escort = Escort.objects.filter(phone_number=phone_number, created_by=request.user).delete()
    if not escort:
        return redirect('users:account')
    if request.method == 'POST':    
        escort.delete()
        messages.success(request, 'Escort deleted successfully!')
    return redirect('users:account')


def edit_escort_details(request, phone_number):
    escort = Escort.objects.filter(phone_number=phone_number, created_by=request.user).first()
    if request.method == 'POST':
        form = EditEscortDetails(request.POST, instance=escort)
        form.instance.created_by = request.user
        if form.is_valid():
            form.save()
            return redirect('escorts:profile', phone_number=phone_number)
    else:
        form = CreateEscortForm(instance=escort)
    context = {'form': form, 'escort': escort}
    return render(request, 'escorts/create_escort.html', context)


def add_service(request, phone_number):    
    escort = Escort.objects.filter(phone_number=phone_number, created_by=request.user).first()
    if not escort:
        return HttpResponse("You Need to Create an Escort Profile First")
    if request.method == "POST":
        form = ServiceForm(request.POST or None)
        form.instance.escort_id = escort
        form.instance.created_by = request.user
        if form.is_valid():
            form.save()
            return redirect('escorts:profile', phone_number=phone_number)
    form = ServiceForm()
    return render(request, 'escorts/add_service.html', {'escort': escort, "form": form})


def remove_service(request, phone_number, service_id):
    service = Service.objects.filter(service_id=service_id, created_by=request.user).first()
    if not service and request.method == 'POST':
        service.delete()
    return redirect('escorts:profile', phone_number=phone_number)

def add_image(request, phone_number):
    escort = Escort.objects.filter(phone_number=phone_number, created_by=request.user).first()
    if not escort:
        return HttpResponse("Escort not found or you are not authorized to add images.")

    if request.method == "POST":
        
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            print("valid")
            image = form.save(commit=False)
            image.escort_id = escort
            image.created_by = request.user
            image.save()
            return redirect('escorts:profile', phone_number=phone_number)

    form = ImageForm()
    return render(request, 'escorts/add_image.html', {'escort': escort, "form": form})


def remove_image(request, phone_number, image_id):
    image = Image.objects.filter(image_id=image_id, created_by=request.user).first()
    if image and request.method == 'POST':
        image.delete()
    return redirect('escorts:profile', phone_number)

