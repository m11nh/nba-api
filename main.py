from nba_api.stats.endpoints import commonplayerinfo
import json 

# Basic Request
player_info = commonplayerinfo.CommonPlayerInfo(player_id=2544)
player_info = json.loads(player_info.get_json())

print(player_info['resultSets'])
