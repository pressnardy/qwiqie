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


