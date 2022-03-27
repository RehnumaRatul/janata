from tkinter.tix import Form
from django.shortcuts import redirect, render
from .models import VisualData
from .forms import VisualDataFrom
from django.contrib import messages




#fetching details andsaving in a dictionary
from django.core import serializers
text = serializers.serialize("python",VisualData.objects.all())


# Create your views here.

def delete(request,id):
        data = VisualData.objects.get(id=id)
        data.delete()
        return redirect('/')

def update(request,id):
        data = VisualData.objects.get(id=id)
        form= VisualDataFrom(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfully...!")
            return render(request, 'visualization/edit.html', {VisualData:data })


def edit(request,id):
        data = VisualData.objects.get(id=id)
       
        return render(request, 'visualization/edit.html', {VisualData:data })



       
        
 
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
    
