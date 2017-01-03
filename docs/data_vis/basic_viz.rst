#####################################
Data Visualization Basics with Python
#####################################

Credit:

`Randy Olson`_

.. _Randy Olson: https://www.safaribooksonline.com/library/view/data-visualization-basics/9781771375573/

The Basics
############

Storytelling
============

Signals vs Noises

Pictures tell stories from the data.

4 Steps:

#. Stop worrying about tools. / Stories will dictate tools.
#. Clearly define the story. (theory in mind)
#. Pick the right chart. (can tell the story. more details later)
#. Assess your visualisation. (clear without distraction? no -> start over)

Maximise Story-ink ratio

:math: Story-ink ratio = Story-ink / totoal ink used to print the graphic

Type of Charts
==============

Bar charts
----------

* Most versatile chart type
* Comparisons among categories

Horizontal bar charts
 * one category and long label
 * compared multiple category values over short time periods or negative values

Line charts
-----------

* For many time points
* Compares trends

Pie charts
----------

* Often misuse
* Best for few categories
* **Parts must sum to a meaning whole**
* Show simple proportion for one category

Stacked area charts
-------------------

* line chart + bar chart
* When cumulative proportions matter
* Poor at showing specific values

Histograms
----------

* Spread fo the data
* First go to; Useful for data exploration

Box plots
---------

* Compare/summarise distributions
* Useful for spotting outliers

Scatterplots
------------
* show relationship
* establish correlation / not causation

Chart Selector

.. image:: chart_selector.png

Choosing the right colors
=========================

* Color should add information
* Consider color blinderness (color-blinder simulator)

Types of color schemes
----------------------

* Qualitative
* Sequential (a range of values)
* Diverging (a range of values with a dividing point)
* Print well - both color and B&W (not sure)

Colorbrewer: already implemented in Seaborn http://colorbrewer2.org/#type=sequential&scheme=BuGn&n=3

Common mistakes
===============

* Unlabelled charts
* Using 3-Dimensional charts
* Parts don't sum to a meaningful whole in pie charts
* Too many categories in pie charts (3 or 4)
* Not starting at zero in bar charts
* Failing to normalise data (% of Python users in a city, not number)
* Chartjunk: extraneous labels, pointless images and fancy effects

Bad examples:

* http://viz.wtf/
* https://www.reddit.com/r/dataisugly/

Good practices
==============

* When appropriate, show the (raw) data
* Clarify correlation != Causation
* Label objects and data directly
* Make sure your visualisation stands by itself

Reproducibility in data visualisation
=====================================

* avoid point and click programs
* include the underlying data
* describe your methods in detail

Data sources
============

* government's open data
 - Australia http://data.gov.au/
 - Taiwan http://data.gov.tw
 - USA
  - http://data.gov
  - https://www.cia.gov/library/publications/the-world-factbook/
 - UK http://data.gov.uk
 - UN http://who.int/gho
 - Quandl
 - AWS public data sets http://aws.amazon.com/datasets

Matplotlib
##########

Concept
=======

Steps:

#. create the figure
#. plot the data
   * multiple times if needed
#. configure axes
#. add annotations
#. show/save the figure

.. code-block:: python

   import matplotlib.pyplot as plt

   plt.figure()

   plt.plot(x1_values, y1_values)
   plt.plot(x2_values, y2_values)
   plt.plot(x3_values, y3_values)

   plt.xticks([2012, 2013, 2014, 2015])
   plt.yticks([0, 1, 2, 3, 4, 5, 6])S
   plt.xlim(2012, 2015)
   plt.ylim(1,5)
   plt.xlabel('')
   plt.ylabel('Web Searches')

   plt.legend()
   plt.grid()
   # plt.title()

   plt.savefig('web-searches.png') # pdf, svg ...
   # plt.show()

Jupyter notebook setting
========================
.. code-block:: python

   %matplotlib inline
   %matplotlib notebook

Why the Jupyter Notebook?
-------------------------

#. Interactive
#. Code in the same place as figures
#. Shareable

Styling
=======

Useful code::

   plt.style.available

   with plt.style.context('bmh'):

   with plt.style.context(['figure_formatting', 'grayscale_colors']):
