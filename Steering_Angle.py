def reward_function(params):
    '''
    Example of using steering angle
    '''

    # Read input variable
    steering = abs(params['steering_angle']) # We don't care whether it is left or right steering

    # Initialize the reward with typical value 
    reward = 1.0

    # Penalize if car steer too much to prevent zigzag
    STEERING_THRESHOLD = 20.0
    if steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    return reward
