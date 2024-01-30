from .models import Store

def has_store(request):
    if request.user.is_authenticated:
        return {'has_store': Store.objects.filter(user_id=request.user).exists()}
    return {'has_store': False}
