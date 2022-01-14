#Peter Njonde
#École secondaire catholique Renaissance
#ICS4U, Quad 4 2021-06-14
#
#Description 
#Ce programme fait un jeux de egg catcher 

from itertools import cycle #importation des modules 
from random import randrange
from tkinter import Canvas, Tk, messagebox, font
from tkinter import *
import pygame
from pygame import mixer


canvas_width = 800 
canvas_height = 400

root = Tk() # crée un windows 

root.title('Egg catcher')# donne titre aux canvas
c = Canvas(root, width=canvas_width, height=canvas_height, \
   background='deep sky blue') # fait que le ciel est bleu et mesure 800 x 400 pixels

c.create_rectangle(-5, canvas_height - 100, canvas_width + 5, \
   canvas_height + 5, fill='sea green' , width=0) #crée grass

c.create_oval(-80, -80, 120, 120, fill='orange', width=0)#crée soleil

c.pack() # dessin tout cela dans le canvas 
#mixer.init()
#pygame.mixer.music.load('music.wav')
#pygame.mixer.music.play(-1)

# fait que les couleur change
color_cycle = cycle (['light blue','light green','light pink','light yellow','light cyan']) 
# crée l'oeuf et paramiters 
egg_width = 45
texte_time = 2000
egg_height = 55
egg_score = 10 # fait que le score de chaque egg est 10 
egg_speed = 500 
egg_interval = 4000 #new egg every 4 seconds 
difficulty_factor = 0.95 # change la difilculté (plus proch de 1 le plus facile)
#créé catcher
catcher_color = 'blue'
catcher_width = 100
catcher_height = 100 # height du arc
catcher_start_x = canvas_width / 2 - catcher_width / 2 # les prochain 3 lignes sont pour faire que le
catcher_start_y = canvas_height - catcher_height - 20 # catcher est aux bas du programme 
catcher_start_x2 = catcher_start_x + catcher_width
catcher_start_y2 = catcher_start_y + catcher_height 
# draw the catcher





catcher = c.create_arc(catcher_start_x, catcher_start_y, \
                       catcher_start_x2, catcher_start_y2, start = 200, extent = 140, \
                       style = 'arc' , outline=catcher_color , width=3) 

# toute écriture sont ici
game_font = font.nametofont('TkFixedFont')#font
game_font.config(size = 18)#texte size

score = 0
score_text = c.create_text(10, 10, anchor = 'nw' , font = game_font, fill='darkblue', \
    text = 'Score: ' + str(score)) #indique score

lives_remaining = 3
lives_text = c.create_text(canvas_width - 10, 10, anchor = 'ne', font = game_font, \
    fill='darkblue' , text = 'Vie: ' + str(lives_remaining)) #indique vie
# ajoute des indicateur sur l'ecran
encoragement_text = c.create_text(canvas_width - 200, 200, anchor = 'center' , font = game_font, fill='red', \
        text = ' ' )
encoragement2_text = c.create_text(200, 200, anchor = 'center' , font = game_font, fill='red', \
        text = ' ' )
encoragement3_text = c.create_text(100, 100, anchor = 'center' , font = game_font, fill='red', \
        text = '' )
encoragement4_text = c.create_text(canvas_width - 100, 100, anchor = 'e' , font = game_font, fill='red', \
        text = '' )
warning_text = c.create_text(canvas_width - 200, 200, anchor = 'center' , font = game_font, fill='yellow', \
        text = ' ' )
warning2_text = c.create_text(200, 200, anchor = 'center' , font = game_font, fill='yellow', \
        text = ' ' )
diffilculty_text = c.create_text(canvas_width - 200, 200, anchor = 'se' , font = game_font, fill='purple', \
        text = ' ' )
#creates dark mode
def backgroud_night():
    c.config(background = 'dark blue' )
    c.itemconfigure(lives_text, fill = 'white')
    c.itemconfigure(score_text, fill = 'white')
    
button = Button(root, text = 'Mode Nuit', command = backgroud_night)# button for night 
button.pack(side = RIGHT)
button.config(font = ('Ink Free',11, 'bold'))
button.config(bg='#000000')
button.config(fg='#FFFFFF')
# creates light mode
def backgroud_light():
    c.config(background = 'deep sky blue' )
    c.itemconfigure(lives_text, fill = 'dark blue')
    c.itemconfigure(score_text, fill = 'dark blue')
    
button2 = Button(root, text = 'Mode Jours', command = backgroud_light)
button2.pack(side = RIGHT)
button2.config(font = ('Ink Free',11, 'bold'))
button2.config(bg='#1CE6F7')
button2.config(fg='#FFFFFF')


eggs = []#list for the eggs


def create_egg():
    x = randrange(10, 740) # random position of eggs 
    y = 40
    #creates oval for the eggs 
    new_egg = c.create_oval(x, y, x + egg_width, y + egg_height, fill = next(color_cycle), width=0)
    eggs.append(new_egg)#oval added to the list 
    root.after(egg_interval, create_egg)# créé les oeufs apres que 4 sec est passeé
