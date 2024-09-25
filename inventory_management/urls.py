from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from mainApp.views import ItemCreateView, ItemDeleteView, ItemDetailView, ItemUpdateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('items/', ItemCreateView.as_view(), name='item-create'),  # POST: Create item
    path('items/<int:id>/', ItemDetailView.as_view(), name='item-detail'),  # GET: Read item by ID
    path('items/<int:id>/update/', ItemUpdateView.as_view(), name='item-update'),
    path('items/<int:id>/delete/', ItemDeleteView.as_view(), name='item-delete'),
 
]
