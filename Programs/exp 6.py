import numpy as np

time = np.array([0, 1, 2, 3, 4])
position = np.array([0, 15, 25, 20, 10])

total_displacement = position[-1] - position[0]
total_time = time[-1] - time[0]

average_velocity = total_displacement / total_time

print("Total Displacement:", total_displacement)
print("Total Time:", total_time)
print("Average Velocity:", average_velocity)