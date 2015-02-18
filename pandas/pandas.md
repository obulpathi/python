# Pandas

## Features
* Data structures with labeled axes supporting automatic or explicit data alignment. This prevents common errors resulting from misaligned data and working with differently-indexed data coming from different sources.
* Integrated time series functionality.
* The same data structures handle both time series data and non-time series data.
* Arithmetic operations and reductions (like summing across an axis) would pass on the metadata (axis labels).
* Flexible handling of missing data.
* Merge and other relational operations found in popular database databases (SQL-based, for example)

## Data Structures
* from pandas import Series, DataFrame
* Series can be thought of as a fixed-length, ordered dictionary, a mapping of index values to data values

## Series
series = Series([4, 7, -5, 3])
Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
series.values
series.index
series['a']
series['a'] = 5
s[['a', 'b']]
s[s>3]
s * 2
s + 1
s  / 3
np.exp(s)
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
s = Series(sdata)
s.isnull()
s.isnotnull()
s1 + s2
s.?
s.name = "Population"
s.index?
s.index.name = "States"
s.index = ['a', 't', 'k', 'o']


## DataFrame
* A DataFrame represents a tabular, spreadsheet-like data structure containing an ordered collection of columns, each of which can be a different value type (numeric, string, boolean, etc.). The DataFrame has both a row and column index; it can be thought of as a dictionary of Series (one for all sharing the same index).
* Row-oriented and column-oriented operations in DataFrame are treated roughly symmetrically
* Frames are column and row addressable


data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
frame = DataFrame(data, columns=['year', 'state', 'pop'])

frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                   index=['one', 'two', 'three', 'four', 'five'])

frame2['debt'] = 0
frame2.debt
frame2.debt.one
s = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame.debt = s
obj.reindex(['a', 'b', 'c', 'd', 'e'])
obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)
obj3 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
obj3.reindex(range(6), method='ffill')
df.describe()


## Stastics
count Number of non-NA values
describe Compute set of summary statistics for Series or each DataFrame column
min, max Compute minimum and maximum values
argmin, argmax Compute index locations (integers) at which minimum or maximum value obtained, respectively
idxmin, idxmax Compute index values at which minimum or maximum value obtained, respectively
quantile Compute sample quantile ranging from 0 to 1
sum Sum of values
mean Mean of values
median Arithmetic median (50% quantile) of values
mad Mean absolute deviation from mean value
var Sample variance of values
std Sample standard deviation of values
skew Sample skewness (3rd moment) of values
kurt Sample kurtosis (4th moment) of values
cumsum Cumulative sum of values
cummin, cummax Cumulative minimum or maximum of values, respectively
cumprod Cumulative product of values
diff Compute 1st arithmetic difference (useful for time series)
pct_change Compute percent changes


## IO

## 