#def reset():
#   global score
#   global lives_remaining
#   lives_remaining = 3
#   score = 0
#   c.itemconfigure(score_text, text='Score: ' + str(score))
#   c.itemconfigure(lives_text, text='Vie: ' \
#        + str(lives_remaining))
#   for egg in eggs:
#    eggs.remove(egg)
#    c.delete(egg)
   
         
#button = Button(root, text = 'Reset', command = reset)
#button.pack(side = RIGHT)


def move_eggs():
    for egg in eggs: # loops throught all the eggs 
        (egg_x, egg_y, egg_x2,egg_y2) = c.coords(egg) 
        c.move(egg, 0 , 10)# eggs moves 10 pixels second
        if egg_y2 > canvas_height:
            egg_dropped(egg)# dropped eggs so call the function
    root.after(egg_speed, move_eggs)
   

def egg_dropped(egg):
    eggs.remove(egg) # takes the egg fallent out of the list
    c.delete(egg)
    lose_a_life()
    if lives_remaining == 0:
        messagebox.showinfo('Game Over!' , 'Final Score: ' \
            + str(score)) #affice your final score
        root.destroy()# ends game
 # enleve la vie
def lose_a_life():
    global lives_remaining
    lives_remaining -= 1
    c.itemconfigure(lives_text, text='Vie: ' \
        + str(lives_remaining))
    if lives_remaining == 2:
         c.itemconfigure(encoragement_text, text = '')
         c.itemconfigure(encoragement2_text, text = '')
         c.itemconfigure(encoragement3_text, text = '')
         c.itemconfigure(encoragement4_text, text = '')
         c.itemconfigure(warning_text, text = 'Fait Attention')
    if lives_remaining == 1:
         c.itemconfigure(encoragement_text, text = '')
         c.itemconfigure(encoragement2_text, text = '')
         c.itemconfigure(encoragement3_text, text = '')
         c.itemconfigure(warning_text, text = '')
         c.itemconfigure(encoragement4_text, text = '')
         c.itemconfigure(warning2_text, text = '1 Vie qui reste')

def check_catch(): #donne des points
    (catcher_x, catcher_y, catcher_x2, catcher_y2) = c.coords(catcher)# verifie que egg est attrapeé
    for egg in eggs:
        (egg_x, egg_y,egg_x2,egg_y2) = c.coords(egg)
        if catcher_x < egg_x and egg_x2 < catcher_x2 and catcher_y2 - egg_y2 < 40:
            eggs.remove(egg)
            c.delete(egg)
            increase_score(egg_score)
    root.after(100, check_catch)

     # hard mode  
def niveux3():
    global difficulty_factor
    difficulty_factor -= 0.20
    if difficulty_factor == 0.75:
        c.itemconfigure(diffilculty_text, text = 'Attention sa va allez plus vite ')

btn3 = Button(root, text = "Mode impossible", command = niveux3)
btn3.config(font = ('Ink Free',11, 'bold'))
btn3.config(bg='#ff6200')
btn3.config(fg='#fffb1f')

btn3.pack(side = LEFT)

def increase_score(points):
   
    global score, egg_speed, egg_interval
    score += points
    egg_speed = int(egg_speed * difficulty_factor)
    egg_interval = int(egg_interval * difficulty_factor)
    c.itemconfigure(score_text, text='Score: ' + str(score))
    if score == 30:
     c.itemconfigure(encoragement_text, text = 'WOW!')
     c.itemconfigure(warning_text, text = '')
     c.itemconfigure(warning2_text, text = '')
     c.itemconfigure(diffilculty_text, text = '')
    if score == 70:
         c.itemconfigure(encoragement_text, text = '')
         c.itemconfigure(warning_text, text = '')
         c.itemconfigure(warning2_text, text = '')
         c.itemconfigure(diffilculty_text, text = '')
         c.itemconfigure(encoragement2_text, text = 'CONTINUE!!')
         
         
    if score == 100:
         c.itemconfigure(encoragement_text, text = '')
         c.itemconfigure(encoragement2_text, text = '')
         c.itemconfigure(warning_text, text = '')
         c.itemconfigure(warning2_text, text = '')
         c.itemconfigure(diffilculty_text, text = '')
         c.itemconfigure(encoragement3_text, text = 'EXCELLENT!')
    if score == 140:
         c.itemconfigure(encoragement_text, text = '')
         c.itemconfigure(encoragement2_text, text = '')
         c.itemconfigure(warning_text, text = '')
         c.itemconfigure(warning2_text, text = '')
         c.itemconfigure(encoragement3_text, text = '')
         c.itemconfigure(diffilculty_text, text = '')
         c.itemconfigure(encoragement4_text, text = 'SUPERBE!!')

 #bouge le panier 
def move_left(event):
    (x1, y1, x2,y2) = c.coords(catcher)
    if x1 > 0:
        c.move(catcher, -20, 0)
def move_right(event):
     (x1, y1, x2,y2) = c.coords(catcher)
     if x2 < canvas_width:
         c.move(catcher, 20, 0)

c.bind('<Left>', move_left)
c.bind('<Right>', move_right)
c.focus_set()



root.after(1000, create_egg)
root.after(1000, move_eggs)
root.after(1000, check_catch)
root.mainloop()

        
                    
                            
                    

                           