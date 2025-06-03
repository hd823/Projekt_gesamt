import pandas as pd
import matplotlib.pyplot as plt
from source.functions_Leistungskurve2 import load_data, plot_power, plot_power_duration_curve

FILE_PATH = "data/activity.csv"

df_power = load_data(FILE_PATH)
fig_power = plot_power(df_power)
fig_power_duration_curve = plot_power_duration_curve(df_power)

plt.show()


