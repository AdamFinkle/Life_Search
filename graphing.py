import matplotlib.pyplot as plt

def distance_graph(probabilities, search_distances):
    fig = plt.figure()
    plt.xlim(0, probabilities[0])
    plt.plot(probabilities, search_distances)
    plt.title("Distance for Probability")
    plt.xlabel("Life probability in random system")
    plt.ylabel("Search radius (meters)")
    plt.show()


def base_graph(probabilities, base_lengths):
    fig = plt.figure()
    plt.xlim(0, probabilities[0])
    plt.plot(probabilities, base_lengths)
    plt.title("Base for Probability")
    plt.xlabel("Life probability in random system")
    plt.ylabel("Telescope array base (meters)")
    plt.show()
