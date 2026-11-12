from django.urls import path
from . import views
urlpatterns=[
 path('',views.home,name='home'),path('about/',views.about,name='about'),path('contact/',views.contact,name='contact'),
 path('signup/',views.signup,name='signup'),path('login/',views.signin,name='login'),path('logout/',views.signout,name='logout'),
 path('dealer/<int:dealer_id>/',views.dealer_page,name='dealer'),path('dealer/<int:dealer_id>/review/',views.post_review,name='post_review'),
 path('get_dealers/',views.dealers_api,name='get_dealers'),path('get_dealers/<str:state>/',views.dealers_api,name='get_dealers_state'),
 path('get_cars/',views.cars_api,name='get_cars'),path('reviews/dealer/<int:dealer_id>/',views.reviews_api,name='reviews'),
 path('sentiment/<path:text>/',views.sentiment_api,name='sentiment'),
]
