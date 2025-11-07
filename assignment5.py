def add_player(players, scores, new_player, new_score):
    players.append(new_player)
    scores.append(new_score)

def remove_player(players, scores, player_to_remove):
    for  i in range(len(players)):
        if players[i] == player_to_remove:
            players.pop(i)
            scores.pop(i)
            return True
        else:
            return False

def get_top_players(players, scores, count):
    copy_of_players=players[:]
    copy_of_scores=scores[:]
    result = []
    for _ in range(count):
        highest_score=0
        highest_score_index=0
        for j in range(len(copy_of_scores)):
            if copy_of_scores[j]> highest_score:
                highest_score = copy_of_scores[j]
                highest_score_index = j
                
        result.append(copy_of_players[highest_score_index])
        copy_of_players.pop(highest_score_index)
        copy_of_scores.pop(highest_score_index)
    return result


def manage_leaderboard(initial_players, initial_scores, new_player_data, player_to_remove, count):
    players = initial_players[:]
    scores = initial_scores[:]
    new_player_data = add_player(players, scores, new_player, new_score)
    remove_player(players, scores, player_to_remove)
    final_result= get_top_players(players, scores, count)
    return players, final_result
players = ["ACE", "BAM", "CID", "DAZ", "EGG"]
scores = [8800, 7500, 9200, 8100, 7900]
new_player = "FIN"
new_score=9300
remove_name = "BAM"
count = 3
final_players, final_result = manage_leaderboard(players, scores, new_player, remove_name, count)
print(f"Final Players: ", final_players)
print(f"Top List: ",final_result )
