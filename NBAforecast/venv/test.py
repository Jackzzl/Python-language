import pandas as pd
import math
import csv
import random
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import cross_val_score

#设置elo等级
base_elo =1600
team_elos = {}
team_stats = {}
x = []
y = []
folder ='data'#存放数据的目录

def initialize_data(Mstat,Ostat,Tstat):
    new_Mstat=Mstat.drop(['Rk','Arena'], axis=1)
    new_Ostat=Ostat.drop(['Rk','G','MP'],axis=1)
    new_Tstat=Tstat.drop(['Rk','G','MP'],axis=1)

    team