import pandas as pd


class Tables():
    def __init__(self, tabName='Results.xlsx'):
        super(Tables, self).__init__()

        self.text = {
        'Вид отклонения':
            ['Плечи', 'Таз', 'Локти', 'Колени', 'Шея', 'Осанка', 'Голень/Стопа',
             'Руки вперед', 'Руки в стороны', 'Руки подняты'],
        'Норма отклонений, градус':
            ['0-3', '0-4', '0-2', '0-2', '0-8', '0-8', '100 - 110', '80 - 90', '85 - 90', '170 - 180'],
        'Показания спедери/п.бок':
                         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        'Показания сзади/л.бок':
                         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']}

        self.tabName = tabName

    def load(self):
        df = pd.DataFrame(self.text)
        df.to_excel(self.tabName, sheet_name='Результаты', index=False)

    def firstInput(self, sholdersAng, elbowAng, pelvisAng, kneeAng, neckAng):
        self.text['Показания спедери/п.бок'][0] = sholdersAng
        self.text['Показания спедери/п.бок'][1] = pelvisAng
        self.text['Показания спедери/п.бок'][2] = elbowAng
        self.text['Показания спедери/п.бок'][3] = kneeAng
        self.text['Показания спедери/п.бок'][4] = neckAng

    def secondInput(self, sholdersAng, elbowAng, pelvisAng, kneeAng, neckAng):
        self.text['Показания сзади/л.бок'][0] = sholdersAng
        self.text['Показания сзади/л.бок'][1] = pelvisAng
        self.text['Показания сзади/л.бок'][2] = elbowAng
        self.text['Показания сзади/л.бок'][3] = kneeAng
        self.text['Показания сзади/л.бок'][4] = abs(neckAng - 90)

    def backInputR(self, backAng, legAng):
        self.text['Показания спедери/п.бок'][5] = backAng
        self.text['Показания спедери/п.бок'][6] = legAng

    def backInputL(self, backAng, legAng):
        self.text['Показания сзади/л.бок'][5] = backAng
        self.text['Показания сзади/л.бок'][6] = legAng

    def handInputL(self, handAng):
        self.text['Показания сзади/л.бок'][7] = handAng

    def handInputR(self, handAng):
        self.text['Показания спедери/п.бок'][7] = handAng

    def handToSideR(self, sideAng):
        self.text['Показания спедери/п.бок'][8] = sideAng

    def handToSideL(self, sideAng):
        self.text['Показания сзади/л.бок'][8] = sideAng

    def handToUpR(self, upAng):
        self.text['Показания спедери/п.бок'][9] = 360 - upAng

    def handToUpL(self, upAng):
        self.text['Показания сзади/л.бок'][9] = upAng
