class Player():
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.turn_troops = 0

    def draft(self, rmap):
        while self.turn_troops > 0:
            selection = input('Where would you like to put your troops?  ')
            if selection == '':
                break
            troops = 0
            while troops < 1 or troops > self.turn_troops:
                troops = int(input('How many? (You currently have ' + str(self.turn_troops) + ')  '))
            rmap[int(selection)].add_troops(troops)
            self.turn_troops -= troops

    def attack(self, rmap):
        attacking = input('Which territory would you like to attack with?  ')
        if attacking != '':
            attacked = int(input('Which territory would you like to attack?  '))
            rmap[int(attacking)].attack(rmap[attacked])

    def fortify(self, rmap):
        fortifying = input('Which territory would you like to get the troops from?  ')
        if fortifying != '':
            fortifyed = int(input('Which territory would you like to fortify?  '))
            troops = 0
            while troops < 1 or troops > rmap[int(fortifying)].troops - 1:
                    troops = int(input('How many? (You can move ' + str(rmap[int(fortifying)].troops - 1) + ')  '))
            rmap[int(fortifying)].move_troops(rmap[int(fortifyed)], troops)
