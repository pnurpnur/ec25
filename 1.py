names = "Vyrdax,Drakzyph,Fyrryn,Elarzris"
ins = "R3,L2,R3,L1"

def find_name(names, instructions, circular, swap):
    # Del opp navnene og instruksjonene
    names = names.split(",")
    instructions = instructions.split(",")

    # Startposisjon (første navn)
    position = 0

    for instr in instructions:
        direction = instr[0]        # 'R' eller 'L'
        steps = int(instr[1:])      # antall steg

        if direction == "R":
            if circular:
                pos = position + steps
                position = pos % len(names)
            else:
                # Flytt til høyre, men ikke ut av listen
                position = min(position + steps, len(names) - 1)
        elif direction == "L":
            if circular:
                pos = position - steps
                position = pos % len(names)
            else:
                # Flytt til venstre, men ikke ut av listen
                position = max(position - steps, 0)
        else:
            raise ValueError(f"Ugyldig instruksjon: {instr}")

        if swap:
            temp = names[0]
            names[0] = names[position]
            names[position] = temp
            position = 0

    # Returner navnet vi ender på
    return names[position]

#names = "Sarnryn,Rynmirix,Loreldrin,Sorrax,Kynulth,Kroncyth,Yndulrix,Tirthel,Cynddar,Tyrgarath"
#ins = "L3,R8,L7,R9,L1,R2,L2,R4,L6,R7,L6"
#res = find_name(names, ins, False, False)
#print(res)

#names = "Xarzion,Urithjoris,Oronlar,Ildaxar,Cynvarnix,Nylnoris,Ralralis,Kyxel,Falgnaris,Quirkyr,Rahris,Thymadarin,Drethnor,Mavwyris,Lorral,Urxeth,Selzral,Falzral,Drakcarth,Zraalix"
#ins = "L11,R8,L16,R17,L12,R13,L11,R13,L19,R12,L5,R8,L5,R14,L5,R8,L5,R9,L5,R15,L19,R5,L13,R7,L12,R13,L16,R19,L17"
#res = find_name(names, ins, True, False)
#print(res)

names = "Brythrax,Rylarverax,Bryngryph,Azmarcoryx,Agnaroris,Ildthyris,Ascalrax,Thymkynar,Eraspyxis,Nyath,Gorathlar,Agnargalor,Zorgalor,Xarvel,Havtaril,Nylroth,Azpyxis,Sarnhynd,Orahthyn,Quarnzar,Rynalar,Gavadar,Cynderpyxis,Ravulrix,Lareldrin,Zraalcalyx,Maradir,Thaznar,Ralrex,Shaelzyph"
ins = "L7,R28,L38,R36,L20,R21,L22,R38,L47,R16,L7,R30,L19,R45,L33,R29,L24,R39,L22,R19,L5,R23,L5,R22,L5,R21,L5,R19,L5,R38,L5,R49,L5,R6,L5,R22,L5,R20,L5,R38,L27,R29,L28,R34,L45,R13,L5,R49,L35,R17,L39,R35,L28,R26,L36,R17,L47,R37,L38"
res = find_name(names, ins, True, True)
print(res)
