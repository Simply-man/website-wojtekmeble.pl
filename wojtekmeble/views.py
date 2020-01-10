from django.shortcuts import render, get_list_or_404


from .models import Pictures

# Check if templeates works


def index(request):
    picture = Pictures.objects.all()[:3]
    context = {
        'picture': picture
    }
    return render(request, "website/index.html", context)


def RecentRealizations(request):
    if request.method == "GET":
        picture = get_list_or_404(Pictures)
        context = {
            'picture': picture
        }
        return render(request, 'website/Recent_Realizations.html', context)
