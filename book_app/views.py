from django.shortcuts import render,redirect
from . models import shop
from .forms import ModeForm


# Create your views here.
# def hoom(request):
#     return render(request, 'detail.html')
def demo(request):
    products=shop.objects.all()
    return render(request,'index.html',{'prod':products})
def details(request,shop_id):
    pro=shop.objects.get(id=shop_id)
    return render(request,'detail.html',{'prod': pro})
def ad(request):
    if request.method=='POST':
        title=request.POST.get('title')
        author = request.POST.get('author')
        desc=request.POST.get('desc')
        price=request.POST.get('price')
        img=request.FILES['img']
        s=shop(title=title,author=author,desc=desc,price=price,img=img)
        s.save()
        print('product added')

    return render(request,'add_product.html')
def update(request,id):
    obj=shop.objects.get(id=id)
    form=ModeForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'obj':obj})
def delete(request,id):
    if request.method=='POST':
        obj=shop.objects.get(id=id)
        obj.delete()
        return redirect('/')
    else:
        return render(request,'delete.html')



