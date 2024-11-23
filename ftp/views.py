from django.shortcuts import render, redirect
from . forms import FtpForm


# Create your views here.

def upload_image(request):

    if request.method == 'POST' and request.FILES['image']:
        form = FtpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ftp:ftp_view')
    else:
        form = FtpForm()
    return render(request, 'ftp/ftp_form.html', { 'form': form })