import datetime
import os
import requests
from dotenv import load_dotenv

load_dotenv()


class ClashAPI:
    def __init__(self):
        self.CLASH_API = os.getenv('CLASH_API')
        self.headers = {"Accept": "application/json", "Authorization": f"Bearer {self.CLASH_API}"}

    def player_info(self, player_tag: str) -> dict | bool:
        """Отримайте інформацію про одного гравця за тегом гравця.
        Теги гравців можна знайти в грі або в списках учасників клану."""
        url: str = f"https://api.clashofclans.com/v1/players/%23{player_tag.replace('#', '')}"
        info: dict = requests.get(url, headers=self.headers).json()
        try:
            if info['reason'] == 'notFound':
                return False
        except KeyError:
            return info

    def clan_info(self, clan_tag: str) -> dict | bool:
        """Get information about a single clan by clan tag. Clan tags can be found using clan search operation.
        Note that clan tags start with hash character '#' and that needs to be URL-encoded properly to work in URL,
        so for example clan tag '#2ABC' would become '%232ABC' in the URL."""
        url: str = f'https://api.clashofclans.com/v1/clans/%23{clan_tag.replace('#', '')}'
        info: dict = requests.get(url, headers=self.headers).json()
        try:
            if info['reason'] == 'notFound':
                return False
        except KeyError:
            return info

    def ccr_seasons(self, clan_tag: str) -> dict:
        """Retrieve clan's capital raid seasons"""
        url = f'https://api.clashofclans.com/v1/clans/%23{clan_tag.replace('#', '')}/capitalraidseasons'
        req = (requests.get(url, headers=self.headers).json())['items']
        return req

    def goldpass_duration(self) -> dict:
        """Get information about the current gold pass season."""
        url = 'https://api.clashofclans.com/v1/goldpass/seasons/current'
        req = requests.get(url, headers=self.headers).json()
        # start = datetime.datetime.strptime(req['startTime'], '%Y%m%dT%H%M%S.%fZ')
        # end = datetime.datetime.strptime(req['endTime'], '%Y%m%dT%H%M%S.%fZ')
        # end_days = (end - datetime.datetime.now()).days

        # return {'start_time': start.strftime('%d.%m.%Y'),
        #         'end_time': end.strftime('%d.%m.%Y'),
        #         'end_days': end_days}
        return req

    def legend_stats(self, player_tag: str) -> dict | bool:
        try:
            stats = self.player_info(player_tag)['legendStatistics']
        except KeyError:
            return False
        else:
            return stats

# print(ClashAPI().player_info('#YLQJPGQL'))
# print(ClashAPI().clan_info('#U2VLCVC'))
# print(ClashAPI().goldpass_duration())
# print(ClashAPI().legend_stats('#VGCY9ULV'))
# pprint(ClashAPI().ccr_seasons(clan_tag='#U2VLCVC'))
