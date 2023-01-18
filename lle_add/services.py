import requests

from typing import Dict

NOMINATIM_API_URL = "https://nominatim.openstreetmap.org"
NOMINATIM_SEARCH_ENDPOINT = f"{NOMINATIM_API_URL}/search"

WALES_BOUNDING_BOX = "-5.5151,51.2956,-2.6870,53.5011"

query_params = {
    "namedetails": 1,
    "polygon_geojson": 1,
    "hierarchy": 1,
    "viewbox": WALES_BOUNDING_BOX,
    "bounded": 1,
}

def get_places(place_name):
    result = fetch_osm_search(query=place_name, params=query_params)
    return result

def fetch_osm_search(query: str, params: Dict[str, int]) -> dict:
    params_query = "&".join(f"{param_name}={param_value}" for param_name, param_value in params.items())
    request_url = f"{NOMINATIM_SEARCH_ENDPOINT}?q={query}&{params_query}&format=json"

    response = requests.get(request_url)
    response.raise_for_status()
    return response.json()