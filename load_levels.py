from random import randint


class levels:
    """
    # load system for levels
    #
    # 0 = wall [0,radius, (x,y)]
    # 1 = guard [1, (x1, y1), (x2, y1), radius]
    # 2 = Player parms [2, radius, (x, y)]
    # 3 = shrink player radius [3, radius, (x, y), max size, min size]
    # 4 = grow player radius [4, radius, (x, y), max size, min size]
    # 5 = level_transit [5, radius, (x, y), "level"]
    # 6 = text [6, radius, (x, y), "text", "level" or None]
    # 7 = coins [7, radius, (x, y)] 
    # 8 = radius_wall [8, radius, (x, y), bufer_cords , None] or [8, radius, (x, y), None, bufer_cords_small],
    # 9 = jump_pad [9, radius, (x, y), (x_lauch_to, y_lauch_to)],
    """

    def level_process(self, string, screen):
        if string == "test":
            return self.test(screen)
            # return self.test(screen)
        elif string == "main_menu":
            return self.main_menu(screen)
        elif string == "level_hub1":
            return self.level_hub1(screen)
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
        elif string == "level6":
            return self.level6(screen)
        elif string == "level7":
            return self.level7(screen)
        elif string == "s_level1":
            return self.s_level1(screen)
        elif string == "level8":
            return self.level8(screen)

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
            [6, 30, (700, 100), "test", "main_menu"],
            [7, 20, (700, 500)],
            [8, 30, (800, 450), 40, None],
            [8, 30, (200, 350), None, 11],
            [9, 20, (300, 350), (500, 75)],


        ]

        return self.add_walls(level, screen)

    def level_hub1(self, screen):
        level = [

            [2, 30, (500, 500)],
            [6, 20, (500, 500), "level selector", None],
            [6, 20, (200, 90), "level 1", "level1"],
            [6, 20, (200, 140), "level 2", "level2"],
            [6, 20, (200, 180), "level 3", "level3"],
            [6, 20, (200, 220), "level 4", "level4"],
            [6, 20, (200, 260), "level 5", "level5"],
            [6, 20, (200, 300), "level 6", "level6"],
            [6, 20, (200, 340), "level 7", "level7"],
            [6, 20, (200, 380), "level 8", "level8"],





        ]

        return self.add_walls(level, screen)

    def main_menu(self, screen):
        level = [

            [2, 30, (500, 400)],
            [6, 30, (200, 200), "Play", None],
            [6, 30, (200, 275), "credits : cat_or_not", None],
            [6, 30, (200, 350), "level editor (soon)", None],
            [6, 30, (200, 425), "exit : key esc", None],
            [5, 30, (300, 200), "level_hub1"],
            [6, 30, (600, 200), "test level", None],
            [5, 30, (700, 200), "test"],
            [6, 30, (600, 275), "custom level (soon)", None],



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
            [7, 20, (850, 450)],
            [8, 30, (100, 350), None, 11],
            [8, 30, (150, 350), None, 11],
            [8, 30, (50, 350), None, 11],

        ]

        level = self.creat_wall_h(level, 200, 15, 30, 190)

        level = self.creat_wall_h(level, 200, 15, 30, 350)

        return self.add_walls(level, screen)

    def level5(self, screen):
        level = [

            [2, 30, (75, 270 - 60)],
            [1, (600, 100), (200, 100), 30],
            [1, (600, 200), (250, 200), 30],
            [1, (600, 300), (300, 300), 30],
            [3, 30, (75, 270 + (270 + 100) / 2), 50, 10],
            [5, 20, (60, 60), "level6"],
            [0, 30, (130, 50)],
            [0, 30, (100, 100)],



        ]

        level = self.creat_wall_h(level, 0, 10, 30, 270 + 100)

        return self.add_walls(level, screen)

    def level6(self, screen):
        level = [

            [6, 30, (300, 270 + 200), "the level is randomized", None],
            [6, 30, (300, 270 + 220),
             "if stuck press 'r' to restart the level", None],
            [2, 10, (75, 270 - 60)],
            [1, (600, 100), (200, 100), 20],
            [1, (600, 300), (300, 300), 20],
            [5, 20, (850, 270 - 60), "level7"],




        ]

        level = self.creat_wall_h(level, 0, 30, 20, 270 + 150)

        for x in range(95):
            level.append([0, 20, [randint(50, 800), randint(50, 270 + 130)]])

        return self.add_walls(level, screen)

    def level7(self, screen):
        level = [

            [2, 30, (100, 400)],
            [5, 20, (100, 0), "s_level1"],
            [0, 30, (164, 401)],
            [7, 15, (400, 333)],
            [9, 20, (256, 403), (890, 73)],
            [1, (554, 220), (554, 50), 30],
            [3, 20, (743, 62), 50, 20],
            [9, 20, (873, 202), (894, 479)],
            [1, (554, 474), (554, 324), 20],
            [9, 20, (600, 339), (417, 217)],
            [1, (220, 50), (220, 220), 40],
            [5, 20, (50, 57), "level8"],



        ]

        level = self.creat_wall_h(level, 641, 30, 30, 400)
        level = self.creat_wall_h(level, 641, 30, 30, 139)
        level = self.creat_wall_h(level, 0, 30, 30, 270)
        level = self.creat_wall_v(level, 0, 30, 30, 480)

        return self.add_walls(level, screen)

    def s_level1(self, screen):
        level = [

            [2, 30, (500, 400)],
            [6, 30, (300, 270 + 220),
             "you found a secret level", None],
            [5, 20, (500, 100), "level7"],

        ]

        for x in range(1, 30):
            level.append([1, (500, 400), (500, 400), 20])

        for x in range(1, 10):
            level.append([7, 20, (300*x/2, 200)])

        return self.add_walls(level, screen)

    def level8(self, screen):
        level = [

            [2, 30, (1000, 1000)],
            [9, 20, (1000, 1000), (480, 270)],
            [8, 60, (250, 327), 45 , None],
            [8, 50, (654, 327), None ,11],
            [1, (200, 480), (300, 450), 30],
            [1, (580, 480), (760, 450), 30],
            [4, 20, (96, 431), 50, 10],
            [3, 20, (834, 447), 50, 10],
            [5, 20, (442, 91), "level9"],
            [0, 30, (170, 325)],
            [1, (64, 254), (262, 98), 30],
            [1, (604, 90), (894, 274), 30],
            


        ]

        level = self.creat_wall_v(level, 195, 3, 30, 332)
        level = self.creat_wall_h(level, 332, 4, 30, 195)
        level = self.creat_wall_v(level, 195, 3, 30, 576)
        level = self.creat_wall_h(level, 0, 3, 30, 327)
        level = self.creat_wall_h(level, 740, 4, 30, 327)

        return self.add_walls(level, screen)

