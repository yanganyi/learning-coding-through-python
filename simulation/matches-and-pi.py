
# reference: https://www.youtube.com/watch?v=sJVivjuMfWA
# this code is a simulation of the experiment above
# we fix the match length to be 1 unit

import random
import math

def buffon_match():
    matches = 100000000
    crossed = 0
    for i in range(matches):
        y = random.random()*10000
        angle = random.random()*90

        if cross_line(y,angle):
            crossed += 1

    return matches/crossed

def cross_line(y,angle):
    # 0.5 is the half of the match length
    delta_y = (math.sin(angle / 180 * math.pi)) / 2
    top = y + delta_y
    bottom = y - delta_y

    # force it to be an integer, to improve the accuracy
    # top_int = math.floor(top)
    top_int = int(top)
    crossed = top_int > bottom and int(top_int) % 2 == 0
    return crossed


def cross_line2(y,angle):
    # 0.5 is the half of the match length
    delta_y = (math.sin(angle / 180 * math.pi)) / 2
    top = y + delta_y
    bottom = y - delta_y
    a = math.floor(top)
    b = math.ceil(bottom)
    # a==b means it crosses an integer line (say y=5 y=6)
    # a%2==0 means it crosses an even integer line (say y=6)
    crossed = a==b and (a % 2) == 0

    # print(y,angle,bottom,top,b,a,crossed)
    # print("y={:.2f}, angle={:.2f}, bottom={:.2f}, top={:.2f}, b={:.0f}, a={:.0f}, {}".format(y,angle,bottom,top,b,a,crossed))

    return crossed


print(buffon_match())
# print(cross_line(5.6,90))