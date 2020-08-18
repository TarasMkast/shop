from .models import Contact


def contact_info(request):
    return {'contact_info': Contact.objects.all()}
