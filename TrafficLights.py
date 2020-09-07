#Author: Megan West
#Title: Aneo Sponsored Puzzle: Traffic Lights
#Goal of this puzzle: You enter a section of road and you plan to rely entirely
#on your cruise control to cross through the area without having to stop or
#slow down. The goal is to find the maximum speed (without speeding) that will
#allow you to cross all the traffic lights while they are green.
#Warning: You can't cross a traffic light the second it turns red!
#Your vehicle enters the zone directly at the speed programmed on the cruise
#control which ensures that it does not change.


import sys
import math

SPEED_LIMIT_KPH = int(input())
LIGHT_COUNT = int(input())
SPEED_LIMIT_MPS = round(SPEED_LIMIT_KPH * (1000.0/3600.0), 0)


#print("Speed limit in KPH: %d" % SPEED_LIMIT_KPH)
#print("Speed limit in meters per second = %f" % SPEED_LIMIT_MPS)
#print("Number of lights = %d" % LIGHT_COUNT)

#did not choose to add input validation loops to this code.

def get_light_stats():
    stats_list = []
    distance, duration = [int(j) for j in input().split()]
    stats_list.append(distance)
    #print("distance: %d" % stats_list[0])
    stats_list.append(duration)
    #print("duration: %d" % stats_list[1])
    return stats_list

def mps_to_kph(mps):
    kph = mps * (3600/1000.0)
    return kph

def kph_to_mps(kph):
    mps = kph * (1000.0/3600)
    return mps

def get_state(speed, distance, duration):
    #if speed > 50 and speed < 80: print("speed before conversion: %f" % speed)
    mps = kph_to_mps(speed)
    #print("speed after conversion: %f" % mps)
    period = duration * 2
    #print("period is %f" % period)

    time_elapsed = distance / mps
    #print(round(time_elapsed, 2))

    while time_elapsed >= period:
        time_elapsed -= period

    if time_elapsed < (period / 2.0):
        return True
    else:
        return False

def calc_max_speed(speed, lights, light):
    if light >= LIGHT_COUNT: return speed
    if speed <= 0: return speed

    distance = lights[light][0]
    duration = lights[light][1]

    #print(speed, distance, duration)

    state = get_state(speed, distance, duration)

    #print("The state at light %d, speed %f, is %s" % (light, speed, state))

    if state == True:
        return calc_max_speed(speed, lights, light + 1)

    return calc_max_speed(speed - 1.0, lights, light = 0)

def print_max_speed(speed):

    #initialize list of lights
    lights = []

    #populate the list of lists
    for light in range(LIGHT_COUNT):
        lights.append(get_light_stats())

    #start testing using speed_limit, so that we reach max speed faster.
    max_speed = round(calc_max_speed(speed, lights, 0), 0)
    print(int(max_speed))

print_max_speed(SPEED_LIMIT_KPH)
