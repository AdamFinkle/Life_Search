class Config:
    """Configuration data holder."""
    def __init__(self, json):
        self._minimum_probability = json["minimumProbability"]
        self._probability_increment =  json["probabilityIncrement"]
        self._minimum_confidence = json["minimumConfidence"]

    @property
    def minimum_probability(self):
        """Minimum probability to consider"""
        return self._minimum_probability

    @property
    def probability_increment(self):
        """Increment of probability to iterate"""
        return self._probability_increment

    @property
    def minimum_confidence(self):
        """
        Minimum confidence to declare life absent from the galaxy
        """
        return self._minimum_confidence


class Galaxy:
    """
    Galaxy data holder.
    """
    def __init__(self, json):
        meters_per_lightyear = 9.46 * 10 ** 15
        self._stellar_density = (json["stellarDensity"]
                                / meters_per_lightyear ** 3)
        self._disc_half_thickness = (json["discHalfThickness"]
                                   * meters_per_lightyear)
        self._altitude_above_ecliptic = (json["altitudeAboveEcliptic"]
                                       * meters_per_lightyear)
        self._minimum_wavelength = json["minimumWavelength"] * 10 ** -9
        self._life_sign_size = json["lifeSignSize"]
        self._life_probability = json["lifeProbability"]

    @property
    def stellar_density(self):
        """Average galactic stellar density"""
        return self._stellar_density

    @property
    def disc_half_thickness(self):
        """
        Distance from ecliptic to top and bottom of galactic disc in
        lightyears
        """
        return self._disc_half_thickness

    @property
    def altitude_above_ecliptic(self):
        """Altitude of observer above the ecliptic"""
        return self._altitude_above_ecliptic

    @property
    def minimum_wavelength(self):
        """
        Minimum wavelength of light escaping atmospheres of life-bearing
        worlds
        """
        return self._minimum_wavelength

    @property
    def life_sign_size(self):
        """Maximum size of life-signs in meters"""
        return self._life_sign_size

    @property
    def life_probability(self):
        """Probability of finding life on random star system"""
        return self._life_probability
