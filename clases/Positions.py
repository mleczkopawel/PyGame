class Positions:
    def __init__(self, game_width, game_height):
        self.game_width = game_width
        self.game_height = game_height

    def get_game_width(self):
        return self.game_width

    def get_game_height(self):
        return self.game_height

    def set_car_position(self, x, y):
        self.car_position_x = x
        self.car_position_y = y

    def get_car_position(self):
        return self.car_position_x, self.car_position_y

    def get_car_position_x(self):
        return self.car_position_x

    def set_car_position_x(self, x):
        self.car_position_x = x

    def get_car_position_y(self):
        return self.car_position_y

    def set_car_position_y(self, y):
        self.car_position_y = y

    def set_car_width(self, car_width):
        self.car_width = car_width

    def get_car_width(self):
        return self.car_width
