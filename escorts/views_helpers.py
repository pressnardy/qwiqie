from escorts.forms import ServiceForm, ImageForm, CreateEscortForm, EditEscortDetails, FilterForm
from django.contrib import messages
from escorts.models import Escort, Image, Service, County, Town
from escorts import util

HOT_SERVICES = [
    'one night stand', 'Threesome', 'cum on face', 'BJ','hand job', 'extraball', 'bolls massage', 'girlfriend esxperience', 'sugar momy'
    ]
HOT_COUNTIES = [
    'nairobi', 'mombasa', 'kisumu', 'nakuru', 'embu'
]
def get_index_context(vips=None, verified_escorts=None, general_escorts=None):
    services = HOT_SERVICES
    counties = HOT_COUNTIES
    locations = County.get_towns_and_counties()
    escorts = []
    if vips:
        escorts += vips
    if general_escorts:
        escorts += general_escorts
    if verified_escorts:
        escorts += verified_escorts
    
    context = {
        'counties': counties,
        'locations': locations,
        'services': services,
        'filter_form': FilterForm(),
        'escorts': util.get_cards(escorts),
    }
    return context


def search_service(service_name):
    escorts = Escort.objects.all()
    results = []
    for escort in escorts:
        if escort.services.filter(service_name=service_name.lower().strip()).first():
            results.append(escort)
    return results or None




