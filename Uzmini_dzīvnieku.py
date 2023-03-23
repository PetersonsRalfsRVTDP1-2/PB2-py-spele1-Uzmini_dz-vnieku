'''
Spēle - Uzmini dzīvnieku.
Veidojis: Ralfs Pētersons DP1-2
'''

import winsound
from time import sleep
from os import system

print('Sveiki! Uzspēlēsim spēli - Uzmini dzīvnieku')
sleep(3)
input('Lai sāktu, spiežat <ENTER>')
system('cls')
sleep(3)
print('LEVEL 1')
sleep(1)

print('''
       _=,_
    o_/6 /#\\
    \__ |##/
     ='|--\\
       /   #'-.
       \#|_   _'-. /
        |/ \_( # |" 
       C/ ,--___/
''')

sleep(1.5)

# Definēt pareizo dzīvnieku
dzivnieks_suns = "suns"

uzmini = ""

while uzmini != dzivnieks_suns:
    # Lūgt lietotājam uzminēt dzīvnieku
    uzmini = input('Uzmini, kas šis pa dzīvnieku: ')
    # Pārbaudīt, vai minējums ir pareizs
    if uzmini == dzivnieks_suns :
        print('Pareizi, dodamies uz nākamo līmeni!')
        sleep(3)
        system('cls')
        print('LEVEL 2')
        sleep(2)
        print('''
      /    \\
     _(I)(I)_
    ( _ .. _ )
     `.`--'.'
      )    (
  ,-./      \,-.
 ( _( ||  || )_ )
__\ \\\\||--||'/ /__ 
`-._//||\/||\\\\_.-'
     `--'`--'
    ''')
        sleep(1.5)
    else:
        print('Diemžēl, nepareizi! Mēģini vēlvreiz.')

# Definēt pareizo dzīvnieku
dzivnieks_varde = "varde"

uzmini = ""

while uzmini != dzivnieks_varde:
    # Lūgt lietotājam uzminēt dzīvnieku
    uzmini = input('Uzmini, kas šis pa dzīvnieku: ')
    # Pārbaudīt, vai minējums ir pareizs
    if uzmini == dzivnieks_varde :
        print('Pareizi, dodamies uz nākamo līmeni!')
        sleep(3)
        system('cls')
        print('LEVEL 3')
        sleep(2)
        print('''
     (()__(()
     /       \ 
    ( /    \  \\
     \ o o    /
     (_()_)__/ \             
    / _,==.____ \\
   (   |--|      )
   /\_.|__|'-.__/\_
  / (        /     \ 
  \  \      (      /
   )  '._____)    /    
(((____.--(((____/
        ''')
        sleep(1.5)
    else:
        print('Diemžēl, nepareizi! Mēģini vēlreiz.')

# Definēt pareizo dzīvnieku
dzivnieks_lacis = "lācis"

uzmini = ""

while uzmini != dzivnieks_lacis:
    # Lūgt lietotājam uzminēt dzīvnieku
    uzmini = input('Uzmini, kas šis pa dzīvnieku: ')
    # Pārbaudīt, vai minējums ir pareizs
    if uzmini == dzivnieks_lacis :
        print('Pareizi, dodamies uz nākamo līmeni!')
        sleep(3)
        system('cls')
        print('LEVEL 4')
        sleep(2)
        print('''
                   .     _,
                   |`\__/ /
                   \  . .(
                    | __T|
                   /   |
      _.---======='    |
     //               {}
    `|      ,   ,     {}
     \      /___;    ,'
      ) ,-;`    `\  //
     | / (        ;||
     ||`\\\\        |||
     ||  \\\\       |||
     )\   )\      )||
     `"   `"      `""
            ''')
        sleep(1.5)
    else:
        print('Diemžēl, nepareizi! Mēģini vēlreiz.')

# Definēt pareizo dzīvnieku
dzivnieks_stirna = "stirna"

uzmini = ""

