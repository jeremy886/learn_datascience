#############
Think Stats 2
#############

Data Sources
############

* http://iiqs.mohw.gov.tw/index.aspx

Jupyter-Notebook (Python 3.6)
##############################

* https://github.com/jeremy886/DataExploration

Code update::

   # Code Update
   #
   #from IPython.html.widgets import interact, fixed
   #from IPython.html import widgets
   from ipywidgets.widgets import interact, fixed
   from ipywidgets import widgets

   # slider = widgets.FloatSliderWidget(min=0, max=4, value=2)
   # ipywidgets.widgets.widget_float.FloatSlider
   slider = widgets.widget_float.FloatSlider(min=0, max=4, value=2)

   # slider = widgets.IntSliderWidget(min=10, max=1000, value=100)
   slider = widgets.widget_int.IntSlider(min=10, max=1000, value=100)

Statistical Inference
#####################

* cross-sectional vs longitudinal study
* samples and populations

Summary Statistics
==================

* central tendency
* modes
* spread
* tails
* outliers
* mean, average

variance
--------

* standard deviation

Effect size
===========

Math equation



http://greenteapress.com/thinkstats2/thinkplot.html

pmf 
===

3 types of plots for PMF
------------------------

.. code-block::

   import thinkstats2
   
   pmf = thinkstats2.Pmf(live.prglngth)
   for val, prob in pmf.Items():
      print(val, prob)


   # Histogram
   thinkplot.PrePlot(1)
   thinkplot.Hist(pmf)
   thinkplot.Config(xlabel='Pregnancy length (weeks)',
                    ylabel='PMF', 
                    xlim=[0, 50],
                    legend=False)

   # PMF
   thinkplot.PrePlot(1)
   thinkplot.Pmf(pmf)
   thinkplot.Config(xlabel='Pregnancy length (weeks)',
                    ylabel='PMF', 
                    xlim=[0, 50])

   #PDF
   thinkplot.PrePlot(1)
   thinkplot.Pdf(pmf)
   thinkplot.Config(xlabel='Pregnancy length (weeks)',
                    ylabel='PMF', 
                    xlim=[0, 50])


Multiple PMF
------------

.. code-block::

   firsts = live[live.birthord == 1]
   others = live[live.birthord != 1]
   
   pmf_firsts = thinkstats2.Pmf(firsts.totalwgt_lb, label='firsts')
   pmf_others = thinkstats2.Pmf(others.totalwgt_lb, label='others')
   
   thinkplot.PrePlot(2)
   thinkplot.Pdfs([pmf_firsts, pmf_others])
   thinkplot.Config(xlabel='Birth weight (lbs)',
                    ylabel='PMF')

CDF
===

.. code-block::

   cdf_weight = thinkstats2.Cdf(live.totalwgt_lb)
   thinkplot.PrePlot(1)
   thinkplot.Cdf(cdf_weight)
   thinkplot.Config(xlabel='Birth weight (lbs)',
                    ylabel='CDF')

* cumulative distribution functions (CDFs) are a better choice for data exploration

Multiple CDF
------------

.. code-block::

   firsts = live[live.birthord == 1]
   others = live[live.birthord != 1]
   
   cdf_firsts = thinkstats2.Cdf(firsts.totalwgt_lb, label='firsts')
   cdf_others = thinkstats2.Cdf(others.totalwgt_lb, label='others')
   
   thinkplot.PrePlot(2)
   thinkplot.Cdfs([cdf_firsts, cdf_others])
   thinkplot.Config(xlabel='Birth weight (lbs)',
                    ylabel='CDF',
                    legend=True)


Scatter plots
=============

* Jitter data to remove effect of roundoff.
* Adjust marker size and alpha to avoid saturation.
* Consider hexplot to reduce time and size.

Correlation
===========

* Correlation measures the strength of a linear relationhip.
* But it's important to look at the relationship before blindl computing correlation.
* Correlation doesn't say anything about slope, which might be more imporant.
* To estimate slope, use least squares or other kinds regression.
* An impressive sounding correlation, like 0.5, corresponds to a less impressive reduction in variance, like 0.25, and even less impressive reduction in RMSE(root mean squared error), like 13%.


Statistical inference
#####################

* Effect size
* Quantifying pervision
* Hypthesis testing


Using data from a sample to infer information about a population.

* Effect size: usually a single number, ideally comparable across studies.
* Confidence interval and/or standard error: quantifies the prevision of the estimate.
* p-value: indicates whether the apparent efffect might be due to chance.

* Effect size: by far the most important!
* Confidence interval and/or standard error: a distant second.
* p-value: an even more distant third.

Effect size
###########




* Obvious measure of effect size is difference in means (with a unit, like cm; absolute difference)
* Relative difference, as a percentage, might be useful, but you might have to choose the denominator.
* Cohen's d is symmetric and standadised, so comparable across studies.
* And with Cohen's d, you can compute relevant summary statistics.

Example
=======

* data from the Behavioral Risk Factor Surveillance System (BRFSS) to estimate the mean and standard deviation of height in cm for adult women and men in the U.S.
* use scipy.stats.norm to represent the distributions. 
* The result is an rv object (which stands for random variable).

