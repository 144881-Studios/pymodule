source = r"""import sys as _py
import time as _time
import colorama as _color
import os as _os
_os.system("pip install colorama")
def printf(*var) :
    for i in list(var) :
        print(i,end="")
        _py.stdout.flush()
def fun(line,sec) :
    if type(line) != list :
        line = list(str(line))
    for i in line :
        printf(i)
        _time.sleep(sec)
def loadsign(main="█",half="▌",fill=" ",grid=10,amaintime=1,showperplace=None,tip="") : # ▌█
    ishalf = True
    for i in range(grid*2+1) :
        ishalf = not(ishalf)
        printf(main*(i//2))
        if ishalf :
            printf(half)
        printf(fill*(grid*2-i))
        if showperplace == None :
            printf(tip+"\r")
        else :
            printf(str(round(i/2/grid*100,showperplace))+"%"+tip+"\r")
        if i < grid*2 :
            _time.sleep(amaintime/2)
    print()
def Traceback(Info=None,Type=RuntimeError,Warn=None,Fakesign=False) :
    if Fakesign :
        if Type != SyntaxError :
            print("Traceback (most recent call last):")
        if Info != None :
            print(Info)
        if Warn == None :
            print(str(Type)[8:-2])
        else :
            print(str(Type)[8:-2]+": "+Warn)
    else :
        raise Type(Warn)
class color :
    def space(line) :
        lib = {"0":_color.Back.BLACK,"1":_color.Back.BLUE,"2":_color.Back.GREEN,"3":_color.Back.CYAN,"4":_color.Back.RED,"5":_color.Back.MAGENTA,"6":_color.Back.YELLOW,"7":_color.Back.WHITE,"8":_color.Back.RESET}
        for i in line :
            printf(lib[i]+" ")
    def printc(foreColor,backColor,*var,_sep=" ",_end="\n") : # foreColor and backColor use binary RGB numbers like “0b110” to represents YELLOW color.
        lib = [_color.Fore.BLACK,_color.Fore.BLUE,_color.Fore.GREEN,_color.Fore.CYAN,_color.Fore.RED,_color.Fore.MAGENTA,_color.Fore.YELLOW,_color.Fore.WHITE,_color.Fore.RESET]
        printf(lib[foreColor])
        lib = [_color.Back.BLACK,_color.Back.BLUE,_color.Back.GREEN,_color.Back.CYAN,_color.Back.RED,_color.Back.MAGENTA,_color.Back.YELLOW,_color.Back.WHITE,_color.Back.RESET]
        printf(lib[backColor])
        for i in list(var) :
            print(i,end=_sep)
        printf(_end)
    class pixel :
        def image(pixels,*var) : # 2D paint: like a tuple ("777","707","777")
            for h in list(var) :
                for i in range(pixels) :
                    for v in h :
                        color.space(v*(pixels*2))
                    print()"""
import sys as _py
import time as _time
import colorama as _color
import os as _os
_os.system("pip install colorama")
def printf(*var) :
    for i in list(var) :
        print(i,end="")
        _py.stdout.flush()
def fun(line,sec) :
    if type(line) != list :
        line = list(str(line))
    for i in line :
        printf(i)
        _time.sleep(sec)
