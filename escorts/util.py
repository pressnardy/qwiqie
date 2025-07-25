import random

def get_cards(escorts):
    cards = []
    for escort in escorts:
        first_image = escort.images.first()
        if not first_image:
            continue
        card = {
            "name": escort.name,
            'escort_class': escort.escort_class,
            "phone_number": escort.phone_number,
            "location": escort.location,
            "profile_picture": first_image.image_field.url,
            'bio': get_bio(escort)
        }
        cards.append(card)
    return cards


def get_bio(escort):
    default_bio = f"I am {str(escort.name).title()}. Sexy hot escort from {str(escort.location).title()}. \
    Call on me to satisfy your fantacies"
    if str(escort.bio).lower() == 'none':
        return default_bio
    return escort.bio


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
    if not mobile_number.isdigit():
        raise ValueError("Mobile number must be numeric")
    if not 10 >= len(mobile_number) >= 9:
        raise ValueError("Mobile number wrong format")
    if str(country_code).startswith('+'):
        country_code = country_code[1:]
    
    if str(mobile_number).startswith('0') and len(mobile_number) == 10:
        mobile_number = mobile_number[1:]
    
    return f"{country_code}{mobile_number}"


def filter_by_location(escort_model, location):
    if location:
        location = str(location).strip().lower()
        # print(location)
    vips = escort_model.objects.filter(
        escort_class="vip", location=location).order_by('?')[:5]
    verified_escorts = escort_model.objects.filter(
        escort_class="verified", location=location).order_by('?')[:5]
    general_escorts = escort_model.objects.filter(
        escort_class="general", location=location).order_by('?')[:5]
    
    return {
        'vips': vips, 'verified': verified_escorts, 'general': general_escorts
    }


def clean_phone(phone):
    if " " in phone:
        phone = phone.split()
    numbers = [i for i in phone if i.isdigit()]
    if len(numbers) < 10:
        raise ValueError(f'phone number must be atleast 10 digits current is {"".join(numbers)} is not')
    digits = ['+254'] + numbers[-9:]
    return ''.join(digits)


def address_to_dict(address):
    address_list = address.split(",")
    address_list = [i.strip() for i in address_list]
    address_dict = {}
    
    count = 0
    while count <= len(address_list) and count <= 3:
        if count == 0:
            address_dict['county'] = address_list[0]
        if count == 1:
            address_dict['town'] = address_list[1]
        if count == 2:
            address_dict['area'] = address_list[2]
        else:
            address_dict['street'] = address_list[3:]
        count += 1
    
    return address_dict


def cleaned_address(address):
    if address:
        address_list = address.strip().replace(' ', '').split(",")
        return ''.join(address)
    

def get_counties_and_towns(county_model):
    ...


