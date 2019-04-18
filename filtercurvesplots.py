import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.font_manager import FontProperties
import numpy as np
import filplot as fp
from matplotlib.backends.backend_pdf import PdfPages
from astropy.table import Table

"""
   The code reads from a file with the format:
   file_name(str), instrument(str), filter_name(str), subplot_number(int), plot_color(str), x_loc(flt), y_loc(flt)
   the file should have no headers
   the delimiter is of 4 spaces with no commas
"""

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['font.family'] = 'Calibri'
font = FontProperties()
font.set_weight('bold')

# Main read part
data = input('Enter filters file name/PATH: ')
can = True
while can is True:
    try:
        tab = Table.read(data, format='ascii.no_header', guess=False, delimiter='\s',
                         names=('file name',
                                'instrument',
                                'filter name',
                                'subplot',
                                'plot color',
                                'name x loc',
                                'name y loc'))
        can = False
    except OSError:
        data = input('file not found... try again: ')

# Plots loop
yminorlocator = AutoMinorLocator(5)
fig = plt.figure(figsize=(8.27, 11.69), dpi=100)
for i in range(0, len(tab['file name'])):
    ax = plt.subplot(max(tab['subplot']), 1, tab['subplot'][i])
    fp.fplots(np.loadtxt(tab['file name'][i], usecols=0), np.loadtxt(tab['file name'][i], usecols=1),
              leg=tab['filter name'][i], col=tab['plot color'][i])
    plt.text(tab['name x loc'][i], tab['name y loc'][i], tab['filter name'][i], fontproperties=font)
    ax.yaxis.set_minor_locator(yminorlocator)

    ax.annotate(tab['instrument'][i], xy=(25000, 1.15), xycoords='data', size=14, ha='right', va='top',
                annotation_clip=False)
    if i == len(tab['file name']) - 1:
        plt.xlabel('Wavelength [Å]')
        plt.xticks([1000, 1400, 1700, 2000, 2500, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000,
                    13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000],
                   [1000, 1400, 1700, 2000, 2500, 3000, 4000, 5000, '', 7000, '', 9000, '', '', 12000, '', '',
                    15000, '', '', '', 19000, '', '', '', '', '', 25000])

ax.annotate('Made by Ido Keinan\nMarch 2019', xy=(2500, -0.5), xycoords='data', size=14, ha='right', va='top',
            annotation_clip=False)
sv = input('Save Pdf? Y/N: ')
if sv == 'y' or sv == 'Y':
    with PdfPages(input('Enter file name: ') + '.pdf') as pdf:
        pdf.savefig(fig, orientation='portrait')
plt.close(fig)
