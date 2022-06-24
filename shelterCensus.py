#Maya Carla Loleatha Anderson
#maya.anderson86@myhunter.cuny.edu
#this program graphs the total num of
#indiv. in NYC shelter 10'-16

import matplotlib.pyplot as plt
import pandas as pd

inF = input("Enter name of input file: ")
outF = input("Enter name of output file: ")

homeless = pd.read_csv(inF)


homeless['Fraction Children'] = homeless['Total Children in Shelter']/ homeless['Total Individuals in Shelter']


homeless.plot(x = "Date of Census", y = "Fraction Children")
plt.show()

fig = plt.gcf()
fig.savefig(outF)
