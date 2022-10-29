from django.shortcuts import render,redirect
from . models import vehicle
from . forms import ModeForm

# Create your views here.
def fun(request):
    obj=vehicle.objects.all()
    return render(request,'index.html',{'vehicles':obj})


def about(request):
    return render(request,'about.html')

def source(request):
    return render(request,'source.html')

def add_vehicle(request):
    if request.method=='POST':
        number = request.POST.get('number')
        type = request.POST.get('type')
        model = request.POST.get('model')
        description = request.POST.get('description')
        v=vehicle(number=number,type=type,model=model,description=description)
        v.save()
        print('added')
    return render(request,'add_vehicle.html')

def update(request,id):
    obj=vehicle.objects.get(id=id)
    form=ModeForm(request.POST or None,request.FILES,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    if obj:
        return render(request, 'edit.html', {'form': form, 'obj': obj})
    else:
        return redirect('/')

def detail(request,vehicle_id):
    vehicle1=vehicle.objects.get(id=vehicle_id)
    return render(request,'detail.html',{'vehicles':vehicle1})

def delete(request,id):
    vehicle1 = vehicle.objects.get(id=id)
    if request.method=='POST':
        obj=vehicle.objects.get(id=id)
        obj.delete()
        return redirect('/')
    return render(request,'delete.html',{'vehicles':vehicle1})
