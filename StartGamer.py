import random
from Level2 import *
from level3 import *
from level4 import *
from level5 import *
from level6 import *
from level7 import *
from passage1 import *
from passage2 import *
from passage3 import *
from audio1 import *
from audio2 import *
from audio3 import *
from Level_1 import level1

def GameStart(last):
    lst = [[level1, fourth_level,seventh_level, passage1, Audio2], [second_level, fifth_level, sixth_level, passage3, Audio3], 
    [third_level,fifth_level, seventh_level, passage2, Audio1],[second_level, fourth_level, sixth_level, passage3, Audio2],
    [level1, fifth_level, seventh_level, passage1, Audio2], [third_level, fourth_level, sixth_level, passage2, Audio3]]

    a = last    
    select = random.choices(lst)[0]
    nextLevel = random.choices(select)[0]
    print("--------------------------------------------------------\n",select)

    print("--------------------------------------------------------\n",nextLevel)
    select.remove(nextLevel)

    print("--------------------------After Removing------------------------------\n",select)

    # lst.remove(nextLevel)
    # if nextLevel in [Audio1, Audio2, Audio3]:
    #     if Audio2 in lst:
    #         lst.remove(Audio2)
    #     if Audio3 in lst:
    #         lst.remove(Audio3)
    #     if Audio1 in lst:
    #         lst.remove(Audio1)

    # elif nextLevel in [level1, second_level, third_level]:
    #     if level1 in lst:
    #         lst.remove(level1)
    #     if second_level in lst:
    #         lst.remove(second_level)
    #     if third_level in lst:
    #         lst.remove(third_level)
    
    # elif nextLevel in [passage1, passage2, passage3]:
    #     if passage1 in lst:
    #         lst.remove(passage1)
    #     if passage2 in lst:
    #         lst.remove(passage2)
    #     if passage3 in lst:
    #         lst.remove(passage3)

    # elif nextLevel in [fourth_level, fifth_level]:
    #     if fourth_level in lst:
    #         lst.remove(fourth_level)
    #     if fifth_level in lst:
    #         lst.remove(fifth_level)

    # elif nextLevel in [sixth_level, seventh_level]:
    #     if sixth_level in lst:
    #         lst.remove(sixth_level)
    #     if seventh_level in lst:
    #         lst.remove(seventh_level)
    nextLevel([], [], [], [], [], 0, a, select)

GameStart(1)