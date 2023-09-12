def solution(players, callings):
    player_indices = {player: index for index, player in enumerate(players)}
    
    for call in callings:
        call_index = player_indices[call]
        previous_player = players[call_index - 1]

        player_indices[call] -= 1
        player_indices[previous_player] += 1
        
        players[call_index] = previous_player
        players[call_index - 1] = call
        
    return players
