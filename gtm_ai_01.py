# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

print"hi,let's play guess number!"

the_bottom = 0


# 获得玩家的范围值
def grab_range(n):
    global the_top
    num = int(n)
    if num <= 0:
        print u"我才不猜不大于零的数呢～"
    else:
        the_top = num
        return the_top

# 生成一个神秘数字
def generate():
    global the_number, the_top
    the_number = random.randint(0,the_top)
    print the_number
    return the_number

# 程序猜数字的程序：
def compare_number():
    global guess_number, the_top, the_bottom,the_number
    guess_number = (the_bottom + the_top)/2
    if guess_number < the_number:
        print u'大白猜的低了'
        the_bottom = guess_number
        print the_bottom
    elif guess_number > the_number:
        print u'大白猜的高了'
        the_top = guess_number
        print the_top
    else:
        print u'大白猜对啦！！！'
    pass    

    
# create frame
frame = simplegui.create_frame("guess_number",200,200)


# register event handlers for control elements and start frame
frame.add_input(u"给定一个随机数的范围：",grab_range, 100)
frame.add_label('   ')
frame.add_button(u"生成神秘数",generate, 100)
frame.add_label('   ')
frame.add_button(u'猜数', compare_number, 100)


# start the game
frame.start()