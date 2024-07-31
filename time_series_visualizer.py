import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import calendar

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df.set_index('date')
# Clean data
lower_quantile = df['value'].quantile(0.025)
upper_quantile = df['value'].quantile(0.975)

df= df[(df['value'] >= lower_quantile) & (df['value'] <= upper_quantile)]


def draw_line_plot():
    fig = plt.figure()
    plt.plot(df['date'], df['value'], color='red')
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Month'] = pd.DatetimeIndex(df_bar['date']).month
    df_bar['Year'] = pd.DatetimeIndex(df_bar['date']).year
    df_bar['Month'] = df_bar['Month'].apply(lambda x: calendar.month_name[x])
    # Draw bar plot
    fig, ax = plt.subplots(figsize=(12, 6))
    hue_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    ax = sns.barplot(x = 'Year',
                y = 'value',
                hue = 'Month',
                data = df_bar,
                hue_order = hue_order,
                palette="tab10",
                errorbar=('ci', 0)
                )

    ax.set(ylabel='Average Page Views', xlabel='Years')
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box['Month'] = pd.DatetimeIndex(df_box['date']).month
    df_box['Year'] = pd.DatetimeIndex(df_box['date']).year
    df_box['Month'] = df_box['Month'].apply(lambda x: calendar.month_abbr[x])

    # Draw box plots (using Seaborn)
    fig, axs = plt.subplots(ncols=2, figsize=(18,6))
    sns.boxplot(data=df_box, x='Year', y='value', flierprops={"marker": "."}, ax=axs[0])
    axs[0].set(ylabel='Page Views', xlabel='Year')
    axs[0].set_title('Year-wise Box Plot (Trend)')
    sns.boxplot(data=df_box, x='Month', y='value', flierprops={"marker": "."}, ax=axs[1], order= ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    axs[1].set(ylabel='Page Views', xlabel='Month')
    axs[1].set_title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
