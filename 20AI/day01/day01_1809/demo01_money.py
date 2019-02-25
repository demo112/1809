# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
money.py 金融相关API
"""
import numpy as np

# 求终值 fv(利率，期数，每期支付，现值)
# 将1000元以1%年利率存入银行5年，每年加存100元
# 到期后本息合计多少钱？
fv = np.fv(0.01, 5, -100, -1000)
print(fv)

# 求现值 np.pv(利率，期数，每期支付，终值)
# 将多少钱以1%年利率存入银行5年，每年加存100元
# 到期后本息合计1561.00
pv = np.pv(0.01, 5, -100,  1561)
print(pv)

# 每期支付 np.pmt(利率，期数，现值)
# 以1%的年利率贷款1000元，分5年还清，平均
# 每年还多少钱？
pmt = np.pmt(0.01, 5, 1000)
print(pmt)
pmt = np.pmt(0.0371 / 12, 30 * 12, 1000000)
print(pmt)

# 期数
# 以1%的年利率从银行贷款1000元，平均每年还
# 206元，多少年还清?
nper = np.nper(0.01, -206, 1000)
print(nper)
