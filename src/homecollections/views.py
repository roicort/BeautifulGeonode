from django.shortcuts import render
from django.views import View

# Create your views here.

from homecollections.models import HomeCollection

class HomeCollectionView(View):
    def get(self, request):
        homecollections = HomeCollection.objects.all()
        return render(request, 'collections.html', {'collections': homecollections})