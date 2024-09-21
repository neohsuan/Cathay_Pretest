import requests
import pytest
import re
import urllib3

# Disable SSL verification related warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Apply warning filter to all tests in this file
pytestmark = pytest.mark.filterwarnings("ignore::urllib3.exceptions.InsecureRequestWarning")

BASE_URL = "https://swapi.dev/api/films/"

# Test Case 1: Verify the response for /films/
def test_films_response():
    response = requests.get(BASE_URL, verify=False)
    assert response.status_code == 200

    json_data = response.json()
    
    # Check if the response contains the 'results' field and that it's an array
    assert 'results' in json_data
    assert isinstance(json_data['results'], list)

    # Verify that each film in 'results' contains the required key fields
    for film in json_data['results']:
        assert 'title' in film
        assert 'episode_id' in film
        assert 'opening_crawl' in film
        assert 'director' in film
        assert 'producer' in film
        assert 'release_date' in film
        assert 'species' in film
        assert 'starships' in film
        assert 'vehicles' in film
        assert 'characters' in film
        assert 'planets' in film
        assert 'url' in film
        assert 'created' in film
        assert 'edited' in film

# Test Case 2: Verify HEAD request returns correct status code and headers
def test_films_head_request():
    response = requests.head(BASE_URL, verify=False)
    assert response.status_code == 200

    # Verify that required headers are present
    headers = response.headers
    assert 'Server' in headers
    assert 'Date' in headers
    assert 'Content-Type' in headers
    assert 'Connection' in headers
    assert 'Vary' in headers
    assert 'X-Frame-Options' in headers
    assert 'ETag' in headers
    assert 'Allow' in headers
    assert 'Strict-Transport-Security' in headers

# Test Case 3: Verify OPTIONS Request Returns Supported Data Formats
def test_options_request_formats():
    response = requests.options(BASE_URL, verify=False)
    assert response.status_code == 200

    json_data = response.json()

    # Test if 'renders' field exists and contains expected response formats
    assert 'renders' in json_data
    assert 'application/json' in json_data['renders']
    assert 'text/html' in json_data['renders']

    # Test if 'parses' field exists and contains expected request formats
    assert 'parses' in json_data
    assert 'application/json' in json_data['parses']
    assert 'application/x-www-form-urlencoded' in json_data['parses']
    assert 'multipart/form-data' in json_data['parses']

# Test Case 4: Verify Title Field Type
def test_title_field_type():
    response = requests.get(BASE_URL, verify=False)
    assert response.status_code == 200

    json_data = response.json()

    # Check if each film in 'results' contains a 'title' field
    for film in json_data['results']:
        assert 'title' in film
        assert isinstance(film['title'], str)  # Check if 'title' is a string

# Test Case 5: Verify episode_id Field Type
def test_episode_id_field_type():
    response = requests.get(BASE_URL, verify=False)
    assert response.status_code == 200

    json_data = response.json()

    # Check if each film in 'results' contains an 'episode_id' field
    for film in json_data['results']:
        assert 'episode_id' in film
        # Check if 'episode_id' is an integer
        assert isinstance(film['episode_id'], int)

# Test Case 6: Verify opening_crawl Field Type
def test_opening_crawl_field_type():
    response = requests.get(BASE_URL, verify=False)
    json_data = response.json()

    # Check if the 'opening_crawl' field is of type string
    for film in json_data['results']:
        assert isinstance(film['opening_crawl'], str)

# Test Case 7: Verify director Field Type
def test_director_field_type():
    response = requests.get(BASE_URL, verify=False)
    json_data = response.json()

    # Check if the 'director' field is of type string
    for film in json_data['results']:
        assert isinstance(film['director'], str)

# Test Case 8: Verify producer Field Type
def test_producer_field_type():
    response = requests.get(BASE_URL, verify=False)
    json_data = response.json()

    # Check if the 'producer' field is of type string
    for film in json_data['results']:
        assert isinstance(film['producer'], str)

