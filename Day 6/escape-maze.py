while (not at_goal()):
    if (front_is_clear() and not right_is_clear()):
        move()
    else:
        if (not right_is_clear()):
            turn_left()
        else:
            turn_left()
            turn_left()
            turn_left()
            move()
