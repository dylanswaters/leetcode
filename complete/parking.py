# leetcode 1603
#complete

class ParkingSystem():
    big = 0
    medium = 0
    small = 0
    
    def __init__(self, big, medium, small) -> None:
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carSize):
        if carSize == 1:
            if self.big >= 1:
                self.big -= 1
                return True
            else:
                return False
        if carSize == 2:
            if self.medium >= 1:
                self.medium -= 1
                return True
            else:
                return False
        if carSize == 3:
            if self.small >= 1:
                self.small -= 1
                return True
            else:
                return False   

def main():
    testParkingSystem = ParkingSystem(1,1,0)
    print(testParkingSystem.addCar(1))
    print(testParkingSystem.addCar(2))
    print(testParkingSystem.addCar(3))
    print(testParkingSystem.addCar(1))


if __name__ == '__main__':
    main()