# Test Case 9: Verify release_date Field Type and Format
def test_release_date_field_type_and_format():
    response = requests.get(BASE_URL, verify=False)
    json_data = response.json()

    # Check if the 'release_date' can be parsed as a valid date and is in ISO 8601 format
    for film in json_data['results']:
        # Verify if it can be parsed as a date
        try:
            parsed_date = film['release_date']  # YYYY-MM-DD format
            assert len(parsed_date) == 10  # Check format length
        except ValueError:
            assert False, f"Invalid date format in {film['release_date']}"

        # Verify the format using regex
        assert re.match(r"^\d{4}-\d{2}-\d{2}$", film['release_date'])

# Test Case 10: Verify species Field Type
def test_species_field_type():
    response = requests.get(BASE_URL, verify=False)
    json_data = response.json()

    # Check if the 'species' field is an array
    for film in json_data['results']:
        assert isinstance(film['species'], list)  # Ensure 'species' is of type array

# Test Case 11: Verify starships Field Type
def test_starships_field_type():
    response = requests.get(BASE_URL, verify=False)
    json_data = response.json()

    # Check if the 'starships' field is an array
    for film in json_data['results']:
        assert isinstance(film['starships'], list)  # Ensure 'starships' is of type array

# Test Case 12: Verify vehicles Field Type
def test_vehicles_field_type():
    response = requests.get(BASE_URL, verify=False)
    json_data = response.json()

    # Check if the 'vehicles' field is an array
    for film in json_data['results']:
        assert isinstance(film['vehicles'], list)  # Ensure 'vehicles' is of type array

# Test Case 13: Verify characters Field Type
def test_characters_field_type():
    response = requests.get(BASE_URL, verify=False)
    json_data = response.json()

    # Check if the 'characters' field is an array
    for film in json_data['results']:
        assert isinstance(film['characters'], list)  # Ensure 'characters' is of type array

# Test Case 14: Verify planets Field Type
def test_planets_field_type():
    response = requests.get(BASE_URL, verify=False)
    json_data = response.json()

    # Check if the 'planets' field is an array
    for film in json_data['results']:
        assert isinstance(film['planets'], list)  # Ensure 'planets' is of type array

# Test Case 15: Verify url Field Type
def test_url_field_type():
    response = requests.get(BASE_URL, verify=False)
    json_data = response.json()

    # Check if the 'url' field is a string
    for film in json_data['results']:
        assert isinstance(film['url'], str)  # Ensure 'url' is of type string

# Test Case 16: Verify created Field Type and Format
def test_created_field_type_and_format():
    response = requests.get(BASE_URL, verify=False)
    json_data = response.json()

    # Check if the 'created' field is a string and in ISO 8601 format
    for film in json_data['results']:
        assert isinstance(film['created'], str)  # Ensure 'created' is of type string
        assert re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{1,6}Z$", film['created'])

# Test Case 17: Verify edited Field Type and Format
def test_edited_field_type_and_format():
    response = requests.get(BASE_URL, verify=False)
    json_data = response.json()

    # Check if the 'edited' field is a string and in ISO 8601 format
    for film in json_data['results']:
        assert isinstance(film['edited'], str)  # Ensure 'edited' is of type string
        assert re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{1,6}Z$", film['edited'])

# Test Case 18: Verify the response for /films/1
def test_films_1_status_code():
    response = requests.get(BASE_URL + '1/', verify=False)
    assert response.status_code == 200  # Ensure the status code is 200 OK

# Test Case 19: Verify Title, Episode ID, Opening Crawl, Director, Producer, and URL
def test_films_1_details():
    response = requests.get(BASE_URL + '1/', verify=False)
    json_data = response.json()

    # Check if the title, episode_id, opening_crawl, director, producer, and url are correct
    assert json_data['title'] == "A New Hope"
    assert json_data['episode_id'] == 4
    assert "It is a period of civil war." in json_data['opening_crawl']
    assert json_data['director'] == "George Lucas"
    assert json_data['producer'] == "Gary Kurtz, Rick McCallum"
    assert json_data['url'] == "https://swapi.dev/api/films/1/"

