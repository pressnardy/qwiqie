from escorts.forms import ServiceForm, ImageForm, CreateEscortForm, EditEscortDetails, FilterForm
from django.contrib import messages
from escorts.models import Escort, Image, Service, County, Town
from escorts import util


def get_index_context(vips, verified_escorts, general_escorts):
    locations = County.get_towns_and_counties()
    context = {
        'locations': locations,
        'filter_form': FilterForm(),
        'vips': util.get_cards(vips), 
        "verified_escorts": util.get_cards(verified_escorts), 
        "general_escorts": util.get_cards(general_escorts),
    }
    return context



