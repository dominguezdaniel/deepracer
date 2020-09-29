import math
def reward_function(params):
'''
Use square root for center line
'''
track_width = params['track_width']
distance_from_center = params['distance_from_center']
steering = abs(params['steering_angle'])
speed = params['speed']
all_wheels_on_track = params['all_wheels_on_track']
ABS_STEERING_THRESHOLD = 15
reward = 1 - (distance_from_center / (track_width/2))**(4)
if reward < 0:
reward = 0
if steering > ABS_STEERING_THRESHOLD:
reward *= 0.8
if not (all_wheels_on_track):
reward = 0
return float(reward)
