def direction(facing, turn):
    allowed_direction = ('N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW')
    multiplier = 45
    if type(facing) != str or type(turn) != int:
        raise TypeError('Parameters must be (str, int)')
    if facing not in allowed_direction:
        raise ValueError('Facing must be one of the 8 directions: N, NE, E, SE, S, SW, W, NW')
    if turn > 1080 or turn < -1080 or turn % 45 != 0:
        raise ValueError('Turn must be multiple of 45, between -1080 and 1080')
    current_facing_index = allowed_direction.index(facing)
    steps_to_turn = (turn // multiplier)
    new_facing_index = (current_facing_index + steps_to_turn) % len(allowed_direction)
    return allowed_direction[new_facing_index]
