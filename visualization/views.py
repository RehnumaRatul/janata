from tkinter.tix import Form
from django.shortcuts import redirect, render
from .models import VisualData
from .forms import VisualDataFrom

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
        
    }
    return render(request, 'visualization/index.html', context)