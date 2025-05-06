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
        max_age = filter_form.cleaned_data['age'].split['-'][1].strip()
    except KeyError:
        pass
    try:
        skin_color = filter_form.cleaned_data['skin_color']
    except KeyError:
        pass
    escorts = escort_model.objects.filter(gender=gender, age__gte=min_age, age__lte=max_age, body_type=body_type, skin_color=skin_color)
    return escorts

    

