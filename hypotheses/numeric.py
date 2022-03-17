def cohen_d(x1 : pd.Series, x2 : pd.Series):
    """Effect size by Cohen's d

    Args:
        x1 (pd.Series): sample 1
        x2 (pd.Series): sample 2

    Returns:
        d (float): Cohen's d
        effect (str): Effect size interpretation as presented in DOI: 10.22237/jmasm/1257035100 
    """
    n1 = x1.shape[0]
    n2 = x2.shape[0]
    s1 = x1.std()
    s2 = x2.std()
    s = np.sqrt(((n1 - 1) * s1**2 + (n2 - 1) * s2 ** 2) / (n1 + n2 - 2))
    d = (x1.mean() - x2.mean()) / s
    if d < 0.01:
        effect = "no effect"
    elif 0.01 < d < 0.2:
        effect = "very small"
    elif 0.2 < d < 0.5:
        effect = "small"
    elif 0.5 < d < 0.8:
        effect = "medium"
    elif 0.8 < d < 1.2:
        effect = "large"
    elif 1.2 < d < 2.0:
        effect = "very large"
    else:
        effect = "huge"
    
    return d, effect

def cohen_d_to_shift_of_means(d : float, x1 : pd.Series, x2 : pd.Series):
    """Convert Cohen's d effect size to the shift of means of the samples

    Args:
        d (float): Cohen's d
        x1 (pd.Series): sample 1
        x2 (pd.Series): sample 2
    """
    n1 = x1.shape[0]
    n2 = x2.shape[0]
    s1 = x1.std()
    s2 = x2.std()
    s = np.sqrt(((n1 - 1) * s1**2 + (n2 - 1) * s2 ** 2) / (n1 + n2 - 2))
    delta = d * s
    return delta
