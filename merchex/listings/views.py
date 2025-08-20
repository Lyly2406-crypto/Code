from django.shortcuts import render 
from django.http import HttpResponse
from .models import Band

from listings.forms import BandForm,ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect
from .forms import BandForm




def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band_id=band.id)
    else:
        form = BandForm()

    return render(request, "listings/band_create.html", {"form": form})


def home(request):
    return render(request, 'listings/home.html')


def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
          send_mail(
           subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'], 
        )
        return redirect('contact')  # Redirect to the same page after sending the email
    else:
     form = ContactUsForm()

     return render(request,
            'listings/contact.html',
            {'form': form})



def band_list(request):
   bands = Band.objects.all()
   return render(request,

           'listings/band_list.html',
           {'bands': bands})

def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request, 'listings/band_detail.html', {'band': band}) 



def about(request):
    return HttpResponse('<h1> A propos</h1> <p> Nous adorons merch !</p>')
