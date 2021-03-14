# Import
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd

# Setting global parameters for plot design ##############################
plt.rcParams['axes.linewidth'] = 4  # set the value globally
plt.rcParams["font.family"] = "Calibri"  # Change the font used in plots
plt.rcParams["hatch.linewidth"] = 5
plt.rcParams["figure.figsize"] = (10,13)


# Data
r = [0, 1]
raw_data = {'blackBars': [4,20], 'hatchBars': [10,100], 'greyBars': [10,20], 'white': [25,30]}
df = pd.DataFrame(raw_data)

# From raw value to percentage
totals = [i + j + k + n for i, j, k, n in zip(df['blackBars'],df['hatchBars'], df['greyBars'], df['white'])]

blackBars = [i / j * 100 for i, j in zip(df['blackBars'], totals)]
greyBars = [i / j * 100 for i, j in zip(df['greyBars'], totals)]
hatchBars = [i / j * 100 for i, j in zip(df['hatchBars'], totals)]
white = [i / j * 100 for i, j in zip(df['white'], totals)]


# plot
barWidth = 0.70
names = ('Control', 'Carbachol')

# Create green Bars
plt.bar(r, blackBars, color='k', edgecolor='k', width=barWidth, label = 'Long PF',linewidth=3.5)
# Create orange Bars
plt.bar(r, greyBars, bottom=blackBars, color='grey', edgecolor='k', width=barWidth,label='Depolarization block',linewidth=3.5)
# Create orange Bars
plt.bar(r, hatchBars,bottom=[i + j for i, j in zip(blackBars, greyBars)], color='w', edgecolor='k',hatch=r"/", width=barWidth, label ='Self-terminated PF',linewidth=3.5)
# Create blue Bars
plt.bar(r, white, bottom=[i + j + k for i, j, k in zip(blackBars, greyBars, hatchBars)], color='w', edgecolor='k', label = 'No PF',
        width=barWidth,linewidth=3.5)

plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)

# Custom x axis
plt.xticks(r, names,fontweight='bold',fontsize=30)
plt.ylim(0,100)

# Custom y axis
plt.yticks(fontweight='bold',fontsize=30)
plt.gca().yaxis.set_major_formatter(mticker.PercentFormatter())
#plt.gca().minorticks_on()
plt.gca().yaxis.set_tick_params(which='major', length=10, width=3, direction='out')
plt.gca().xaxis.set_tick_params(which='major', length=10, width=5, direction='out')

# Add a legend
plt.legend(bbox_to_anchor=(1,0.6), ncol=1,fontsize=30, frameon=False, 'reverse')
plt.tight_layout()

# Show graphic
plt.gcf().set_size_inches(12, 11)
plt.show()