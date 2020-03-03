import matplotlib.pyplot as plt
from matplotlib import interactive

plt.figure(1)
plt.plot(
    [1, 2, 3, 4], # Xdata
    [1, 4, 9, 16],# Ydata
    color='green', 
    linestyle='-.',
    label='Green Data'
)
plt.plot(
    [2, 3, 4, 5],
    [2, 3, 4, 5], 
    color='black', 
    linestyle='-',
    label='black data'
)

plt.ylabel('Y data')
plt.xlabel('Time (s)')
plt.legend() # show the label declared inside the plot method

# set interactive=True at the firs plot, interactive=False at the last one
interactive(True)
plt.show()
# -------------------------------------
# Subplot

plt.figure(2)
# create the first panel
plt.subplot(2,1,1) #lines, columns, panel number
panel_1 = plt.subplot(2,1,1)
panel_1.set_xlim([0, 6])
panel_1.set_ylim([0, 20])
plt.plot(
    [1, 2, 3, 4], # Xdata
    [1, 4, 9, 16],# Ydata
    color='green', 
    linestyle='-.',
    label='Green Data'
)
plt.ylabel('Y panel 1')
plt.xlabel('Time (s)')
plt.legend() # show the label declared inside the plot method

# create the second panel
panel_2 = plt.subplot(2,1,2)
panel_2.set_xlim([0, 6])
panel_2.set_ylim([0, 20])

plt.plot(
    [2, 3, 4, 5],
    [2, 3, 4, 5], 
    color='black', 
    linestyle='-',
    label='black data'
)
plt.ylabel('Y panel 2')
plt.xlabel('Time (s)')
plt.legend() # show the label declared inside the plot method

# Show interactive=False at the last plot
interactive(False)
plt.show()