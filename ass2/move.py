from Maestro import Controller
import curses


class Move:
    def __init__(self):
        self.screen = curses.initscr()
        curses.cbreak()
        curses.noecho()
        curses.halfdelay(1)
        curses.endwin()
        self.screen.keypad(True)

        self.control = Controller()
        self.control.setTarget(1, 6000)
        self.control.setTarget(2, 6000)

        self.head_pos = 6000
        self.head_step = 1000
        self.head_tilt = 5000

        self.speed = 1250

        self.control.setTarget(0, 6000)
        self.control.setTarget(3, 6000)
        self.control.setTarget(4, 5000)

    def turn_head(self, direction):
        if (direction == 1 and self.head_pos > 6000 - 2 * self.head_step):
            self.head_pos -= self.head_step
        elif (direction == 0 and self.head_pos < 6000 + 2 * self.head_step):
            self.head_pos += self.head_step
        self.control.setTarget(3, self.head_pos)

    def tilt_head(self, direction):
        if (direction == 1 and self.head_tilt > 5000 - 2 * self.head_step / 2):
            self.head_tilt -= self.head_step / 2
        elif (direction == 0 and self.head_tilt < 5000 + 2 * self.head_step / 2):
            self.head_tilt += self.head_step / 2
        self.control.setTarget(4, self.head_tilt)

    def change_speed(self, direction):
        if (direction == 0 and self.speed > 1000):
            self.speed -= 250
        elif (direction == 1 and self.speed < 1500):
            self.speed += 250

    def run(self):
        try:
            while True:
                self.screen.clear()
                char = self.screen.getch()
                if char == ord('z'):
                    break
                elif char == ord(' '):  # reset entirely
                    self.control.setTarget(0, 6000)
                    self.control.setTarget(3, 6000)
                    self.control.setTarget(4, 5000)
                    self.head_pos = 6000
                    self.head_tilt = 5000
                elif char == ord('s'):  # reset body
                    self.control.setTarget(0, 6000)
                elif char == ord('w'):  # reset head
                    self.control.setTarget(4, 5000)
                    self.control.setTarget(3, 6000)
                    self.head_pos = 6000
                    self.head_tilt = 5000
                elif char == ord('r'):  # head up
                    self.tilt_head(0)
                elif char == ord('f'):  # head down
                    self.tilt_head(1)
                elif char == ord('q'):  # head left
                    self.turn_head(0)
                elif char == ord('e'):  # head right
                    self.turn_head(1)
                elif char == ord('a'):  # body left
                    self.control.setTarget(0, 7500)
                elif char == ord('d'):  # body right
                    self.control.setTarget(0, 5000)
                elif char == ord('='):
                    self.change_speed(1)
                elif char == ord('-'):
                    self.change_speed(0)

                if char == curses.KEY_UP:  # forward
                    self.control.setTarget(1, 6000 - self.speed)
                elif char == curses.KEY_DOWN:  # backward
                    self.control.setTarget(1, 6000 + self.speed)
                elif char == curses.KEY_RIGHT:  # right
                    self.control.setTarget(1, 6000)
                    self.control.setTarget(2, 6000 - self.speed)
                elif char == curses.KEY_LEFT:  # left
                    self.control.setTarget(1, 6000)
                    self.control.setTarget(2, 6000 + self.speed)
                else:
                    self.control.setTarget(1, 6000)
                    self.control.setTarget(2, 6000)

                    # 3 - head (left right)
                    # 4 - head (up down)
                    # 0 - body

        finally:
            # shut down
            curses.nocbreak()
            self.screen.keypad(0)
            curses.echo()
            curses.endwin()


move = Move()
move.run()
