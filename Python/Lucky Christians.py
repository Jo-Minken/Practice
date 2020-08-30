"""
15 Christians and 15 non-Christians shipwrecked and trapped in an island. 
Due to the lack of resourse, they decided to throw 15 ppl into the sea. 
They stood in a circle and started to count numbers from 1 to 9. 
A person who counts 9 will feed the sharks, the next person will count from 1 again, until all 15 poor guys are thown into the sea.

God bless and all 15 Christians survived!

Now write a program to figure out the position they stood at the beginning.

Hint: Try to solve the program on your own first. Imagine 30 ppl as a list of dead or alive. Only someone alive will count the number, and the person who count 9 will turn the value from alive to dead. This continues untill the total dead men pile up to 15.

Hint: Now google Josephus problem (luck Jewish though) for more information
"""

def lucky_christians():
    ppl = [True] * 30 # 30 people alive at the beginning
    number = dead = index = 0

    while dead < 15:
        is_alive = ppl[index]
        
        if is_alive:
            number += 1
            number = number % 9

            if number == 0:
                ppl[index] = False
                dead += 1
        
        index += 1
        index = index % 30
    
    # number is the count from 1 to 9, dead is the count for dead ppl, 
    # index is the index of each value in the list
    return ppl

lucky_christians()