def loadsign(main="█",half="▌",fill=" ",grid=10,amaintime=1,showperplace=None,tip="") : # ▌█
    ishalf = True
    for i in range(grid*2+1) :
        ishalf = not(ishalf)
        printf(main*(i//2))
        if ishalf :
            printf(half)
        printf(fill*(grid*2-i))
        if showperplace == None :
            printf(tip+"\r")
        else :
            printf(str(round(i/2/grid*100,showperplace))+"%"+tip+"\r")
        if i < grid*2 :
            _time.sleep(amaintime/2)
    print()
def Traceback(Info=None,Type=RuntimeError,Warn=None,Fakesign=False) :
    if Fakesign :
        if Type != SyntaxError :
            print("Traceback (most recent call last):")
        if Info != None :
            print(Info)
        if Warn == None :
            print(str(Type)[8:-2])
        else :
            print(str(Type)[8:-2]+": "+Warn)
    else :
        raise Type(Warn)
class color :
    def space(line) :
        lib = {"0":_color.Back.BLACK,"1":_color.Back.BLUE,"2":_color.Back.GREEN,"3":_color.Back.CYAN,"4":_color.Back.RED,"5":_color.Back.MAGENTA,"6":_color.Back.YELLOW,"7":_color.Back.WHITE,"8":_color.Back.RESET}
        for i in line :
            printf(lib[i]+" ")
    def printc(foreColor,backColor,*var,_sep=" ",_end="\n") : # foreColor and backColor use binary RGB numbers like “0b110” to represents YELLOW color.
        lib = [_color.Fore.BLACK,_color.Fore.BLUE,_color.Fore.GREEN,_color.Fore.CYAN,_color.Fore.RED,_color.Fore.MAGENTA,_color.Fore.YELLOW,_color.Fore.WHITE,_color.Fore.RESET]
        printf(lib[foreColor])
        lib = [_color.Back.BLACK,_color.Back.BLUE,_color.Back.GREEN,_color.Back.CYAN,_color.Back.RED,_color.Back.MAGENTA,_color.Back.YELLOW,_color.Back.WHITE,_color.Back.RESET]
        printf(lib[backColor])
        for i in list(var) :
            print(i,end=_sep)
        printf(_end)
    class pixel :
        def image(pixels,*var) : # 2D paint: like a tuple ("777","707","777")
            for h in list(var) :
                for i in range(pixels) :
                    for v in h :
                        color.space(v*(pixels*2))
                    print()
def help(key=None) :
    if key == None or key == "" or key == "strmodle" :
        print("""Tree(the * mark means it is a function.)
strmodle
|___printf*
|___fun*
|___loadsign*
|___Traceback*
|___color
|   |___space*
|   |___printc*
|   |___pixel
|       |___image*
|___help*
|___source*
|___copyright*

Enter "strmodle.help(function_name)" like strmodle.help("color.space") to show a single function's help.""")
    elif key == "printf" or key == "strmodle.printf" :
        print("""printf(*var)
prints one or more values with no gaps, no enters.""")
    elif key == "fun" or key == "strmodle.fun" :
        print("""fun(line,sec)
prints a value with second(s) per a single letter(a number or string) or a single word(a list)""")
    elif key == "loadsign" or key == "strmodle.loadsign" :
        print("""loadsign(main="█",half="▌",fill=" ",grid=10,amaintime=1,showperplace=None,tip="")
makes a loading sign.
main:
    whole parts of a loading sign's token.
half:
    half parts of a loading sign's token.
fill:
    blank parts of a loading sign's token.
grid:
    how many grids in a loading sign.
amaintime:
    the time of load a grid.
showperplace:
    show the percent's decimal places.(None is not show)
tip:
    the tip when loading.""")
    elif key == "Traceback" or key == "strmodle.Traceback" :
        print("""Traceback(Info=None,Type=RuntimeError,Warn=None,Fakesign=False)
raise a real or fake exception.
Info:
    a exception's information.
Type:
    the exception's type.
Warn:
    a exception's warning.
Fakesign:
    real or fake.""")
    elif key == "color" or key == "strmodle.color" :
        print("""Tree(the * mark means it is a function.)
color
|___space*
|___printc*
|___pixel
    |___image*

Enter "strmodle.help(color.function_name)" like strmodle.help("color.printc") to show a single function's help.""")
    elif key == "space" or key == "color.space" or key == "strmodle.color.space" :
        print("""color.space(line)
prints spaces with colors.
line:
    string codes, every single number of string must be 0~8:
        -----------------------
        |number|color  |binary|
        =======================
        |0     |black  |0b000 |
        -----------------------
        |1     |blue   |0b001 |
        -----------------------
        |2     |green  |0b010 |
        -----------------------
        |3     |cyan   |0b011 |
        -----------------------
        |4     |red    |0b100 |
        -----------------------
        |5     |magenta|0b101 |
        -----------------------
        |6     |yellow |0b110 |
        -----------------------
        |7     |white  |0b111 |
        -----------------------
        |8     |default|0b1000|
        -----------------------""")
    elif key == "printc" or key == "color.printc" or key == "strmodle.color.printc" :
        print("""color.printc(foreColor,backColor,*var,_sep=" ",_end="\n")
prints texts with colors.
foreColor and backColor:
    integers, and they all must be 0~8:
        -----------------------
        |number|color  |binary|
        =======================
        |0     |black  |0b000 |
        -----------------------
        |1     |blue   |0b001 |
        -----------------------
        |2     |green  |0b010 |
        -----------------------
        |3     |cyan   |0b011 |
        -----------------------
        |4     |red    |0b100 |
        -----------------------
        |5     |magenta|0b101 |
        -----------------------
        |6     |yellow |0b110 |
        -----------------------
        |7     |white  |0b111 |
        -----------------------
        |8     |default|0b1000|
        -----------------------
*var:
    output values.
_sep:
    a gap between two values.
_end:
    the end of all output.""")
    elif key == "pixel" or key == "color.pixel" or key == "strmodle.color.pixel" :
        print("""Tree(the * mark means it is a function.)
pixel
|___image*

Enter "strmodle.help(color.pixel.function_name)" like strmodle.help("color.pixel.image") to show a single function's help.""")
    elif key == "image" or key == "color.pixel.image" or key == "strmodle.color.pixel.image" :
        print("""color.pixel.image(pixels,*var)
pixels:
    how many pixels does the image has.
*var:
    2D tuple with lists, like [2,3,3],[7,4,4],[0,3,1] . The color codes:
        integers, and they all must be 0~8:
            -----------------------
            |number|color  |binary|
            =======================
            |0     |black  |0b000 |
            -----------------------
            |1     |blue   |0b001 |
            -----------------------
            |2     |green  |0b010 |
            -----------------------
            |3     |cyan   |0b011 |
            -----------------------
            |4     |red    |0b100 |
            -----------------------
            |5     |magenta|0b101 |
            -----------------------
            |6     |yellow |0b110 |
            -----------------------
            |7     |white  |0b111 |
            -----------------------
            |8     |default|0b1000|
            -----------------------""")
    elif key == "help" or key == "strmodle.help" :
        print("""help(key=None)
for help.
key:
    a string:
        a single function, a function with whole path, or a class.
See function list? Type strmodle.help() to see.""")
    elif key == "source" or key == "strmodle.source" :
        print("""source
type print(source) to see the source code of this module.""")
    elif key == "copyright" or key == "strmodle.copyright" :
        print("""copyright(key=None)
key:
    s string.
type strmodle.copyright() to see more.""")
    else :
        print("nothing to see.")
def copyright(key=None) :
    if key == None or key == "" :
        print('type strmodle.copyright("144881") or strmodle.copyright("thismodule") to see.')
    elif key in ["144881","144881studios","144881Studios","144881STUDIOS","144881 studios","144881 Studios","144881 STUDIOS"] :
        print("144881 Studios Copyright (c) 2013-2020.")
    else :
        print("144881 Python strmodle Module Copyright (c) 2020.")
