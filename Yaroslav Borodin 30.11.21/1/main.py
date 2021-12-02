# 1) Создайте базовый класс «Стол» и дочерние: «Прямоугольные столы» и «Круглые столы».
# В базовом классе должен быть метод вычисления площади поверхности стола, который будет переопределяться у наследников
# В базовом классе этот метод должен вызывать ошибку - что метод должен быть переопределен у наследника.

from Desk import Desk
from RectangleDesk import RectangleDesk
from RoundDesk import RoundDesk

if __name__ == "__main__":
    newDesk = Desk()
    newDesk.calculate_area()

    roundDesk = RoundDesk(4)
    roundDesk.calculate_area()

    rectDesc = RectangleDesk(1, 2)
    rectDesc.calculate_area()
