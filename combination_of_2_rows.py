import pandas as pd

def get_new_combinations(df1: pd.DataFrame, df2: pd.DataFrame, col1: str, col2: str) -> pd.DataFrame:
    """
    Returns a DataFrame containing rows from df1 where the (col1, col2) combination 
    does not exist in df2.

    Parameters:
    - df1 (pd.DataFrame): First DataFrame to compare (source of new rows).
    - df2 (pd.DataFrame): Second DataFrame to check against.
    - col1 (str): First column name to compare.
    - col2 (str): Second column name to compare.

    Returns:
    - pd.DataFrame: Filtered DataFrame with only new combinations.
    """
    # Create sets of tuples for the combinations
    combos_df1 = set(zip(df1[col1], df1[col2]))
    combos_df2 = set(zip(df2[col1], df2[col2]))
    
    # Get new combinations
    new_combos = combos_df1 - combos_df2
    
    # Filter df1 for only those new combinations
    result_df = df1[df1[[col1, col2]].apply(tuple, axis=1).isin(new_combos)]
    
    return result_df
