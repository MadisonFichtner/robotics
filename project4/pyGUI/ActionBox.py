class ActionBox:
    def __init__(self, canvas, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.action = None  # the action that this box contains
        self.icon = canvas.create_rectangle(self.x - self.width / 2, self.y - self.height / 2, self.x + self.width / 2,
                                            self.y + self.height / 2, fill="#FFFFFF")

    # return if the given coordinates are within the box
    def contains(self, x, y):
        return self.x - self.width / 2 < x < self.x + self.width / 2 and \
               self.y - self.height / 2 < y < self.y + self.height / 2

    def set_action(self, action):
        self.action = action
