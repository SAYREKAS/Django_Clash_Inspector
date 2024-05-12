from django.urls import path
from search.views import search_page, player_search, about_player, clan_search, about_clan, name_search

urlpatterns = (
    [path('', search_page, name='search'),

     path('player/', player_search, name='player_search'),
     path('player/<str:player_tag>/', about_player, name='player'),

     path('clan/', clan_search, name='clan_search'),
     path('clan/<str:clan_tag>/', about_clan, name='clan'),
     path('name_search', name_search, name='name_search'),
     ]
)
