import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest


chat_id = 464814509 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    count = np.array([x_success, y_success])
    nobs = np.array([x_cnt, y_cnt])
    stat, pval = proportions_ztest(count, nobs, alternative='two-sided')
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return pval < 0.08
