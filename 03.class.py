class BlackBox:
    def __init__(self, name, price):
        self.name=name
        self.price=price

class VideoMaker:
    def make(self):
        print('추억용 여행 영상 제작')

class MailSender:
    def send(self):
        print('메일발송')
        

class TravelBlackBox(BlackBox, VideoMaker, MailSender):
    def __init__(self, name, price, sd):
        super().__init__(name, price)
        self.sd = sd
    
    def set_travel_mode(self, min):
        print(f'{self.name} {min}분 동안 여행 모드 ON')

class AdvancedTravelBlackBox(TravelBlackBox):
    def set_travel_mode(self, min):
        print(f'{self.name} {min}분 동안 여행 모드 ON')
        self.make()
        self.send()
            


        

b1=BlackBox('까망이',200000)
b2=AdvancedTravelBlackBox('하양이',100000, 64)
b2.set_travel_mode(15)