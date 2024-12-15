from django.shortcuts import render

# دالة لصفحة البداية
def home(request):
    return render(request, 'home.html')
