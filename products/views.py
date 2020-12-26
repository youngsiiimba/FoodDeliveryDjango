from django.shortcuts import render

# Create your views here.
def beta_view(request, *args, **kwargs):
    return render(request, "beta.html") 