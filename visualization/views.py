from tkinter.tix import Form
from django.shortcuts import redirect, render
from .models import VisualData
from .forms import VisualDataFrom




#fetching details andsaving in a dictionary
from django.core import serializers
text = serializers.serialize("python",VisualData.objects.all())


# Create your views here.




 
def index(request):
    a = 27
    data = VisualData.objects.all()
    if request.method == 'POST':
        form = VisualDataFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
            
    else:
        form = VisualDataFrom()

    
    context = {
        'data': data,
        'form': form,
        'text': text,
        
    }
    return render(request, 'visualization/index.html', context)
