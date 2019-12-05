from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponse
from django import forms
import django_excel as excel
from .models import Listing, Realtor


class UploadFileForm(forms.Form):
    file = forms.FileField()


# Create your views here.
def import_data(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)

        def listing_func(row):
            q = Realtor.objects.filter(name=row[0])[0]
            row[0] = q
            return row
        if form.is_valid():
            realtor = Realtor.objects.get(name='Mark')
            print(request.FILES['file'].get_dict())
            request.FILES['file'].save_to_database(
                model=Listing,
                initializer=listing_func,
                mapdict=[
                    'realtor', 'title', 'address', 'city', 'state', 'zip_code', 'description', 'price', 'bedrooms',
                    'address', 'bathrooms', 'garage', 'sqft', 'lot_size', 'photo_main', 'photo_1', 'photo_2',
                    'photo_3', 'photo_4', 'photo_5', 'is_published']
            )
            return redirect('handson_view')
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(
        request,
        'listings/upload_form.html',
        {
            'form': form,
            'title': 'Import excel data into database example',
            'header': 'Please upload sample-data.xls:'
        })


def handson_table(request):
    return excel.make_response_from_a_table(Listing, 'handsontable.html')


def index(request):

    listings = Listing.objects.all()

    context = {
        'listings': listings
    }

    return render(request, 'listings/listings.html')


def listing(request):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')


