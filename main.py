"""
Calculates the search distance and telescope size needed to find signs
of life, emitting light of a given minimum wavelength, with a given
confidence, given the average probability of life around stars in a
galactic disc of given dimensions and average stellar density.
"""

import database, graphing, loading, simulation
import json
from contextlib import closing
import sqlite3

def _run(galaxy, config):
    """
    Run simulations of decreasing probability that each system bears
    life.
    """
    probabilities, search_distances, base_lengths = [], [], []
    probability = galaxy.life_probability
    while probability >= config.minimum_probability:
        stars = simulation.trials(config.minimum_confidence, probability)
        volume = stars / galaxy.stellar_density
        search_distance = simulation.search_distance(
            volume, galaxy.disc_half_thickness, galaxy.altitude_above_ecliptic)
        base_length = simulation.base(galaxy.minimum_wavelength,
                                      search_distance,
                                      galaxy.life_sign_size)
        probabilities.append(probability)
        search_distances.append(search_distance)
        base_lengths.append(base_length)
        probability += config.probability_increment
    return probabilities, search_distances, base_lengths


def main():
    """
    Load configuration and galactic data, run a simulation, and graph
    and save the output.
    """
    with open("data.json", 'r') as f:
        galaxy = loading.Galaxy(json.load(f))
    with open("config.json", 'r') as f:
        config = loading.Config(json.load(f))
    probabilities, search_distances, base_lengths = _run(galaxy, config)
    database.export(probabilities, search_distances, base_lengths)
    graphing.distance_graph(probabilities, search_distances)
    graphing.base_graph(probabilities, base_lengths)

    
if __name__ == "__main__": main()