# Test Case 20: Verify Species, Starships, Vehicles, Characters, and Planets URLs
def test_films_1_urls():
    response = requests.get(BASE_URL + '1/', verify=False)
    json_data = response.json()

    # Expected prefixes for each array
    expected_prefixes = {
        'characters': "https://swapi.dev/api/people/",
        'planets': "https://swapi.dev/api/planets/",
        'starships': "https://swapi.dev/api/starships/",
        'vehicles': "https://swapi.dev/api/vehicles/",
        'species': "https://swapi.dev/api/species/"
    }

    # Verify characters URLs
    for url in json_data['characters']:
        assert url.startswith(expected_prefixes['characters']), f"Invalid character URL: {url}"

    # Verify planets URLs
    for url in json_data['planets']:
        assert url.startswith(expected_prefixes['planets']), f"Invalid planet URL: {url}"

    # Verify starships URLs
    for url in json_data['starships']:
        assert url.startswith(expected_prefixes['starships']), f"Invalid starship URL: {url}"

    # Verify vehicles URLs
    for url in json_data['vehicles']:
        assert url.startswith(expected_prefixes['vehicles']), f"Invalid vehicle URL: {url}"

    # Verify species URLs
    for url in json_data['species']:
        assert url.startswith(expected_prefixes['species']), f"Invalid species URL: {url}"

# Test Case 21: Verify Release Date, Created, and Edited Fields Content
def test_films_1_dates():
    response = requests.get(BASE_URL + '1/', verify=False)
    json_data = response.json()

    # Check if release_date is correct
    assert json_data['release_date'] == "1977-05-25", f"Unexpected release date: {json_data['release_date']}"

    # Check if created date is correct
    assert json_data['created'] == "2014-12-10T14:23:31.880000Z", f"Unexpected created date: {json_data['created']}"

    # Check if edited date is correct
    assert json_data['edited'] == "2014-12-20T19:49:45.256000Z", f"Unexpected edited date: {json_data['edited']}"

# Test Case 22: Verify Response Time
def test_films_1_response_time():
    response = requests.get(BASE_URL + '1/', verify=False)
    # Verify that the response time is less than 500 milliseconds
    assert response.elapsed.total_seconds() < 0.5, f"Response time exceeded 500ms: {response.elapsed.total_seconds()} seconds"

# Test Case 23: Verify POST Method Is Not Allowed for /films
def test_post_method_not_allowed_for_films():
    response = requests.post(BASE_URL, verify=False)
    # Verify that the status code is 405 Method Not Allowed
    assert response.status_code == 405, f"Expected status code 405, but got {response.status_code}"

# Test Case 24: Verify PUT Method Is Not Allowed for /films
def test_put_method_not_allowed_for_films():
    response = requests.put(BASE_URL, verify=False)
    # Verify that the status code is 405 Method Not Allowed
    assert response.status_code == 405, f"Expected status code 405, but got {response.status_code}"

# Test Case 25: Verify DELETE Method Is Not Allowed for /films
def test_delete_method_not_allowed_for_films():
    response = requests.delete(BASE_URL, verify=False)
    # Verify that the status code is 405 Method Not Allowed
    assert response.status_code == 405, f"Expected status code 405, but got {response.status_code}"

# Test Case 26: Verify PATCH Method Is Not Allowed for /films
def test_patch_method_not_allowed_for_films():
    response = requests.patch(BASE_URL, verify=False)
    # Verify that the status code is 405 Method Not Allowed
    assert response.status_code == 405, f"Expected status code 405, but got {response.status_code}"

# Test Case 27: Verify Handling of Invalid Film ID /films/7
def test_invalid_film_id_7():
    response = requests.get(BASE_URL + '7/', verify=False)
    # Check if the status code is 404 for invalid IDs
    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"
    json_data = response.json()

    # Validate error message in the response body (optional)
    assert json_data['detail'] == "Not found", f"Expected error message 'Not found', but got {json_data['detail']}"

# Test Case 28: Verify Handling of Invalid Film ID /films/999
def test_invalid_film_id_999():
    response = requests.get(BASE_URL + '999/', verify=False)
    # Check if the status code is 404 for invalid IDs
    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"
    json_data = response.json()

    # Validate error message in the response body (optional)
    assert json_data['detail'] == "Not found", f"Expected error message 'Not found', but got {json_data['detail']}"

# Test Case 29: Verify Handling of Invalid Film ID /films/-1
def test_invalid_film_id_minus_1():
    response = requests.get(BASE_URL + '-1/', verify=False)
    # Check if the status code is 404 for invalid IDs
    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"
    json_data = response.json()

    # Validate error message in the response body (optional)
    assert json_data['detail'] == "Not found", f"Expected error message 'Not found', but got {json_data['detail']}"
