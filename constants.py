class Constants:
    def __init__(self):

        self.width = 600
        self.height = 600

        self.rows = 3
        self.columns = 3

        self.square_size = self.width // self.columns
        self.line_width = 15
        self.circle_width = 15
        self.cross_width = 20

        self.radius = self.square_size // 4
        self.offset = 50

        #Colors
        self.background = (255, 51, 153)
        self.line_color = (204, 0, 102)
        self.circle_color = (102, 255, 255)
        self.cross_color = (255, 0, 0)