from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

s = True
while s:

    number = input("Number: ")
    coords = np.array(np.random.randint(0, number, (number, 3)))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(coords[:,0], coords[:,1], coords[:,2])
    plt.show()
    cont = raw_input("Continue? (y/n)")
    print(type(cont))
    if cont == 'n':
        s = False