import pandas as pd
import matplotlib.pyplot as plt


tabela = pd.DataFrame({
    'idade': [20, 23, 45, 31, 32],
    'nome': ['joao', 'maria', 'jose', 'sofia', 'helena']
})

plt.hist(tabela['idade'])