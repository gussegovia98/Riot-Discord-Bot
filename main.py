from riotwatcher import LolWatcher, ApiError
import pandas as pd


def riothandler():
    api_key = 'RGAPI-c296d748-27a8-4992-9141-487bde22f1c3'
    watcher = LolWatcher(api_key)
    my_region = 'na1'

    me = watcher.summoner.by_name(my_region, 'guss14')
    ranked_stats = watcher.league.by_summoner(my_region, me['id'])
    masteries = watcher.champion_mastery.by_summoner(my_region, me['id'])
    latest_version = watcher.data_dragon.versions_for_region(my_region)['n']['champion']
    static_champ_list = watcher.data_dragon.champions(latest_version, False, 'en_US')

    # creating champ list dictionary

    champ_dict = {}

    for key in static_champ_list['data']:
        row = static_champ_list['data'][key]
        champ_dict[row['key']] = row['id']

    # print(me)
    # print()
    print("Player Name: ", ranked_stats[0]["summonerName"])
    print("Rank: ", ranked_stats[0]["tier"], ranked_stats[0]['rank'])
    print("Top 10 champion Masteries")
    top_champs = []
    for i in range(0, 10):
        top_champs.append(masteries[i])

    for i in range(0, 10):
        print("Name:", champ_dict[str(top_champs[i]["championId"])])
        print("Champion Level:", top_champs[i]["championLevel"])
        print("Champion Points:", top_champs[i]["championPoints"])


if __name__ == '__main__':
    riothandler()
