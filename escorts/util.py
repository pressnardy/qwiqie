import random

def get_cards(escorts):
    cards = []
    for escort in escorts:
        first_image = escort.images.first()
        if not first_image:
            continue
        card = {
            "name": escort.name,
            "phone_number": escort.phone_number,
            "location": escort.location,
            "profile_picture": first_image.image_field.url
        }
        cards.append(card)
    return cards


def get_random_ids(model):
    total_objects = model.objects.count()
    random_ids = random.sample(range(1, total_objects + 1), 5)
    random_objects = model.objects.filter(id__in=random_ids)

    return random_objects

def filter_escorts(filter_form, escort_model, gender):
    try:
        body_type = filter_form.cleaned_data['body_type']
    except KeyError:
        pass
    try:
        min_age = filter_form.cleaned_data['age'].split('-')[0].strip()
    except KeyError:
        pass
    try:
        max_age = filter_form.cleaned_data['age'].split('-')[1].strip()
    except KeyError:
        pass
    try:
        skin_color = filter_form.cleaned_data['skin_color']
    except KeyError:
        pass
    escorts = escort_model.objects.filter(
        gender=gender, age__gte=min_age, age__lte=max_age, body_type=body_type, skin_color=skin_color
        )
    vips = [escort for escort in escorts if escort.escort_class == 'VIP']
    verified = [escort for escort in escorts if escort.escort_class == 'Verified']
    general = [escort for escort in escorts if escort.escort_class == 'general']
    return {
        'vips': vips,
        'verified': verified,
        'general': general
    }

    
def format_phone_number(mobile_number, country_code='254'):
    # Remove '+' if present
    if country_code.startswith('+'):
        country_code = country_code[1:]
    
    # Remove leading 0 from mobile number if present
    if mobile_number.startswith('0') and len(mobile_number) == 10:
        mobile_number = mobile_number[1:]
    
    return f"{country_code}{mobile_number}"

# Example usage:
print(format_phone_number("0712345678", "+254"))  # Output: 254712345678

def filter_by_location(escort_model, location):
    vips = escort_model.objects.filter(
        escort_class="VIP", location=location).order_by('?')[:5]
    verified_escorts = escort_model.objects.filter(
        escort_class="verified", location=location).order_by('?')[:5]
    general_escorts = escort_model.objects.filter(
        escort_class="general", location=location).order_by('?')[:5]
    
    return {
        'vips': vips, 'verified': verified_escorts, 'general': general_escorts
    }


