import calculatePose as cp
import winsound
import tables as tb

t = 1000
freq = 600

class timerCount():
    def __init__(self, theEnd=False):
        super(timerCount, self).__init__()

        self.theEnd = theEnd
        self.table = tb.Tables()

    def endingTime(self, mainTime, lmList):
        calcul = cp.calculatePose()
        #Стойка спереди
        if mainTime == 10:
            calcul.calculateBody(lmList)
            self.table.firstInput(calcul.sholdersAng, calcul.elbowAng, calcul.pelvisAng,
                                  calcul.kneeAng, calcul.neckAng)
            winsound.Beep(freq, t)
        # Стойка сзади
        elif mainTime == 20:
            calcul.calculateBody(lmList)
            self.table.secondInput(calcul.sholdersAng, calcul.elbowAng,
                                   calcul.pelvisAng, calcul.kneeAng, calcul.neckAng)
            winsound.Beep(freq, t)
        # Стойка левым боком
        elif mainTime == 30:
            calcul.findAngleBack(lmList[23][1], lmList[23][2],
                                 lmList[11][1], lmList[11][2],
                                 lmList[25][1], lmList[25][2])
            calcul.findAngleLegs(lmList[27][1], lmList[27][2],
                                 lmList[25][1], lmList[25][2],
                                 lmList[31][1], lmList[31][2]) #[29][2]
            self.table.backInputL(calcul.backAng, calcul.legAng)
            winsound.Beep(freq, t)
        # Стойка левым боком, руки вперед
        elif mainTime == 35:
            calcul.findAngleHand(lmList[11][1], lmList[11][2],
                                 lmList[13][1], lmList[13][2],
                                 lmList[23][1], lmList[23][2])
            self.table.handInputL(calcul.handAng)
            winsound.Beep(freq, t)
        # Стойка правым боком
        elif mainTime == 45:
            calcul.findAngleBack(lmList[24][1], lmList[24][2],
                                 lmList[12][1], lmList[12][2],
                                 lmList[26][1], lmList[26][2])
            calcul.findAngleLegs(lmList[28][1], lmList[28][2],
                                 lmList[26][1], lmList[26][2],
                                 lmList[32][1], lmList[32][2]) #[30][2]
            self.table.backInputR(calcul.backAng, calcul.legAng)
            winsound.Beep(freq, t)
        # Стойка правым боком, руки вперед
        elif mainTime == 50:
            calcul.findAngleHand(lmList[12][1], lmList[12][2],
                                 lmList[14][1], lmList[14][2],
                                 lmList[24][1], lmList[24][2])
            self.table.handInputR(calcul.handAng)
            winsound.Beep(freq, t)
        #руки в стороны
        elif mainTime == 60:
            calcul.findAngleHand(lmList[12][1], lmList[12][2],
                                 lmList[14][1], lmList[14][2],
                                 lmList[24][1], lmList[24][2])
            self.table.handToSideR(calcul.handAng)
            calcul.findAngleHand(lmList[11][1], lmList[11][2],
                                 lmList[13][1], lmList[13][2],
                                 lmList[23][1], lmList[23][2])
            self.table.handToSideL(calcul.handAng)
            winsound.Beep(freq, t)
        # поднятие рук вверх
        elif mainTime == 65:
            calcul.findAngleHand(lmList[12][1], lmList[12][2],
                                 lmList[14][1], lmList[14][2],
                                 lmList[24][1], lmList[24][2])
            self.table.handToUpR(calcul.handAng)
            calcul.findAngleHand(lmList[11][1], lmList[11][2],
                                 lmList[13][1], lmList[13][2],
                                 lmList[23][1], lmList[23][2])
            self.table.handToUpL(calcul.handAng)
            winsound.Beep(freq, t)
        elif mainTime == 70:
            self.theEnd = True


    def save(self):
        self.table.load()
