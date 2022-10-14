import curses
import time
import random
from curses import wrapper

def start_scr(stdscr):
    stdscr.clear() 
    stdscr.addstr( 0,0, "Bienvenue dans WPM !",curses.color_pair(3))
    stdscr.addstr("\nAppuyer sur n'importe quel touche pour commencer ...",curses.color_pair(3))
    stdscr.refresh()

    stdscr.getkey()

def end_scr(stdscr):
    stdscr.clear() 
    stdscr.addstr( 0,0, "Vous allez quitter le programme",curses.color_pair(3))
    stdscr.addstr("\nVoulez vous continuer ? Y/N",curses.color_pair(3))
    stdscr.refresh()

    key = stdscr.getkey()

    if ord(key) == 89: # C'est oui
        pass
    else: #c'est non
        wpm_test(stdscr)



def display_text(stdscr, target, typed_text, wpm=0):
        stdscr.clear()
        stdscr.addstr(target,curses.color_pair(3))
        stdscr.addstr(3,0, f"WPM: {wpm}")

        for i, char in enumerate(typed_text):
            if target[i] == typed_text[i]:
                stdscr.addstr(0,i, char,curses.color_pair(1))
            else:
                stdscr.addstr(0,i, char,curses.color_pair(2))
        stdscr.refresh()

def wpm_test(stdscr):
    i=0
    while i < 1:
        with open(r"target.txt", 'r',encoding="utf-8") as f:
            for count, line in enumerate(f):
                pass
        f = open("target.txt", 'r', encoding="utf-8")
        target = f.readlines()
        target = target[random.randrange(1,count)]
        target = target[:-1]
        f.close

        typed_text = []
        wpm = 0

        start_time= time.time()

        stdscr.refresh
        while True:

            time_elapsed = max(time.time() - start_time,1)
            wpm = round((len(typed_text) / (time_elapsed / 60))/5)

            display_text(stdscr,target,typed_text,wpm)

            key = stdscr.getkey()

            if ord(key) == 27:
                i+=1
                break
            elif key in ["KEY_BACKSPAXE",'\b',"\x7f"]:
                if len(typed_text) > 0:
                    typed_text.pop()
            elif len(typed_text) < len(target):
                typed_text.append(key)
            elif len(typed_text) == len(target):
                break
    end_scr(stdscr)

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    stdscr.keypad(False)




    
    start_scr(stdscr)
    wpm_test(stdscr)



wrapper(main)
