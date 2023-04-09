import pandas as pd
import numpy as np

from scipy.stats import ttest_1samp

chat_id = 670223087 # Ваш chat ID, не меняйте название переменной

def solution(x) -> bool:
    alpha = 0.06 # уровень значимости критерия
    threshold = 300 # пороговое значение затрат
    t_statistic, p_value = ttest_1samp(x, threshold)
    reject_null = p_value/2 < alpha and t_statistic < 0
    return reject_null[0]
