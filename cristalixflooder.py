import keyboard
from time import sleep

print("  .oooooo.             o8o               .             oooo   o8o  ")
print(" d8P'  `Y8b            `'"'"'"             .o8             `888   `'"'"'"         ")
print("888          oooo d8b oooo   .oooo.o .o888oo  .oooo.    888  oooo  oooo    ooo")
print("888          `888'"''"'8P `888  d88(  '"'8   888   `P  )88b   888  `888   `88b..8P"'"  ")
print("888           888      888  `'"'Y88b.    888    .oP"888   888   888     Y888"'" ")
print("`88b    ooo   888      888  o.  )88b   888 . d8(  888   888   888   .o8'"'"'"88b ")
print(" `Y8bood8P'  d888b    o888o 8'""'888P'   '"'888'"' `Y888'""'8o o888o o888o o88'   888o ")
print('\nv1\t\t\t\tMSG FLOODER\t\t\t\tBy VAFI')
print('\t\t\t\t\t\t\thttps://github.com/VAFI\n')

nick = input("Никнейм: ")
msg = input("Сообщение: ")
dalay = float(input("Введите задержку: "))
while True:
    sleep(dalay)
    keyboard.send('t')
    sleep(0.1)
    keyboard.write('/msg ' + nick + ' ' + msg)
    sleep(0.1)
    keyboard.send('enter')
    print('/msg ' + nick + ' ' + msg)
