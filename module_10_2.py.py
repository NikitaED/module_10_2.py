import threading
import time
enemies = 100


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = enemies
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            time.sleep(1)
            self.enemies -= self.power
            self.enemies = max(self.enemies, 0)
            self.days += 1
            print(f"{self.name} сражается {self.days}..., осталось {self.enemies} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} дня(ей)!")



knight1 = Knight(name="Sir Galahad", power=10)
knight2 = Knight(name="Sir Lancelot", power=20)


knight1.start()
knight2.start()


knight1.join()
knight2.join()


print("Битвы завершены!")
