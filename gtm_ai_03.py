# Guess the number baymax version
import simplegui
import random

print u"Hi,我是大白，我会玩猜数字的游戏哦"

the_bottom = 0
number_list = []
thenum_list = []
interval = 1000
i = 0
j = 0
all_list = []
guess_number = 0

# 获得玩家的范围值
def grab_range(n):
    global the_top,num
    num = int(n)
    if num <= 0:
        print u"我才不猜不大于零的数呢～"
    else:
        return num
    
# 生成一个神秘数字
def generate():
    global the_number, the_top, thenum_list
    the_top = num
    the_number = random.randint(0,the_top)
    thenum_list.append(the_number)
    return the_number

# 程序猜数字的程序：
def compare_number():
    global guess_number, the_top, the_bottom,the_number
    if guess_number < the_number and the_top - guess_number == 1:
        guess_number += 1
    else:
        guess_number = (the_bottom + the_top)/2
    number_list.append(guess_number)
#    if guess_number == the_number:
#        print u'已经猜对啦，就不要再让我猜了'
#    else:
    if guess_number < the_number :
        print u'大白猜了',guess_number, u'，可惜猜低了'
        the_bottom = guess_number
    elif guess_number > the_number:
        print u'大白猜了',guess_number, u'，可惜猜高了'
        the_top = guess_number
    else:
        print u'大白猜了',guess_number, u'，猜对啦！！！'
        all_list.append(number_list) 
    
# 回放函数
def review():
    if timer.is_running() :
        timer.stop()
    else:
        print u'大白这次猜数的全过程为：'
        timer.start()
    
# 总结作战经验
def review_all():
    print " "
    print u'在过去的几次游戏中：'
    global j, m
    m = len(all_list) 
    for record in all_list:
        if j < m:
            print u'在第', j+1, u'次猜数中，神秘数字为：', thenum_list[j]
            print u'大白一共猜了', len(all_list[j]),u'次'
            print u'猜的数字为：', all_list[j]
            j +=1
    
# 设置timer：
def timer_handler():
    global i
    l = len(number_list) - 1   
    if i <= l:        
        print u'大白第', i+1 ,u'次猜的数为', number_list[i] 
        i += 1
    else:
        print u'结束啦，就是这样'
        timer.stop()

# 重来：
def redo():
    global number_list, the_bottom,i
    the_top = num
    the_bottom = 0
    number_list = []
    i = 0
            
# create frame
frame = simplegui.create_frame("guess_number",400,400)
timer = simplegui.create_timer(interval, timer_handler)
        
# register event handlers for control elements and start frame
frame.add_input(u"给定神秘数字的范围：",grab_range, 100)
frame.add_label('   ')
frame.add_button(u"生成神秘数",generate, 100)
frame.add_label('   ')
frame.add_button(u'猜数', compare_number, 100)
frame.add_label('   ')
frame.add_button(u'再来一局', redo, 100)
frame.add_label('   ')
frame.add_label('   ')
frame.add_label('   ')
frame.add_label(u'- 回顾 - ')
frame.add_button(u'回放本次', review, 100)
frame.add_label('   ')
frame.add_button(u'总结作战经验', review_all, 100)

# start the game
frame.start()