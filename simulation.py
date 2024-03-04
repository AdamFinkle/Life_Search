import math

def trials(confidence, probability):
    """
    Trials
    P = (1-p)^n
    ln(P) = n * ln(1-p)
    ln(P) / n = ln(1-p) ~ -p
    p = -ln(P)/n
    P = 1-c
    n = -ln(1-c)/p
    """
    return round(-math.log(1 - confidence) / probability)


def base(wavelength, distance, size):
    """
    Base Separation
    a = L/B
    A = atan(r/R) ~ r/R
    a = A
    L/B = r/R
    B = LR/r
    """
    return wavelength * distance / size


def search_distance(volume, thickness, altitude):
    """Returns maximum distance in volume to be searched."""
    sphere_radius = ((3*volume)/(4*math.pi))**(1./3.)
    if altitude + sphere_radius <= thickness/2 and altitude-sphere_radius >= -thickness/2:
        return sphere_radius
    else: return bounded_sphere_radius(volume, thickness, altitude)


def bounded_sphere_radius(volume, thickness, altitude):
    """
    Returns the radius of a volume equal to a sphere bounded by planes.

    Given,
    r = radius, t = thickness/2, w = altitude
    V = sphere - cap_1 - cap_2
    sphere = (4/3)pi * r^3
    cap = (pi/3)(3r-h)h^2
    h_1 = r - t + w
    h_2 = r - t - w

    Therefore,
    cap_1 = (pi/3)(2r+t-w)(r-t+w)^2
    cap_2 = (pi/3)(2r+t+w)(r-t-w)^2

    Therefore,
    V = (4/3)pi * r^3 - (pi/3)(2r+t-w)(r-t+w)^2 - (pi/3)(2r+t+w)(r-t-w)^2

    Distributing and simplifying,
    3V/4pi = r^3 - 2wr^2 - (w^2)r + wtr + wt^2 + (w^2)t
    
    Rewriting as a cubic,
    ar^3 + br^2 + cr + d = 0
    a = 1, b = -2w, c = wt, d = wt^2 + (w^2)t - 3V/4pi

    Depressing the cubic by change of variable,
    x = r - b/3a
    x^3 + px + q = 0
    p = (3ac - b^2)/(3a^2)
    q = (2b^3 - 9abc + 27(a^2)d)/(27a^3)

    For a depressed cubic y^3 + my = n,
    y = (n/2 + delta^(1/2))^(1/3) + (n/2 + delta^(1/2))^(1/3)
    delta = (n^2)/2 + (m^3)/27

    Here, y = x, m = p, n = -q
    
    Therefore,
    x = (-q/2 + delta^(1/2))^(1/3) + (-q/2 + delta^(1/2))^(1/3)
    delta = (-q^2)/2 + (p^3)/27

    QED, r = x + b/3a
    """
    w = altitude; t = thickness/2; V = volume
    a = 1; b = 2*w; c = w*t; d = w*t*t + w*w*t - 3*V/(4*math.pi)
    p = (3*a*c - b**2)/(3*a**2)
    q = (2*b**3 - 9*a*b*c + 27*a**2 *d)/(27*a**3)
    delta = (q**2 / 2) + (p**3 / 27)
    x = (-q/2 + math.sqrt(delta))**(1./3.) + (-q/2 + math.sqrt(delta))**(1./3.)
    return x + b/(3*a)
