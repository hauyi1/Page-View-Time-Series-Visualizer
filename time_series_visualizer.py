import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df.set_index('date')
# Clean data
lower_quantile = df['value'].quantile(0.025)
upper_quantile = df['value'].quantile(0.975)

df_cleaned = df[(df['value'] >= lower_quantile) & (df['value'] <= upper_quantile)]


def draw_line_plot():
    plt.subplots(figsize = (20,5))
    sns.lineplot(x='date', y='value', data=df_cleaned).set(title = 'Daily freeCodeCamp Forum Page Views 5/2016-12/2019', xlabel='Date', ylabel='Page Views');





    # Save image and return fig (don't change this part)
    plt.savefig('line_plot.png')
    return plt

# def draw_bar_plot():
#     # Copy and modify data for monthly bar plot
#     df_bar = None

#     # Draw bar plot





#     # Save image and return fig (don't change this part)
#     fig.savefig('bar_plot.png')
#     return fig

# def draw_box_plot():
#     # Prepare data for box plots (this part is done!)
#     df_box = df.copy()
#     df_box.reset_index(inplace=True)
#     df_box['year'] = [d.year for d in df_box.date]
#     df_box['month'] = [d.strftime('%b') for d in df_box.date]

#     # Draw box plots (using Seaborn)





#     # Save image and return fig (don't change this part)
#     fig.savefig('box_plot.png')
#     return fig
