import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = df = pd.read_csv('fcc-forum-pageviews.csv',
                      index_col='date',
                      parse_dates=True)

# Clean data
df = df[(df['value'] >= (df['value'].quantile(0.025)))
        & (df['value'] <= (df['value'].quantile(0.975)))]


def draw_line_plot():
  # Draw line plot
  fig = plt.figure(figsize=(18, 6))

  plt.plot(df, color='firebrick')
  plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
  plt.xlabel('Date')
  plt.ylabel('Page Views')

  # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig


def draw_bar_plot():
  # Copy and modify data for monthly bar plot
  df_bar = df.copy()
  df_bar.reset_index(inplace=True)
  df_bar['year'] = pd.DatetimeIndex(df_bar['date']).year
  df_bar['month'] = pd.DatetimeIndex(df_bar['date']).month_name()
  df_bar = pd.DataFrame(df_bar.groupby(['year', 'month']).mean())
  df_bar.reset_index(inplace=True)
  df_bar['month'] = pd.to_datetime(df_bar['month'], format='%B')
  df_bar = df_bar.pivot(index='year', columns='month', values='value')
  df_bar.columns = df_bar.columns.strftime('%B')

  # Draw bar plot
  fig = df_bar.plot.bar(figsize=(8, 6)).figure
  plt.xlabel('Years')
  plt.ylabel('Average Page Views')

  # Save image and return fig (don't change this part)
  fig.savefig('bar_plot.png')
  return fig


def draw_box_plot():
  # Prepare data for box plots (this part is done!)
  df_box = df.copy()
  df_box.reset_index(inplace=True)
  df_box['Year'] = [d.year for d in df_box.date]
  df_box['Month'] = [d.strftime('%b') for d in df_box.date]
  # Draw box plots (using Seaborn)
  fig, axes = plt.subplots(1, 2, figsize=(18, 6))
  sns.boxplot(x=df_box['Year'],
              y=df_box['value'].rename('Page Views'),
              ax=axes[0]).set(title='Year-wise Box Plot (Trend)')
  
  months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct','Nov', 'Dec']
  
  sns.boxplot(x=df_box['Month'],
              y=df_box['value'].rename('Page Views'),
              order=months,
              ax=axes[1]).set(title='Month-wise Box Plot (Seasonality)')

  # Save image and return fig (don't change this part)
  fig.savefig('box_plot.png')
  return fig
