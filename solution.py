import pandas as pd
import numpy as np
from scipy.stats import norm

chat_id = 670223087 # Ваш chat ID, не меняйте название переменной

def solution(x):
    alpha=0.06
    n = len(x)
    mu = 300
    sigma = np.std(x, ddof=1)
    se = sigma / np.sqrt(n)
    z = (np.mean(x) - mu) / se
    p_value = norm.cdf(z)
    return p_value < alpha
