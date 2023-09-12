def solution(players, callings):
    player_positions = {player: index for index, player in enumerate(players)}
    
    for calling in callings:
        current_position = player_positions[calling]
        previous_player = players[current_position - 1]

        player_positions[calling] -= 1
        player_positions[previous_player] += 1
        
        players[current_position] = previous_player
        players[current_position - 1] = calling
        
    return players
