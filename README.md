# Assignment
data engineer Assignment

Required packages:
pip install pandas
pip install matplotlib
import pyplot

PROCESS:

1. created dataframe using pandas and imported csv file into the dataframe.
2. listed products without prices using isna() function to show all nan values in the column.
3. to show the count of products with and without prices sum() function is used.
4. to correct the format of price_string column:
   a.first removed all the dollar symbols from column(if added without removing it displayed double dollar symbols)
   b.then added dollar symbols to column once again
   c.then separted the price_string column into currency and values using series.split() function
5.created new dataframe for category and values and then changing the datatype of values column from object to float using .astype() function
  then performed grouping on category column using .groupby() function ,follwed by mean on values column using .mean() function
6. to plot graph .bar() is used to plot bar plot of the above data.
