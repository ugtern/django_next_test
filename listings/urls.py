from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
    path('import_data', views.import_data, name='import_data'),
    path('handson_view', views.handson_table, name='handson_view'),
]
