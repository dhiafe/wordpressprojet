from django.shortcuts import render

def cv_view(request):
    return render(request, 'portfolio/cv.html')

def stages_view(request):
    return render(request, 'portfolio/stages.html')

def travaux_view(request):
    return render(request, 'portfolio/travaux.html')

def certifications_view(request):
    return render(request, 'portfolio/certifications.html')


# Create your views here.
