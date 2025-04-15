import pandas as pd

# Let's say your DataFrames are df1 and df2

# 1. Create a combined key for each DataFrame
df1['combined'] = df1['x'].astype(str) + '_' + df1['y'].astype(str)
df2['combined'] = df2['x'].astype(str) + '_' + df2['y'].astype(str)

# 2. Find the unique combinations in each DataFrame
unique_df1 = pd.DataFrame(df1['combined'].unique(), columns=['combined'])
unique_df2 = pd.DataFrame(df2['combined'].unique(), columns=['combined'])

# 3. Identify the combinations that are in one but not the other
merged_df = pd.merge(unique_df1, unique_df2, on='combined', how='outer', indicator=True)
non_matching_combinations = merged_df[merged_df['_merge'] != 'both']

# 4. Separate the 'x' and 'y' values from the combined key
non_matching_combinations[['x', 'y']] = non_matching_combinations['combined'].str.split('_', expand=True)

# 5. The result is a DataFrame containing the unique 'x' and 'y' combinations
result_df = non_matching_combinations[['x', 'y']].reset_index(drop=True)

print(result_df)
