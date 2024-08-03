
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
    pokemon_enties = PokemonEntity.objects.filter(
        appeared_at__lte=timezone.now(),
        disappeared_at__gte=timezone.now()
    )

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    pokemons_on_page = []
    for pokemon in pokemons:
        try:
            pokemons_on_page.append({
                'pokemon_id': pokemon.id,
                'img_url': pokemon.image.url,
                'pokemon_name': pokemon.pokemon_name
            })
        except ValueError:
            continue

    for pokemon_entity in pokemon_enties:
        try:
            add_pokemon(
                folium_map,
                pokemon_entity.lat,
                pokemon_entity.lon,
                request.build_absolute_uri(pokemon_entity.pokemon_name.image.url)
            )
        except ValueError:
            continue

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)

    pokemon_entities = PokemonEntity.objects.filter(pokemon_name=pokemon)
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri(pokemon.image.url)
        )

    previous_evolutions = pokemon.evolutions.filter(id__lt=pokemon.id).order_by('-id')
    next_evolutions = pokemon.evolutions.filter(id__gt=pokemon.id).order_by('id')

    previous_evolution = None
    if previous_evolutions:
        previous_evolution = {
            'pokemon_name_ru': previous_evolutions.first().pokemon_name,
            'pokemon_id': previous_evolutions.first().id,
            'img_url:': request.build_absolute_uri(previous_evolutions.first().image.url)
        }

    next_evolution = None
    if next_evolutions:
        next_evolution = {
            'pokemon_name_ru': next_evolutions.first().pokemon_name,
            'pokemon_id': next_evolutions.first().id,
            'img_url': request.build_absolute_uri(next_evolutions.first().image.url)
        }

    pokemon_info = {
        'img_url': request.build_absolute_uri(pokemon.image.url),
        'pokemon_name_ru': pokemon.pokemon_name,
        'pokemon_name_en': pokemon.pokemon_name_en,
        'pokemon_name_jp': pokemon.pokemon_name_jp,
        'description': pokemon.description,
        'previous_evolution': previous_evolution,
        'next_evolution': next_evolution
    }

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(),
        'pokemon': pokemon_info
    })
