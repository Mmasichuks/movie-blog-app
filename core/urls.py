from django.urls import path
from . import views
from . import views


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("about", views.aboutpage, name="aboutpage"),
     path("blog", views.blog, name="blog"),
      path("product", views.product, name="product"),
       path("contact", views.contact, name="contact"),
    

]