while uzmini != dzivnieks_stirna:
    # Lūgt lietotājam uzminēt dzīvnieku
    uzmini = input('Uzmini, kas šis pa dzīvnieku: ')
    # Pārbaudīt, vai minējums ir pareizs
    if uzmini == dzivnieks_stirna :
        print('Pareizi, dodamies uz nākamo līmeni!')
        sleep(3)
        system('cls')
        print('LEVEL 5')
        sleep(2)
        print('''
                  ,,__
        ..  ..   / o._)                   
       /--'/--\  \-'||              
      /        \_/ / |                    
    .'\  \__\  __.'.'             
      )\ |  )\ |      
     // \\\\ // \\\\
    ||_  \\\\|_  \\\\_
    '--' '--'' '--'
                ''')
        sleep(1.5)
    else:
        print('Diemžēl, nepareizi! Mēģini vēlreiz.')

# Definēt pareizo dzīvnieku
dzivnieks_kamielis = "kamielis"

uzmini = ""

while uzmini != dzivnieks_kamielis :
    # Lūgt lietotājam uzminēt dzīvnieku
    uzmini = input('Uzmini, kas šis pa dzīvnieku: ')
    # Pārbaudīt, vai minējums ir pareizs
    if uzmini == dzivnieks_kamielis :
        print('Pareizi, tagad nebūs tik viegli!')
        sleep(3)
        system('cls')
        print('LEVEL 6')
        sleep(2)
        print('''
             _                 __                 
      __.--**"""**--...__..--**""""*-.            
    .'                                `-.         
  .'                         _           \        
 /                         .'        .    \   _._ 
:                         :          :`*.  :-'.' ;
;    `                    ;          `.) \   /.-' 
:     `                             ; ' -*   ;    
       :.    \           :       :  :        :    
 ;     ; `.   `.         ;     ` |  '             
 |         `.            `. -*"*\; /        :     
 |    :     /`-.           `.    \/`.'  _    `.   
 :    ;    :    `*-.__.-*""":`.   \ ;  'o` `. /   
       ;   ;                ;  \   ;:       ;:   ,/
  |  | |                       /`  | ,      `*-*'/ 
  `  : :  :                /  /    | : .    ._.-'  
   \  \ ,  \              :   `.   :  \ \   .'     
    :  *:   ;             :    |`*-'   `*+-*       
    `**-*`""               *---*
                    ''')
        sleep(1.5)
    else:
        print('Diemžēl, nepareizi! Mēģini vēlreiz.')

# Definēt pareizo dzīvnieku
dzivnieks_degunradzis = "degunradzis"

uzmini = ""

while uzmini != dzivnieks_degunradzis :
    # Lūgt lietotājam uzminēt dzīvnieku
    uzmini = input('Uzmini, kas šis pa dzīvnieku: ')
    # Pārbaudīt, vai minējums ir pareizs
    if uzmini == dzivnieks_degunradzis :
        print('Pareizi, dodamies uz nākamo līmeni!')
        sleep(3)
        system('cls')
        print('LEVEL 7')
        sleep(2)
        print('''
                                            .      //
                                       /) \ |\    //
                                 (\\\\|  || \)u|   |F     /)
                                  \```.FF  \  \  |J   .'/
                               __  `.  `|   \  `-'J .'.'
        ______           __.--'  `-. \_ J    >.   `'.'   .
    _.-'      ""`-------'           `-.`.`. / )>.  /.' .<'
  .'                                   `-._>--' )\ `--''
  F .                                          ('.--'"
 (_/                                            '\\
  \                                             'o`.
  |\                                                `.
  J \          |              /      |                \\
   L \                       J       (             .  |
   J  \      .               F        _.--'`._  /`. \_)
    F  `.    |                       /        ""   "'
    F   /\   |_          ___|   `-_.'
   /   /  F  J `--.___.-'   F  - /
  /    F  |   L            J    /|
 (_   F   |   L            F  .'||
  L  F    |   |           |  /J  |
  | J     `.  |           | J  | |              ____.---.__
  |_|______ \  L          | F__|_|___.---------'
--'        `-`--`--.___.-'-'---
                        ''')
        sleep(1.5)
    else:
        print('Diemžēl, nepareizi! Mēģini vēlreiz.')

# Definēt pareizo dzīvnieku
dzivnieks_briedis = "briedis"

uzmini = ""

