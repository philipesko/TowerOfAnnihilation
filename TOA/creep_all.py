from creep import Creep


class Creep_blue_1(Creep):

    def __init__(self):
        super().__init__()
        self.creep_health = 30
        self.max_health = 30
        self.speed = 3.5
        self.reward = 5
        # Creep level 1
        self.blue_creep1 = [self.load_image('creep-1-blue/1.png'),
                            self.load_image('creep-1-blue/2.png'),
                            self.load_image('creep-1-blue/3.png'),
                            self.load_image('creep-1-blue/4.png'),
                            self.load_image('creep-1-blue/5.png'),
                            self.load_image('creep-1-blue/6.png')]


class Creep_green_1(Creep):

    def __init__(self):
        super().__init__()
        self.creep_health = 40
        self.max_health = 40
        self.speed = 3.5
        self.reward = 10
        # Creep level 2
        self.blue_creep1 = [self.load_image('creep-1-green/1.png'),
                            self.load_image('creep-1-green/2.png'),
                            self.load_image('creep-1-green/3.png'),
                            self.load_image('creep-1-green/4.png'),
                            self.load_image('creep-1-green/5.png'),
                            self.load_image('creep-1-green/6.png')]


class Creep_red_1(Creep):

    def __init__(self):
        super().__init__()
        self.creep_health = 50
        self.max_health = 50
        self.speed = 3.5
        self.reward = 15
        # Creep level 3
        self.blue_creep1 = [self.load_image('creep-1-red/1.png'),
                            self.load_image('creep-1-red/2.png'),
                            self.load_image('creep-1-red/3.png'),
                            self.load_image('creep-1-red/4.png'),
                            self.load_image('creep-1-red/5.png'),
                            self.load_image('creep-1-red/6.png')]


class Creep_blue_2(Creep):

    def __init__(self):
        super().__init__()
        self.creep_health = 60
        self.max_health = 60
        self.speed = 3
        self.reward = 20
        # Creep level 4
        self.blue_creep1 = [self.load_image('creep-2-blue/1.png'),
                            self.load_image('creep-2-blue/2.png'),
                            self.load_image('creep-2-blue/3.png'),
                            self.load_image('creep-2-blue/4.png')]


class Creep_green_2(Creep):

    def __init__(self):
        super().__init__()
        self.creep_health = 70
        self.max_health = 70
        self.speed = 3
        self.reward = 25
        # Creep level 4
        self.blue_creep1 = [self.load_image('creep-2-green/1.png'),
                            self.load_image('creep-2-green/2.png'),
                            self.load_image('creep-2-green/3.png'),
                            self.load_image('creep-2-green/4.png')]


class Creep_red_2(Creep):

    def __init__(self):
        super().__init__()
        self.creep_health = 80
        self.max_health = 80
        self.speed = 3
        self.reward = 30
        # Creep level 4
        self.blue_creep1 = [self.load_image('creep-2-red/1.png'),
                            self.load_image('creep-2-red/2.png'),
                            self.load_image('creep-2-red/3.png'),
                            self.load_image('creep-2-red/4.png')]


class Creep_blue_3(Creep):

    def __init__(self):
        super().__init__()
        self.creep_health = 90
        self.max_health = 90
        self.speed = 3
        self.reward = 35
        # Creep level 4
        self.blue_creep1 = [self.load_image('creep-3-blue/1.png'),
                            self.load_image('creep-3-blue/2.png'),
                            self.load_image('creep-3-blue/3.png'),
                            self.load_image('creep-3-blue/4.png')]


class Creep_green_3(Creep):

    def __init__(self):
        super().__init__()
        self.creep_health = 100
        self.max_health = 100
        self.speed = 3
        self.reward = 40
        # Creep level 4
        self.blue_creep1 = [self.load_image('creep-3-green/1.png'),
                            self.load_image('creep-3-green/2.png'),
                            self.load_image('creep-3-green/3.png'),
                            self.load_image('creep-3-green/4.png')]


class Creep_red_3(Creep):

    def __init__(self):
        super().__init__()
        self.creep_health = 110
        self.max_health = 110
        self.speed = 3
        self.reward = 45
        # Creep level 4
        self.blue_creep1 = [self.load_image('creep-3-red/1.png'),
                            self.load_image('creep-3-red/2.png'),
                            self.load_image('creep-3-red/3.png'),
                            self.load_image('creep-3-red/4.png')]


class Boss(Creep):

    def __init__(self):
        super().__init__()
        self.creep_health = 1000
        self.max_health = 1000
        self.speed = 1
        self.reward = 100
        # Boss
        self.blue_creep1 = [self.load_image('boss/boss-1.png'),
                            self.load_image('boss/boss-2.png'),
                            self.load_image('boss/boss-3.png'),
                            self.load_image('boss/boss-4.png')]
