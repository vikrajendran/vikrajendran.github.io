# -*- coding: utf-8 -*-

# -- Sheet --

import pandas as pd 
import numpy as np

from scipy import stats
import math

from mplsoccer import PyPizza, add_image, FontManager
import matplotlib.pyplot as plt

df1 = pd.read_csv('Untitled spreadsheet - Sheet1 (1).csv')

df2 = pd.read_csv('Untitled spreadsheet - Sheet1 (2).csv')

df3 = pd.read_csv('Untitled spreadsheet - Sheet1 (3).csv')

df4 = pd.read_csv('Untitled spreadsheet - Sheet1 (4).csv')

df1 = pd.merge(df1, df2, on='Player')

df1.head()

df2 = pd.merge(df3, df4, on='Player')

df2.head()

df = pd.merge(df1, df2, on='Player')

df.head()

df = df.loc[df['90s_x_x']>15]

df.head().reset_index()

df = df.loc[df['Pos_x_x']== 'MF']

df['ProgCarries/90'] = (df['Prog_x'])/(df['90s_x_x'])

df['xA/90'] = (df['xA'])/(df['90s_y_x'])

df['ProgPasses/90'] = (df['Prog_y'])/(df['90s_y_x'])

df['Touches/90'] = (df['Touches'])/(df['90s_x_x'])

df['Passes/90'] = (df['Cmp'])/(df['90s_y_x'])

df['Aerials Won/90'] = (df['Won'])/(df['90s_y_y'])

df['PossesionWinningTackles/90'] = (df['TklW▼'])/(df['90s_x_y'])

df['Interceptions/90'] = (df['Int_x'])/(df['90s_x_y'])

df.head(10).reset_index()

params = list(df.columns)

print(params)

params = params[126:]

print(params)

player = df.loc[df['Player']== 'Thiago Alcántara'].reset_index()

player = list(player.loc[0])
player = player[127: ]

print(player)

print(len(params)),(len(player))

values = []
for x in range(len(params)):
    values.append(math.floor(stats.percentileofscore(df[params[x]],player[x])))

# instantiate PyPizza class
baker = PyPizza(
    params=params,                  # list of parameters
    straight_line_color="#000000",  # color for straight lines
    straight_line_lw=1,             # linewidth for straight lines
    last_circle_lw=1,               # linewidth of last circle
    other_circle_lw=1,              # linewidth for other circles
    other_circle_ls="-."            # linestyle for other circles
)

# plot pizza
fig, ax = baker.make_pizza(
    values,              # list of values
    figsize=(8, 8),      # adjust figsize according to your need
    param_location=110,  # where the parameters will be added
    kwargs_slices=dict(
        facecolor="#f4c2c2", edgecolor="#000000",
        zorder=2, linewidth=1
    ),                   # values to be used when plotting slices
    kwargs_params=dict(
        color="#000000", fontsize=12,
         va="center"
    ),                   # values to be used when adding parameter
    kwargs_values=dict(
        color="#000000", fontsize=12,
         zorder=3,
        bbox=dict(
            edgecolor="#000000", facecolor="#f4c2c2",
            boxstyle="round,pad=0.2", lw=1
        )
    )                    # values to be used when adding parameter-values
)

# add title
fig.text(
    0.515, 0.97, "Thiago Alcántara - Liverpool FC", size=18,
    ha="center" , color="#000000"
)

# add subtitle
fig.text(
    0.515, 0.942,
    "Percentile Rank vs Top-Five League Midfielders | Season 2021-22",
    size=15,
    ha="center", color="#000000"
)

# add credits
#CREDIT_1 = "data: statsbomb viz fbref"
#CREDIT_2 = "inspired by: @Worville, @FootballSlices, @somazerofc & @Soumyaj15209314"

#fig.text(
    #0.99, 0.005, f"{CREDIT_1}\n{CREDIT_2}", size=9,
     #color="#000000",
    #ha="right"
#)


plt.savefig('C:\\Users\\vikra\\OneDrive\\Documents\\Data.png', format ='png')

plt.show()



