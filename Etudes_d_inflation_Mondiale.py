import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


# Lire le fichier CSV
df = pd.read_csv(r"C:\Users\yacin\Desktop\ETudes de l'inflation Mondiale\global_inflation_data.csv")

# Afficher les dix premières lignes
df.info()
