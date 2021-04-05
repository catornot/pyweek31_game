class levels:
    """
    # load system for levels
    #
    # 0 = wall , [0,radius, (x,y)]
    # 1 = guard
    # 2 = Player parms
    # 3 = shrink player radius
    # 4 = grow player radius
    # 5 = level_transit
    # 6 = text
    # 7 = coins
    """

    def level_process(self, string, screen):
        if string == "test":
            return self.test(screen)
        elif string == "main_menu":
            return self.main_menu(screen)
        elif string == "level1":
            return self.level1(screen)
        elif string == "level2":
            return self.level2(screen)
        elif string == "level3":
            return self.level3(screen)
        elif string == "level4":
            return self.level4(screen)
        elif string == "level5":
            return self.level5(screen)

        else:
            print(string)
            return self.main_menu(screen)

    def add_walls(self, level, screen):
        for x in range(int(screen.get_width()/60)):
            level.append([0, 30, (x*60, 0)])
            level.append([0, 30, (x*60, screen.get_height())])

        for x in range(int(screen.get_height()/60)):
            level.append([0, 30, (0, x*60)])
            level.append([0, 30, (screen.get_width(), x*60)])

        level.append([0, 30, (screen.get_width(), screen.get_height())])
        return level

    def creat_wall_h(self, level, x, t, radius, y):
        for i in range(0, t):
            level.append([0, radius, (x + radius*2*i, y)])

        return level

    def creat_wall_v(self, level, y, t, radius, x):
        for i in range(0, t):
            level.append([0, radius, (x, y + radius*2*i)])

        return level

    def test(self, screen):
        level = [

            [0, 30, (140, 160)],
            [0, 30, (200, 160)],
            [0, 50, (480, 270)],
            [1, (300, 75), (600, 75), 30],
            [2, 30, (100, 200)],
            [3, 20, (600, 200), 50, 10],
            [4, 20, (600, 350), 50, 10],
            [5, 20, (700, 400), "main_menu"],
            [6, 30, (700,100),"test","main_menu"],
            [7, 20, (700,500)]


        ]

        return self.add_walls(level, screen)

    def main_menu(self,screen):
        level = [

            [2, 30, (500, 400)],
            [6, 30, (200,200),"Play",None],
            [6, 30, (200,275),"credits : cat_or_not",None],
            [6, 30, (200,350),"level editor (soon)",None],
            [6, 30, (200,425),"exit : key esc",None],
            [5, 30, (300, 200), "level1"],
            [6, 30, (600,200),"test level",None],
            [5, 30, (700, 200), "test"],
            [6, 30, (600,275),"custom level (soon)",None],



        ]

        return self.add_walls(level, screen)

    def level1(self, screen):
        level = [

            [0, 30, (140, 160)],
            [0, 30, (200, 160)],
            [0, 50, (200, 300)],
            [0, 50, (200, 450)],
            [0, 50, (100, 400)],
            [1, (100, 75), (400, 75), 30],
            [2, 30, (100, 200)],
            [3, 20, (600, 200), 50, 10],
            [4, 20, (600, 350), 50, 10],
            [5, 20, (100, 500), "level2"],


        ]

        return self.add_walls(level, screen)

    def level2(self, screen):
        level = [
            [2, 30, (100, 200)],
            [0, 30, (140, 160)],
            [3, 20, (160, 400), 50, 10],
            [0, 75, (850, 100)],
            [0, 75, (800, 150)],
            [5, 20, (75, 75), "level3"],
            [1, (300, 300), (400, 350), 30],
            [4, 20, (850, 300), 50, 10],
            [1, (400, 500), (400, 400), 30],
            [5, 20, (300, 375), "level4"],


        ]
        level = self.creat_wall_h(level, 20, 10, 30, 160)

        level = self.creat_wall_h(level, 220, 10, 30, 240)

        level = self.creat_wall_v(level, 240, 10, 30, 220)

        return self.add_walls(level, screen)

    def level3(self, screen):
        level = [

            
            [2, 10, (850, 300)],
            [0, 30, (140, 160)],
            [3, 20, (160, 400), 50, 10],
            [0, 75, (850, 100)],
            [0, 75, (800, 150)],
            [5, 20, (75, 75), "level3"],
            [1, (300, 300), (400, 350), 30],
            [4, 20, (850, 300), 50, 10],
            [1, (400, 500), (400, 400), 30],
            [5, 20, (300, 375), "level4"],


        ]
        level = self.creat_wall_h(level, 20, 10, 30, 160)

        level = self.creat_wall_h(level, 220, 10, 30, 240)

        level = self.creat_wall_v(level, 240, 10, 30, 220)

        return self.add_walls(level, screen)

    def level4(self, screen):
        level = [
            
            [2, 30, (75, 270)],
            [3, 20, (850, 90), 50, 10],
            [4, 20, (400, 90), 50, 10],
            [3, 20, (440, 90), 50, 30],
            [1, (250, 270), (600, 270), 30],
            [5, 20, (850, 270), "level5"],
            [1, (500, 400), (550, 500), 30],
            [1, (450, 500), (400, 400), 30],
            [7, 20, (850,450)],

        ]

        level = self.creat_wall_h(level, 200, 15, 30, 190)

        level = self.creat_wall_h(level, 200, 15, 30, 350)

        return self.add_walls(level, screen)

    def level5(self, screen):
        level = [
            
            [2, 30, (500, 400)],
            [6, 30, (480,190),"Thanks for playing",None],
            [6, 30, (480,210),"I will add more content later on icht.io",None],
            [6, 30, (480,230),"Now you could try to make your own levels",None],
            [6, 30, (480,250),"with the load_levels.py file if you have the source version",None],
            [6, 40, (480,270),"to main menu","main_menu"],
            [5, 20, (480 + 90, 280), "main_menu"],

        ]

        return self.add_walls(level, screen)