while uzmini != dzivnieks_briedis :
    # Lūgt lietotājam uzminēt dzīvnieku
    uzmini = input('Uzmini, kas šis pa dzīvnieku: ')
    # Pārbaudīt, vai minējums ir pareizs
    if uzmini == dzivnieks_briedis :
        print('Pareizi, dodamies uz nākamo līmeni!')
        sleep(3)
        system('cls')
        print('LEVEL 8')
        sleep(2)
        print('''
 \\\\/),
 ,'.' /,
(_)- / /,
   /\_/ |__..--,  * 
  (\___/\ \ \ / ).'
   \____/ / (_ //
    \\\\_ ,'--'\_(
    )_)_/ )_/ )_)
   (_(_.'(_.'(_.'
           ''')
        sleep(1.5)
    else:
        print('Diemžēl, nepareizi! Mēģini vēlreiz.')

# Definēt pareizo dzīvnieku
dzivnieks_zebra = "zebra"

uzmini = ""

while uzmini != dzivnieks_zebra:
    # Lūgt lietotājam uzminēt dzīvnieku
    uzmini = input('Uzmini, kas šis pa dzīvnieku: ')
    # Pārbaudīt, vai minējums ir pareizs
    if uzmini == dzivnieks_zebra :
        print('Pareizi, dodamies uz nākamo līmeni!')
        sleep(3)
        system('cls')
        print('LEVEL 9')
        sleep(2)
        print('''
               __           _       _           __
        _..--"" ."""--._   ( \.---./ )   _.--""". ""--.._
    .-'`     ' .    `'-.'.  \/ e e \/  .'.-'`    . '     `'-.
 .'`       '            '.\  \  ^  /  /.'             '      `'. 
/__      '     .          \`\/`-"-`\/`/          '      '     __\\
`  '. .' __    .   _       \{       }/       _   '    __ '. .'  `
     '--'  '-. . /` \       {       }       / `\ ' .-'  '--'
              '-'    |       {     }       |    '-'
                      \     //\   /\\\\     /
                       '._ //  '-'  \\\\ _.'
                          (('.  )  .'))
                              \(  /
                               `"`
              ''')
        sleep(1.5)
    else:
        print('Diemžēl, nepareizi! Mēģini vēlreiz.')

# Definēt pareizo dzīvnieku
dzivnieks_siksparnis = "sikspārnis"

uzmini = ""

while uzmini != dzivnieks_siksparnis :
    # Lūgt lietotājam uzminēt dzīvnieku
    uzmini = input('Uzmini, kas šis pa dzīvnieku: ')
    # Pārbaudīt, vai minējums ir pareizs
    if uzmini == dzivnieks_siksparnis :
        print('Pareizi, dodamies uz pēdējo līmeni!')
        sleep(3)
        system('cls')
        print('LEVEL 10')
        sleep(2)
        print('''
/'--.._ `'-="""=-'` _..--'\\
|   ~. )  _     _  ( .~   |
 \  '~/   a  _  a   \~'  /
  \  `|     / \     |`  /
   `'--\    \_/    /--'`
       .'._  J__.-'.
      / /  '-/_ `-  \\
     / -"-'-.  '-.__/
     \__,-.\/     | `\\
     /  ;---.  .--'   |
    |     /\\'-'      /
    '.___.\   _.--;'`)
''')
        sleep(1.5)
    else:
        print('Diemžēl, nepareizi! Mēģini vēlreiz.')

# Definēt pareizo dzīvnieku
dzivnieks_koala = "koala"

uzmini = ""

while uzmini != dzivnieks_koala :
    # Lūgt lietotājam uzminēt dzīvnieku
    uzmini = input('Uzmini, kas šis pa dzīvnieku: ')
    # Pārbaudīt, vai minējums ir pareizs
    if uzmini == dzivnieks_koala :
        print('Apsveicu, tu uzminēji visus dzīvniekus!!!')

        # Uzvaras skaņa
        winsound.Beep(440, 250)
        sleep(0.1)
        winsound.Beep(880, 250)
        sleep(0.1)
        winsound.Beep(220, 250)
        sleep(0.1)
        winsound.Beep(880, 250)
        sleep(0.1)
        winsound.Beep(1020,400)
        sleep(3)

    else:
        print('Diemžēl, nepareizi! Mēģini vēlreiz.')