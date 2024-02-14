import requests
import constants
import pandas as pd

MY_STEAM_ID = "76561198168505850"


def get_owned_games(steam_id):
    ''' Returns a dataframe formatted as [appid, playtime_forever, steamid]
        containing all of the games played by the user'''
    method = 'IPlayerService/GetOwnedGames/v0001/?'
    key_param = f'key={constants.STEAM_API_KEY}'
    steam_id_param = f'steamid={steam_id}'
    res = requests.get(
        f'{constants.STEAM_API_LINK}{method}{key_param}&{steam_id_param}'
    )
    body = res.json()['response']

    df = pd.DataFrame.from_dict(body['games'])
    df.drop(
        columns=['playtime_windows_forever',
                 'playtime_mac_forever',
                 'playtime_linux_forever',
                 'rtime_last_played',
                 'playtime_disconnected',
                 'playtime_2weeks'], 
        inplace=True
    )
    df['steamid'] = steam_id
    return df

def get_user_friends(steam_id):
    ''' Returns a dataframe formatted as [appid, playtime_forever, steamid]
        containing all of the games played by the user'''
    method = 'ISteamUser/GetFriendList/v0001/?'
    key_param = f'key={constants.STEAM_API_KEY}'
    steam_id_param = f'steamid={steam_id}'
    relation_param = 'relationship=friend'
    res = requests.get(
        f'{constants.STEAM_API_LINK}{method}{key_param}&{steam_id_param}&{relation_param}'
    )
    body = res.json()['friendslist']['friends']
    df = pd.DataFrame(body)
    df.drop(
        columns=['relationship', 'friend_since'],
        inplace=True
    )
    return df