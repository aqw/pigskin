import pytest
import requests

from pigskin.pigskin import pigskin

gp = pigskin()


@pytest.mark.vcr()
def test_invalid_response_get_json():
    junk_url = 'https://httpbin.org/json'
    gp.config['modules']['API'] = { key: junk_url for key in gp.config['modules']['API'] }
    gp.config['modules']['ROUTES_DATA_PROVIDERS'] = { key: junk_url for key in gp.config['modules']['ROUTES_DATA_PROVIDERS'] }

    assert not gp.get_current_season_and_week()
    assert not gp.get_seasons()
    assert not gp.get_weeks(2017)
    assert not gp.get_games(2017, 'reg', 8)
    assert not gp.get_team_games('2018', '49ers')
    assert not gp.get_game_versions('2017090700', '2017')

@pytest.mark.vcr()
def test_invalid_response_get_html():
    junk_url = 'https://httpbin.org/html'
    gp.config['modules']['API'] = { key: junk_url for key in gp.config['modules']['API'] }
    gp.config['modules']['ROUTES_DATA_PROVIDERS'] = { key: junk_url for key in gp.config['modules']['ROUTES_DATA_PROVIDERS'] }

    assert not gp.get_current_season_and_week()
    assert not gp.get_seasons()
    assert not gp.get_weeks(2017)
    assert not gp.get_games(2017, 'reg', 8)
    assert not gp.get_team_games('2018', '49ers')
    assert not gp.get_game_versions('2017090700', '2017')

@pytest.mark.vcr()
def test_invalid_response_get_bytes():
    junk_url = 'https://httpbin.org/bytes/20'
    gp.config['modules']['API'] = { key: junk_url for key in gp.config['modules']['API'] }
    gp.config['modules']['ROUTES_DATA_PROVIDERS'] = { key: junk_url for key in gp.config['modules']['ROUTES_DATA_PROVIDERS'] }

    assert not gp.get_current_season_and_week()
    assert not gp.get_seasons()
    assert not gp.get_weeks(2017)
    assert not gp.get_games(2017, 'reg', 8)
    assert not gp.get_team_games('2018', '49ers')
    assert not gp.get_game_versions('2017090700', '2017')

@pytest.mark.vcr()
def test_invalid_response_post_json():
    junk_url = 'https://httpbin.org/post'
    gp.config['modules']['API'] = { key: junk_url for key in gp.config['modules']['API'] }
    gp.config['modules']['ROUTES_DATA_PROVIDERS'] = { key: junk_url for key in gp.config['modules']['ROUTES_DATA_PROVIDERS'] }

    # these POST, and as far as I can tell, httbin only provides JSON responses to POST
    # TODO: find a way to test these for html and bytes as well
    assert not gp.login(username='nope', password='so_secret')
    assert not gp.refresh_tokens()
