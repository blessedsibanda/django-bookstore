from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import TemplateView, DetailView
from main import views, models, forms


urlpatterns = [
    path('about-us/', 
        TemplateView.as_view(template_name='about_us.html'),
        name="about_us"),
    path('contact-us/', 
        views.ContactUsView.as_view(),
        name="contact_us"), 
    path('products/<slug:tag>/', 
        views.ProductListView.as_view(),
        name="products"),
    path('product/<slug:slug>/',
            DetailView.as_view(model=models.Product),
            name="product"),
    path('signup/',
            views.SignUpView.as_view(),
            name="signup"),
    path('login/',
            auth_views.LoginView.as_view(
                template_name="login.html",
                form_class=forms.AuthenticationForm,
            ),
            name="login"),
    path('', 
        TemplateView.as_view(template_name='home.html'),
        name="home"), 
]