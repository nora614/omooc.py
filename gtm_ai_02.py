# Guess the number baymax version
import simplegui
import random

print u"Hi,我是大白，我会玩猜数字的游戏哦"

the_bottom = 0
number_list = []
interval = 1000
i = 0

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
    return the_number

# 程序猜数字的程序：
def compare_number():
    global guess_number, the_top, the_bottom,the_number
    guess_number = (the_bottom + the_top)/2
    number_list.append(guess_number)
    if guess_number < the_number:
        print u'大白猜了',guess_number, u'，可惜猜低了'
        the_bottom = guess_number
    elif guess_number > the_number:
        print u'大白猜了',guess_number, u'，可惜猜高了'
        the_top = guess_number
    else:
        print u'大白猜了',guess_number, u'，猜对啦！！！'
        
# 回放函数
def review():
    if timer.is_running() :
        timer.stop()
    else:
        print u'大白这次猜数的全过程为：'
        timer.start()
    

# 设置timer：
def timer_handler():
    global l, i
    l = len(number_list) - 1   
    if i <= l:        
        print u'大白第', i+1 ,u'次猜的数为', number_list[i] 
        i += 1
    else:
        print u'结束啦，就是这样'
        timer.stop()
        
# create frame
frame = simplegui.create_frame("guess_number",200,200)
timer = simplegui.create_timer(interval, timer_handler)
        

# register event handlers for control elements and start frame
frame.add_input(u"给定一个随机数的范围：",grab_range, 100)
frame.add_label('   ')
frame.add_button(u"生成神秘数",generate, 100)
frame.add_label('   ')
frame.add_button(u'猜数', compare_number, 100)
frame.add_label('   ')
frame.add_button(u'回放', review, 100)


# start the game
frame.start()