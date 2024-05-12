from django.shortcuts import render, redirect

from search.services import ClashAPI
from galery.models import HeroImages


def search_page(request):
    goldpass_duration = ClashAPI().goldpass_duration()
    context: dict = {
        'title': 'Пошук',
        'goldpass_duration': goldpass_duration,
    }
    return render(request, 'search/search.html', context)


def player_search(request):
    if request.method == 'POST':
        player_tag = request.POST.get('player_tag').replace('#', '')
        return redirect('player', player_tag=player_tag)


def about_player(request, player_tag):
    player_info: dict = ClashAPI().player_info(player_tag)
    if not player_info:
        return render(request, 'search/search.html', {'player_error': f"Гравця з тегом '{player_tag}' не існує"})
    else:
        legendary_stats: dict = ClashAPI().legend_stats(player_tag)
        hero_images = HeroImages.objects.all()
        context: dict = {
            'title': 'Пошук гравця',
            'player_info': player_info,
            'legendary_stats': legendary_stats,
            'hero_images': hero_images,
            'exclude_keys': ['achievements', 'labels', 'troops', 'heroes', 'heroEquipment', 'spells',
                             'playerHouse', 'legendStatistics'],
        }
        return render(request, 'search/about_player.html', context)


def clan_search(request):
    if request.method == 'POST':
        clan_tag = request.POST.get('clan_tag').replace('#', '')
        return redirect('clan', clan_tag=clan_tag)


def about_clan(request, clan_tag):
    clan_info: dict = ClashAPI().clan_info(clan_tag)
    if not clan_info:
        return render(request, 'search/search.html', {'clan_error': f"Клану з тегом '{clan_tag}' не існує"})
    else:
        ccr: dict = ClashAPI().ccr_seasons(clan_tag)
        context: dict = {
            'title': 'Пошук клану',
            'clan_info': clan_info,
            'ccr': ccr,
            'exclude_main': ['memberList', 'labels', 'badgeUrls', 'clanCapital', ],
            'exclude_ccr': ['members', 'attackLog', 'defenseLog', ],
        }
        return render(request, 'search/about_clan.html', context)


def name_search(request):
    api = ClashAPI()
    if request.method == 'GET':
        clan_name = request.GET.get('clan_name')
        min_clan_points = request.GET.get('min_clan_points')
        limit = request.GET.get('limit')
        min_clan_level = request.GET.get('min_clan_level')
        min_members = request.GET.get('min_members')
        max_members = request.GET.get('max_members')
        clan_info = api.search_clans(clan_name, min_clan_points=min_clan_points, limit=limit, min_members=min_members,
                                     min_clan_level=min_clan_level, max_members=max_members)
        if clan_info:
            context = {'clan_info': clan_info}
            return render(request, 'search/about_clan_name.html', context)

    return render(request, 'search/about_clan_name.html')
