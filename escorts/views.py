from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ServiceForm, ImageForm, CreateEscortForm, EditEscortDetails, FilterForm
from django.contrib import messages
from .models import Escort, Image, Service
from . import util
from .util import get_cards, filter_escorts
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    vips = Escort.objects.filter(escort_class="vip", gender="female")
    verified_escorts = Escort.objects.filter(escort_class="verified", gender='female')
    general_escorts = Escort.objects.filter(escort_class="general", gender="female")
    filter_form = FilterForm()
    context = {
        'filter_form': filter_form,
        'vips': get_cards(vips), 
        "verified_escorts": get_cards(verified_escorts), 
        "general_escorts": get_cards(general_escorts),
    }
    return render(request, "escorts/index.html", context)

@csrf_exempt
def filter_location(request):
    print('called')
    context = {
        'filter_form': FilterForm(),
    }
    if request.method == 'POST':
        print("post")
        location = request.POST['location'].lower()
        if not location:
            return redirect('escorts:index')
        escorts = util.filter_by_location(Escort, location=location)
        context = {
        'filter_form': FilterForm(),
        'vips': get_cards(escorts['vips']), 
        "verified_escorts": get_cards(escorts['verified']), 
        "general_escorts": get_cards(escorts['general']),
        }
        return render(request, 'escorts/index.html', context)


@csrf_exempt
def female_filters(request):
    if request.method == "POST":
        filter_form = FilterForm(request.POST)
        print(filter_form)      
        escorts = filter_escorts(filter_form=filter_form, escort_model=Escort, gender='female')
        filter_form = FilterForm()
        context = {
            'filter_form': filter_form,
            'vips': get_cards(escorts['vips']), 
            "verified_escorts": get_cards(escorts['verified']), 
            "general_escorts": get_cards(escorts['general']),
        }

        return render(request, 'escorts/index.html', context)
    return redirect('escorts:index')
    

   
@csrf_exempt
def get_females(request):
    vips = Escort.objects.filter(escort_class="VIP", gender="female").order_by('?')[:5]
    verified_escorts = Escort.objects.filter(escort_class="verified", gender='female')[:5]
    general_escorts = Escort.objects.filter(escort_class="general", gender="female")[:5]
    form = FilterForm()
    context = {
        'form': form,
        'vips': get_cards(vips), 
        "verified_escorts": get_cards(verified_escorts), 
        "general_escorts": get_cards(general_escorts),
    }
    return render(request, "escorts/escorts.html", context)


@csrf_exempt
def filter_gender(request):
    if request.method == 'POST':
        print('gender called')
        gender = request.POST['gender']
        vips = Escort.objects.filter(escort_class="VIP", gender=gender).order_by('?')[:5]
        verified_escorts = Escort.objects.filter(escort_class="verified", gender=gender)
        general_escorts = Escort.objects.filter(escort_class="general", gender=gender)
        form = FilterForm()
        context = {
            'filter_form': form,
            'vips': get_cards(vips), 
            "verified_escorts": get_cards(verified_escorts), 
            "general_escorts": get_cards(general_escorts),
        }
        return render(request, "escorts/index.html", context)
    

def view_escort(request, phone_number):
    """
    view only version of ecort profile targeting escort clients
    """
    escort = get_object_or_404(Escort, phone_number=phone_number)
    services = escort.services.all()
    images = escort.images.all()
    context = {'escort': escort, 'services': services, 'images': images}    
    return render(request, 'escorts/escort.html', context)


@login_required
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

@login_required
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

@login_required
def delete_escort(request, phone_number):
    escort = Escort.objects.filter(phone_number=phone_number, created_by=request.user).first()
    if escort and escort.created_by == request.user:  
        escort.delete()
        messages.success(request, 'Escort deleted successfully!')
    return redirect('users:account')

@login_required
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
    return render(request, 'escorts/edit_details.html', context)


@login_required
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


@login_required
def remove_service(request, phone_number, service_id):
    service = Service.objects.filter(service_id=service_id, created_by=request.user).first()
    if service:
        service.delete()
    return redirect('escorts:profile', phone_number=phone_number)


@login_required
def add_image(request, phone_number):
    escort = Escort.objects.filter(phone_number=phone_number, created_by=request.user).first()
    if not escort:
        return HttpResponse("Escort not found or you are not authorized to add images.")

    if request.method == "POST":
        
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.escort = escort
            image.created_by = request.user
            image.save()
            return redirect('escorts:profile', phone_number=phone_number)

    form = ImageForm()
    return render(request, 'escorts/add_image.html', {'escort': escort, "form": form})


@login_required
def remove_image(request, phone_number, image_id):
    image = Image.objects.filter(image_id=image_id, created_by=request.user).first()
    if image:
        # Delete the image file from the directory
        if image.image_field:
            image.image_field.delete(save=False)
        image.delete()
    return redirect('escorts:profile', phone_number)


@login_required
def pay(request, escort_phone):
    if request.method == 'POST':
        form = PaymentForm()
        if form.is_valid:
            
            pass   
    return 

