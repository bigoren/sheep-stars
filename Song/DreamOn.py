from Song import Song
from Animations_Sheep.SheepConfettiAnimation import SheepConfettiAnimation
from Animations_Sheep.SpinningHeadAnimation import SpinningHeadAnimation

class DreamOnSong(Song):

    def __init__(self):
        Song.__init__(self)
        self.file = '1-Sleepy_Koala_-_Dans_La_Main_De_Chronos.wav'
        
        self.confettiAnm = SheepConfettiAnimation(self.smallSheep)
        self.spinningAnm = SpinningHeadAnimation(self.smallSheep, [50,130,200], 4)

        self.confettiAnm2 = SheepConfettiAnimation(self.bigSheep34)
        self.spinningAnm2 = SpinningHeadAnimation(self.bigSheep34, [50,130,200], 4)

        self.plan = [[0,8000,[self.confettiAnm, self.confettiAnm2]],
                    [8000,10000,[self.spinningAnm, self.spinningAnm2]],
                    [10000,18000,[self.confettiAnm, self.confettiAnm2]],
                    [18000,20000,[self.spinningAnm, self.spinningAnm2]],
                    [20000,28000,[self.confettiAnm, self.confettiAnm2]],
                    [28000,30000,[self.spinningAnm, self.spinningAnm2]],
                    [30000,38000,[self.confettiAnm, self.confettiAnm2]],
                    [38000,40000,[self.spinningAnm, self.spinningAnm2]]]
                    #[107000,49,[self.confettiAnm]]]
    
            
    def apply_animations(self, current_time):
        if (current_time % 10 == 0):
            print current_time
        for block in self.plan:
            start_time = block[0]
            end_time = block[1]
            animations = block[2]
            if current_time > start_time and current_time < end_time:
                duration = end_time - start_time
                percent = (current_time - start_time) / float(duration)
                for animation in animations:  
                    animation.apply(percent)
