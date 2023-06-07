class SpaceAge:

    earthSecs=31557600
    PlanetYears={'Mercury':0.2408467,'Venus':0.61519726,'Earth':1.0,'Mars':1.8808158,'Jupiter':11.862615,'Saturn':29.447498,'Uranus':84.016846,'Neptune':164.79132}

    def __init__(self, seconds):
        self.seconds=seconds
    
    def on_earth(self):
        return self.calc('Earth')
    
    def on_mercury(self):
        return self.calc('Mercury')
    
    def on_venus(self):
        return self.calc('Venus')
    
    def on_mars(self):
        return self.calc('Mars')
    
    def on_jupiter(self):
        return self.calc('Jupiter')
    
    def on_saturn(self):
        return self.calc('Saturn')
    
    def on_uranus(self):
        return self.calc('Uranus')
    
    def on_neptune(self):
        return self.calc('Neptune')

    def calc(self,planet):
        return round(self.seconds/(SpaceAge.PlanetYears[planet]*SpaceAge.earthSecs),2)