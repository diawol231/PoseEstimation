from math import atan2, degrees


def findAngleBody(x1, y1, x2, y2):
    try:
        result = int(degrees(atan2(y1 - y2, x1 - x2)))
    except ZeroDivisionError:
        return 0
    if result < 0:
        result = abs(result)
    if result > 90:
        result = abs(result - 180)
    return result


    #отклонение шеи
def findAngleNeck(x1, y1, x2, y2, xNeck, yNeck):
    try:
        normalX = (x1 + x2)/2
        normalY = (y1 + y2)/2
        result = int(degrees(atan2(yNeck - normalY, xNeck - normalX) - atan2(y2 - normalY, x2 - normalX)))
    except:
        return 0

    if result < 0:
        result = abs(result)
    if result > 90:
        result = abs(result - 270)
    return result


class calculatePose():
    def __init__(self):
        super(calculatePose, self).__init__()
        self.sholdersAng = 0
        self.elbowAng = 0
        self.pelvisAng = 0
        self.kneeAng = 0
        self.backAng = 0
        self.neckAng = 0

        self.legAng = 0
        self.handAng = 0

    def calculateBody(self, lmList):
        # отклонение плечи
        self.sholdersAng = findAngleBody(lmList[11][1], lmList[11][2],
                                         lmList[12][2], lmList[12][2])
        # отклонение локти
        self.elbowAng = findAngleBody(lmList[13][1], lmList[13][2],
                                      lmList[14][1], lmList[14][2])
        # отклонение таз
        self.pelvisAng = findAngleBody(lmList[23][1], lmList[23][2],
                                       lmList[24][1], lmList[24][2])
        # отклонение колени
        self.kneeAng = findAngleBody(lmList[25][1], lmList[25][2],
                                     lmList[26][1], lmList[26][2])
        # отклонение шеи от перпендикуляра
        self.neckAng = findAngleNeck(lmList[11][1], lmList[11][2],
                                     lmList[12][1], lmList[12][2],
                                     lmList[0][1], lmList[0][2])

        #отклонение смещения осанки
    def findAngleBack(self, x0, y0, x1, y1, x2, y2):
        try:
            self.backAng = int(degrees(atan2(y1 - y0, x1 - x0) - atan2(y2 - y0, x2 - x0)))
        except ZeroDivisionError:
            self.backAng = 0
        if self.backAng < 0:
            self.backAng = abs(self.backAng)
        if self.backAng > 90:
            self.backAng = abs(self.backAng - 180)
        self.backAng = abs(self.backAng)

    def findAngleLegs(self, x0, y0, x1, y1, x2, y2):
        try:
            self.legAng = abs(int(degrees(atan2(y1 - y0, x1 - x0) - atan2(y2 - y0, x2 - x0))))
            if self.legAng > 180:
                self.legAng = 360 - self.legAng
        except ZeroDivisionError:
            self.legAng = 0

        if self.legAng > 180:
            self.legAng = 360 - self.legAng

    def findAngleHand(self, x0, y0, x1, y1, x2, y2):
        try:
            self.handAng = abs(int(degrees(atan2(y1 - y0, x1 - x0) - atan2(y2 - y0, x2 - x0))))
        except ZeroDivisionError:
            self.handAng = 0
