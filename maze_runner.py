import numpy as np
import random
import matplotlib.pyplot as plt
import pickle

infile = open('maze_examples\maze4x6.pckl', 'rb')
data = pickle.load(infile)
infile.close()
print(data)

nr, nc = data.shape  # number of rows and columns in array

pc = []  # will contain open points along the boarder
pr = []

for i, m in enumerate(data[:, 0]):  # looping over most left column
    if m:  # if m is true
        pc.append(0)
        pr.append(i)

for i, m in enumerate(data[:, nc - 1]):  # looping over most right column
    if m:  # if m is true
        pc.append(nc - 1)
        pr.append(i)

for i, m in enumerate(data[0, :]):  # looping over top row
    if m:  # if m is true
        pc.append(i)
        pr.append(0)

for i, m in enumerate(data[nr - 1, :]):  # looping over bottom row
    if m:  # if m is true
        pc.append(i)
        pr.append(nr - 1)

start_point = [pr[0], pc[0]]  # finds starting point
end_point = [pr[1], pc[1]]  # finds end point

new_point_all = []
current_point = start_point
loop_counter = 0

while current_point != end_point:
    possible_moves = []
    if current_point[0] < nr:
        if data[current_point[0] + 1, current_point[1]]:  # Check cell down
            possible_moves.append([current_point[0] + 1, current_point[1]])

    if current_point[1] < nc:
        if data[current_point[0], current_point[1] + 1]:  # check cell right
            possible_moves.append([current_point[0], current_point[1] + 1])

    if current_point[0] > 0:
        if data[current_point[0] - 1, current_point[1]]:  # Check cell up
            possible_moves.append([current_point[0] - 1, current_point[1]])

    if current_point[1] > 0:
        if data[current_point[0], current_point[1] - 1]:  # check cell left
            possible_moves.append([current_point[0], current_point[1] - 1])

    new_point = random.choice(possible_moves)  # New point choices a random co ordinates in possible moves list
    new_point_all.append(new_point)  # appends new points to the new point al list

    plt.imshow(data, cmap="plasma")
    plt.scatter(new_point[1], new_point[0], c="blue", alpha=0.9,
                s=1000)  # Makes a graph of each move as it passes through the while loop
    plt.axis('off')
    plt.show()

    current_point = new_point  # Checks if current point has reached the new point cordinates and kills the loop
    if current_point == end_point:
        print("End point reached")
        break
    loop_counter += 1  # set a loop counter to kill loop because there is a possibility it can run forever
    if loop_counter > 10000:
        print("Maximum number of loops reached")
        break

print(new_point_all)
