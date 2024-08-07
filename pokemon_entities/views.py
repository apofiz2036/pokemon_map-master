
import folium

from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Pokemon, PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons = Pokemon.objects.all()

    now = timezone.now()

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    pokemons_on_page = []
    for pokemon in pokemons:
        try:
            pokemons_on_page.append({
                'pokemon_id': pokemon.id,
                'img_url': pokemon.image.url,
                'title_ru': pokemon.name_ru
            })
        except ValueError:
            continue

    pokemon_entities = PokemonEntity.objects.filter(
        appeared_at__lte=now,
        disappeared_at__gte=now
    )

    for pokemon_entity in pokemon_entities:
        try:
            add_pokemon(
                folium_map,
                pokemon_entity.lat,
                pokemon_entity.lon,
                request.build_absolute_uri(pokemon_entity.pokemon.image.url)
            )
        except ValueError:
            continue

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)

    pokemon_entities = PokemonEntity.objects.filter(pokemon=pokemon)
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri(pokemon.image.url)
        )

    previous_evolutions = pokemon.prev_evolution
    next_evolutions = pokemon.next_evolutions.first()

    previous_evolution = None
    if previous_evolutions:
        previous_evolution = {
            'name_ru': pokemon.prev_evolution.name_ru,
            'pokemon_id': pokemon.prev_evolution.id,
            'img_url': request.build_absolute_uri(pokemon.prev_evolution.image.url)
        }

    next_evolution = None
    if next_evolutions:
        next_evolution = {
            'name_ru': next_evolutions.name_ru,
            'pokemon_id': next_evolutions.id,
            'img_url': request.build_absolute_uri(next_evolutions.image.url)
        }

    pokemon_info = {
        'img_url': request.build_absolute_uri(pokemon.image.url),
        'title_ru': pokemon.name_ru,
        'title_en': pokemon.name_en,
        'title_jp': pokemon.name_jp,
        'description': pokemon.description,
        'previous_evolution': previous_evolution,
        'next_evolution': next_evolution
    }

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(),
        'pokemon': pokemon_info
    })
