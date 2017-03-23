# imports
from pandas import read_csv, DataFrame
from sklearn import preprocessing

# DataFrames
bus_df = read_csv('./data/bus.csv')
dancing_df = read_csv('./data/dancing.csv')
stairs_df = read_csv('./data/stairs.csv')
running_df = read_csv('./data/running.csv')
walking_df = read_csv('./data/walking.csv')

# normalization
bus_df = DataFrame(preprocessing.normalize(bus_df.values, norm='l2'))
dancing_df = DataFrame(preprocessing.normalize(dancing_df.values, norm='l2'))
stairs_df = DataFrame(preprocessing.normalize(stairs_df.values, norm='l2'))
running_df = DataFrame(preprocessing.normalize(running_df.values, norm='l2'))
walking_df = DataFrame(preprocessing.normalize(walking_df.values, norm='l2'))

# frame and feature extraction
start = 0
stop = int(3 * 60 / 0.01) # 3 minutes
interval = int(10 / 0.01) # 10 seconds

features = {
  'X kurt': [], 'Y kurt': [], 'Z kurt': [],
  'X max':  [], 'Y max':  [], 'Z max':  [],
  'X mean': [], 'Y mean': [], 'Z mean': [],
  'X min':  [], 'Y min':  [], 'Z min':  [],
  'X skew': [], 'Y skew': [], 'Z skew': [],
  'X std':  [], 'Y std':  [], 'Z std':  [],
  'activity': []
}

def extract_features(activity, df):
  features['X kurt'].append(df[df.columns[0]].kurt())
  features['Y kurt'].append(df[df.columns[1]].kurt())
  features['Z kurt'].append(df[df.columns[2]].kurt())

  features['X max'].append(df[df.columns[0]].max())
  features['Y max'].append(df[df.columns[1]].max())
  features['Z max'].append(df[df.columns[2]].max())

  features['X mean'].append(df[df.columns[0]].mean())
  features['Y mean'].append(df[df.columns[1]].mean())
  features['Z mean'].append(df[df.columns[2]].mean())

  features['X min'].append(df[df.columns[0]].min())
  features['Y min'].append(df[df.columns[1]].min())
  features['Z min'].append(df[df.columns[2]].min()) 

  features['X skew'].append(df[df.columns[0]].skew())
  features['Y skew'].append(df[df.columns[1]].skew())
  features['Z skew'].append(df[df.columns[2]].skew())

  features['X std'].append(df[df.columns[0]].std())
  features['Y std'].append(df[df.columns[1]].std())
  features['Z std'].append(df[df.columns[2]].std())

  features['activity'].append(activity)

for i in range(start, stop, interval):
  extract_features('bus', bus_df[i:i + interval])
  extract_features('dancing', dancing_df[i:i + interval])
  extract_features('stairs', stairs_df[i:i + interval])
  extract_features('running', running_df[i:i + interval])
  extract_features('walking', walking_df[i:i + interval])

DataFrame.from_dict(features).to_csv('./data/features.csv', index=False)