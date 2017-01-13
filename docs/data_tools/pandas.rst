======
Pandas
======


Key ideas
#########

Here are some key points to remind myself later.

df['gender'] = df.gender.astype('category')


pip install pandas-datareader 

df = pd.read_csv('beatles.csv', converters={'Released': parse})

http://pandas.pydata.org/pandas-docs/stable/timeseries.html#timeseries-offset-aliases

pip install gmaps
jupyter nbextension enable --py gmaps 
jupyter nbextension enable --py --sys-prefix widgetsnbextension

Google API Key
AI--------------

pip install folium


Correlation
###########

.. code-block:: python

   heights.corr(weights)
   heights.corr(np.log(weights))
   heights.corr(weights, method='spearman')
   
Series
######

* s.loc['key'] can use to query and set the value.
* s.append(['China', 'Tai Chi']) will not modify the original series.

DataFrame
#########

* copy: df_copy = df.copy()
* delete: df.drop(['Store 1']) # no effect on df, two parameters: inplace and axis
* delete: del df['Name'] # delete a column, with effect on df
* add: df['Location'] = 'Taipei' # add a new column, all values are 'Taipei'


Read CSV Files
==============

* df = pd.read_csv('olympics.csv', index_col=0, skiprows=1) # for existing headers in the column and row
* df.rename(columns={'old':'new'}, inplace = True)

Query 
======
* Use iloc() and loc() for row based query and use [] for column based query
* df1.count()
* df1 = df1.dropna()
* df1[df1['Cost'] > 10] # masking

Indexing
========

#. df['country'] = df.index # preserve the old indexes
#. df.set_index(['Gold'])
#. df.head() # show first 5 rows
#. df.reset_index() # promote the old indexes into a column and create new indexes

Multiple indexes
----------------

* df.set_index(['State', 'City'])
* df.loc[('Vic', 'Melbourne')]
* df.loc[('Vic', 'Melbourne'), (NSW, 'Sydney')]

#. df = df.set_index([df.index, 'Name'])
#. df.index.names = ['Location', 'Name']
#. df = df.append(pd.Series(data={'Cost': 3.00, 'Item Purchased': 'Kitty Food'}, name=('Store 2', 'Kevyn')))

Missing Values
--------------

* df.fillna()
* df.sort_index()

