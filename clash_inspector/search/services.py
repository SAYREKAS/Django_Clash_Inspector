import os
import requests
from dotenv import load_dotenv

load_dotenv()


class ClashAPI:
    def __init__(self):
        self.CLASH_API = os.getenv('CLASH_API')
        self.headers = {"Accept": "application/json", "Authorization": f"Bearer {self.CLASH_API}"}

    def player_info(self, player_tag: str) -> dict | bool:
        url: str = f"https://api.clashofclans.com/v1/players/%23{player_tag.replace('#', '')}"
        info: dict = requests.get(url, headers=self.headers).json()
        try:
            if info['reason'] == 'notFound':
                return False
        except KeyError:
            return info

    def clan_info(self, clan_tag: str) -> dict | bool:
        url: str = f'https://api.clashofclans.com/v1/clans/%23{clan_tag.replace('#', '')}'
        info: dict = requests.get(url, headers=self.headers).json()
        try:
            if info['reason'] == 'notFound':
                return False
        except KeyError:
            return info

    def ccr_seasons(self, clan_tag: str) -> dict:
        url = f'https://api.clashofclans.com/v1/clans/%23{clan_tag.replace('#', '')}/capitalraidseasons'
        req = (requests.get(url, headers=self.headers).json())['items']
        return req

    def goldpass_duration(self) -> dict:
        url = 'https://api.clashofclans.com/v1/goldpass/seasons/current'
        req = requests.get(url, headers=self.headers).json()
        return req

    def legend_stats(self, player_tag: str) -> dict | bool:
        try:
            stats = self.player_info(player_tag)['legendStatistics']
        except KeyError:
            return False

        return stats

    def search_clans(self, name: str, location_id: int = None, min_members: int = None, max_members: int = None,
                     min_clan_points: int = None, min_clan_level: int = None, limit: int = None) -> dict | bool:

        params = {
            'name': name,
            'locationId': location_id,
            'minMembers': min_members,
            'maxMembers': max_members,
            'minClanPoints': min_clan_points,
            'minClanLevel': min_clan_level,
            'limit': limit
        }

        params = {k: v for k, v in params.items() if v}

        url = 'https://api.clashofclans.com/v1/clans'

        try:
            req = requests.get(url, headers=self.headers, params=params).json()
            if req.get('reason') == 'badRequest':
                return False
            else:
                return req['items']
        except Exception as ex:
            print(f"An error occurred: {ex}")
            return False

# print(ClashAPI().player_info('#YLQJPGQL'))
# print(ClashAPI().clan_info('#U2VLCVC'))
# print(ClashAPI().goldpass_duration())
# print(ClashAPI().legend_stats('#VGCY9ULV'))
# print(ClashAPI().ccr_seasons(clan_tag='#U2VLCVC'))
# print(ClashAPI().search_clans(name='otamani'))
