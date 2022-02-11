import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
from scipy.stats import fisher_exact
import math

from pretty_msg import print_error, print_msg, print_warn

"""Multiple pairwise comparisons (post-hoc) with Fisher's exact test
Function is pipe() friendly

Arguments:
  contingency_table : pandas.DataFrame
  Contingency table of shape (n, 2) where n - amount of comparison groups
Returns:
  contingency_table : pandas.DataFrame
  Same as input argument
  
Prints pandas.DataFrame with matrix of p-values between the comparison groups.
Cells holding p-values <= alpha are highlighted in a different color 
"""
def pairwise_fisher(contingency_table : pd.DataFrame, alpha : float = 0.05) -> pd.DataFrame:
    p_value_matrix = np.identity(len(contingency_table.index))
    
    # Pairwise comparisons
    for i1 in range(len(contingency_table.index)):
        for i2 in range(i1 + 1, len(contingency_table.index)):
            group1 = contingency_table.index[i1]
            group2 = contingency_table.index[i2]
            odds_ratio, p_value = fisher_exact(contingency_table.loc[[group1, group2]])
            p_value_matrix[i1][i2] = p_value
            p_value_matrix[i2][i1] = p_value_matrix[i1][i2]
    # Final presentation of the p-value matrix
    p_value_matrix = pd.DataFrame(
        data = p_value_matrix,
        columns = contingency_table.index.to_list(),
        index = contingency_table.index.to_list()
    ).T.style\
        .background_gradient(cmap = "ocean", vmin = 0.0, vax = alpha)\
        .format(precision=3)
    display(p_value_matrix)
    return contingency_table

"""Multiple comparisons with Chi-square test
Function is pipe() friendly

Arguments:
  contingency_table : pandas.DataFrame
  Contingency table of shape (n, 2) where n - amount of comparison groups
Returns:
  contingency_table : pandas.DataFrame
  Same as input argument
  
Prints the result of Chi-square test for the comparison groups. If H1 is accepted, 
calls for post-hoc Fisher's exact test pairwise_fisher()
"""
def multiple_comparisons(contingency_table : pd.DataFrame, alpha : float = 0.05) -> pd.DataFrame:
    chi2, p_value, dof, ex = chi2_contingency(contingency_table)
    if p_value > alpha:
        # H0
        print_msg(f"p-value = {p_value:.3f}: Вынуждены отклонить альтернативную гипотезу и принять нулевую")
        return contingency_table 
    else:
        # H1
        # Если в множественных сравнения приняли H1, 
        # то выполняем множественные парные сравнения с целью уточнить вывод
        print_warn(f"p-value = {p_value:.3f}: Вынуждены отклонить нулевую гипотезу и принять альтернативную")
        return pairwise_fisher(contingency_table, alpha)

"""Proportions and their corresponding 95%-confidence intervals.
Formula implemented has been taken from here - https://www.biostathandbook.com/confidence.html
Function is pipe() friendly

Arguments:
  contingency_table : pandas.DataFrame
  Contingency table of shape (n, 2) where n - amount of comparison groups
Returns:
  contingency_table : pandas.DataFrame
  Same as input argument
  
Prints pandas.DataFrame with matrix of p-values between the comparison groups.
Cells holding p-values <= alpha are highlighted in a different color
"""
def prop_conf_int(df : pd.DataFrame, column_success : pd.Index, column_failures : pd.Index) -> pd.DataFrame:
    # Proportion
    n = df[column_success] + df[column_failures]
    prop = df[column_success] / n
    # 95%-confidence interval
    sp = prop * (1 - prop) / n
    sp = sp.apply(lambda x: 1.96 * math.sqrt(x))
    ci_lwr = prop - sp
    ci_upr = prop + sp
    return pd.DataFrame(
        data = {"prop" : prop, "ci_lwr" : ci_lwr, "ci_upr" : ci_upr}
    )
