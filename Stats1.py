# To create ordered categories in Pandas, you can use the pd.Categorical() function on the specific dataframe column
# e.g.
#   cereal['shelf'] = pd.Categorical(cereal['shelf'], ['bottom', 'mid', 'top'], ordered=True)
#   df[column_name] = pd.Categorical(df[column_name], [order1, order2, order_n,...], ordered=True)
# categorical data has an attribute called '.cat.codes'. This is a numerical representatioin for each category. If the data is ordered, we could use this representation to find the average/median. E.g. eduction levels of participants.
# Example below of getting tree health:
# nyc_trees = pd.read_csv("./nyc_tree_census.csv")

# tree_health_statuses = nyc_trees['health'].unique()
# print(tree_health_statuses)

# health_categories = ['Poor', 'Fair', 'Good']

# nyc_trees['health'] = pd.Categorical(nyc_trees['health'], health_categories, ordered=True)

# median_health_index = np.median(nyc_trees['health'].cat.codes)
# print(median_health_index)

# median_health_status = health_categories[int(median_health_index)]

# print(median_health_status)


# .cat.codes should only be used when there is equal spacing between categories. Using it for the list ['infant', 'slighlty older infant', 'old person'] might put the median as an 'adult' when actually there are no adult participants.

# -----------------------------------------------------------------------------------------------------------------

# Sometimes we don’t want to assume that there’s equal spacing between categories. e,g, breed of a dog.
# Another way of encoding categorical variables is called One-Hot Encoding (OHE). With OHE, we essentially create a new binary variable for each of the categories within our original variable. This technique is useful when managing nominal variables because it encodes the variable without creating an order among the categories.
# We can use pd.get_dummies() to encode it this way: It takes all the different values within the chosen column and in the background creates a new column for each unique value, it then assigns a 1 to the row in the column the value corresponds to and sets a 0 for the rest of the columns of that row.
# That is why you need to redfine the whole dataframe rather than the single chosen column.
#   df = pd.get_dummies(data=df, columns=[column_name])

# -------------------------------------------------------------------------
# df['col_name'].value_counts(normalize=True, dropna=False) <--- this will provide a the % mix/proportions of the data.

# ---------------------------------------------------------------------------
# Contingency tables are the same thing as frequency tables, e.g. how many rows have certain values within 2 fields such as Gender = male or female, and employed = Yes or No
# Crosstab gives a breakdown matrix of how many observations belong to the different value combinations
# e.g.
# contingency_table = pd.crosstab(df1['field1'], df2['field2'])

# To get the proportion of each combination, we can divide the output by the size of the dataframe - it will divide all combinations by the dataframe size
# e.g.
# contingency_table_percentage = contingency_table/len(df1)


# We can get the expected frequency of each combination by firstly calculating the marginal proportions (the proportion of each field individually (added together they would make 200%))
# We then take those percentages, and multiply them against the percentage for the whole contingency table (i.e. multiply the individual field values percentages by the overall table percentages.)

# We can then multiply these final percentages by the number of rows to get a table with the number of expected observations in each combination.

# We can get the values by using the function chi2_contingency() from scipy.stats package.
# chi2_contingency() has four outputs which need to be unpacked:
# chi2, pval, dof, expected = chi2_contingency(special_authority_freq)
#   chi2 = the test statistic
#   pval = p-value of the test
#   dof = degrees of freedom
#   expected = "The expected frequencies, based on the marginal sums of the table."
# expected is the value that will give us the expected table.
# We can then compare this table to the original table from the crosstab function and see if there is a major difference (the expected table would be the scenario if there was no association between the two variables). If there is a difference, we can say that there is likely some relationship between the two variables.
# e.g. two fields: is_strong, is_fast. It is likely that those will be positively correlated for athletic people.
# We can use np.round(expected) to make the output a bit neater


# Chi squared statistic ---------------------
# we can then use the chi-aquared statistic to summarise how different the actual and expected tables are.
# As a formula ------> Chi-Squared = sum((observed - expected)^2)
# We can use the first value from the previously unpacked formula chi2 to get this number.

# "For a 2x2 table (like the one we’ve been investigating), a Chi-Square statistic larger than around 4 would strongly suggest an association between the variables. In this example, our Chi-Square statistic is much larger than that — 1307.88! This adds to our evidence that the variables are highly associated."
