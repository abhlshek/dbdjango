from django.contrib import admin
from django.urls import path
from. import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('book/',views.book),
    path('',views.index),
    path('between/',views.between),
    path('searchbooks/',views.searchbooks),
    path('searchor/',views.searchor),
    path('aggregates/',views.aggregates),
    path('betweens/',views.betweens),
    path('allbooks/',views.allbooks),
    path('aggregate/',views.aggregate),
    path('books/',views.books),
    path('drop/',views.drop),
    path('delete/',views.delete),
    path("insert/",views.insert),
    path('search1/',views.search1),
    path('remove/',views.remove),
    path('update/',views.update),
    path('bank/',views.bank),
    path('searchbank/',views.searchbank),
    path('searchaccount/',views.searchaccount),
    path('deleteaccount/',views.deleteaccount),
    path('updateaccount/',views.updateaccount),
    path('moviesearch/',views.moviesearch),
    path('readexcle/',views.readexcle),
    path('test/',views.test),
    path('GetAccount/',views.GetAccount)
]