Height data::

   mu1, sig1 = 178, 7.7
   male_height = scipy.stats.norm(mu1, sig1)
   mu2, sig2 = 163, 7.3
   female_height = scipy.stats.norm(mu2, sig2)

Samples::

   male_sample = male_height.rvs(1000)
   female_sample = female_height.rvs(1000)
   # samples are numpy arrays

Use samples to compute means and standard deviations::

   mean1, std1 = male_sample.mean(), male_sample.std()
   mean2, std2 = female_sample.mean(), female_sample.std()

Absolute Difference
-------------------

   difference_in_means = male_sample.mean() - female_sample.mean()

Relative difference
-------------------

::

   # you have to choose the denominator
   
   # male_sample.mean() is the denominator
   #
   relative_difference = difference_in_means / male_sample.mean()
   relative_difference * 100   # percent
   
   # female_sample.mean() is the denominator
   #
   relative_difference = difference_in_means / female_sample.mean()
   relative_difference * 100    # percent

Relative difference (Alternatives)
----------------------------------

* As probabilities, they don't depend on units of measure, so they are comparable between studies.
* They are expressed in operational terms, so a reader has a sense of what practical effect the difference makes.

overlap::
   # threshold
   #
   thresh = (std1 * mean2 + std2 * mean1) / (std1 + std2)

   male_below_thresh = sum(male_sample < thresh)
   female_above_thresh = sum(female_sample > thresh)
   
   overlap = male_below_thresh / len(male_sample) + female_above_thresh / len(female_sample)

misrepresentation rate::

   misclassification_rate = overlap / 2

probability of superiority::

   # In this context it's the probability that a randomly-chosen man is taller than a randomly-chosen woman.
   sum(x > y for x, y in zip(male_sample, female_sample)) / len(male_sample)

Cohen's  d
-----------

d  is the difference in means, standardized by dividing by the standard deviation. Here's a function that computes it::

   def CohenEffectSize(group1, group2):
       """Compute Cohen's d.

      group1: Series or NumPy array
      group2: Series or NumPy array

      returns: float
      """
      diff = group1.mean() - group2.mean()

      n1, n2 = len(group1), len(group2)
      var1 = group1.var()
      var2 = group2.var()

      pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
      d = diff / numpy.sqrt(pooled_var)
      return d

   CohenEffectSize(male_sample, female_sample)


Use Cohen's d to find the overlap and superiority::

   def overlap_superiority(control, treatment, n=1000):
       """Estimates overlap and superiority based on a sample.
       
       control: scipy.stats rv object
       treatment: scipy.stats rv object
       n: sample size
       """
       control_sample = control.rvs(n)
       treatment_sample = treatment.rvs(n)
       thresh = (control.mean() + treatment.mean()) / 2
       
       control_above = sum(control_sample > thresh)
       treatment_below = sum(treatment_sample < thresh)
       overlap = (control_above + treatment_below) / n
       
       superiority = sum(x > y for x, y in zip(treatment_sample, control_sample)) / n
       return overlap, superiority

   control = scipy.stats.norm(0, 1)
   treatment = scipy.stats.norm(cohen_d, 1)
   o, s = overlap_superiority(control, treatment)


::
   # Code Update
   # slider = widgets.FloatSliderWidget(min=0, max=4, value=2)
   # ipywidgets.widgets.widget_float.FloatSlider
   slider = widgets.widget_float.FloatSlider(min=0, max=4, value=2)

Effect Size, Difference in Proportions
======================================

================== ================== ============== ========== ==============
Treatment          Difference in rate Percent change Odds ratio Log odds ratio
================== ================== ============== ========== ==============
Administer peanuts -14 points         -83%           0.15       -0.82
Withhold peanuts   +14 points         +467%          6.6        +0.82
================== ================== ============== ========== ==============

Quantifying Percision
=====================

What could possibly go wrong?

* Sampling bias
* Measurement error
* Random error

Difference between Standard Deviation and Standard Error

* SD is about the population
* SE is about the statistics
 
Summary
-------

* SE and CI quantify variability due to random sampling.
* Resampling is a simple and general way to compute them.
* Don't forget about other sources of error.

Hypothesis Test
===============

Test statistic:
   Whatever number you choose to quantify the magnitude of the effect.

Null Hypothesis:
   A model of a hypothetical world where the apparent effect is not real.

Permutation test:
   If the test statistic is a difference in means, we can simulate the nul hypothesis by pooling the groups and shuffling.

p-value:
   The p-value is the probability that the test statistic, under the null hypothesis, exceeds the observed value.

   If it's small, you can conclude that the apparent effect is probably not due to chance.


Interpreting p-values
---------------------

.. image:: https://imgs.xkcd.com/comics/p_values_2x.png

Suggestions:
   Less than 1%: the apparent effect is probably not due to chance.

   More than 10%: the apparent effect is plausibly due to chance.

   In between: borderline.

Reminder
--------

NHST can rule out one explanation, random sampling, but not:

* Sampling bias
* Measrement error
* Confuounding variables
* Fraud
* Honest mistakes
* etc

Summary
-------

* Effect size is important.
* SE and CI quantify error due to randomness (but not other sources of error).
* p-values indicate whether an effect might be due to chance (but that's often not the thing we should worry about).







