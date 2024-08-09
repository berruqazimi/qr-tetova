from django.shortcuts import render, redirect ,get_object_or_404
from .models import QRCodeModel
from .forms import QRCodeForm,SearchForm
from django.contrib.auth.decorators import permission_required




def home(request):
    context = dict()
    return render(request, 'home.html', context=context)
def register(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            qr_code_instance = form.save()
            return redirect('retrieve', pk=qr_code_instance.pk)
    else:
        form = QRCodeForm()
    return render(request, 'register.html', {'form': form})

def retrieve(request, pk):
    qr_code_instance = QRCodeModel.objects.get(pk=pk)
    return render(request, 'retrieve.html', {'qr_code_instance': qr_code_instance})


def search(request):
    form = SearchForm(request.POST or None)
    qr_codes = QRCodeModel.objects.none()
    no_results = False
    if form.is_valid():
        query = form.cleaned_data.get('query')
        if query:
            qr_codes = QRCodeModel.objects.filter(name__icontains=query)
            if not qr_codes.exists():
                no_results = True


    return render(request, 'search.html', {'form': form, 'qr_codes': qr_codes, 'no_results':no_results})
@permission_required('qr.can_update_qrcode', raise_exception=True)
def update_qr_code(request, id):
    qr_code = get_object_or_404(QRCodeModel, id=id)
    if request.method == 'POST':
        form = QRCodeForm(request.POST, instance=qr_code)
        if form.is_valid():
            form.save()
            return redirect('search')
    else:
        form = QRCodeForm(instance=qr_code)
    return render(request, 'update_qr_code.html', {'form': form})
@permission_required('qr.can_update_qrcode', raise_exception=True)
def delete_qr_code(request, id):
    qr_code = get_object_or_404(QRCodeModel, id=id)
    if request.method == 'POST':
        qr_code.delete()
        return redirect('search')
    return render(request, 'delete_qr_code.html', {'qr_code': qr_code})