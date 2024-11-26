import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('data.csv')
data_new = data.pivot_table()
#mean_med_sales_by_type = sales.pivot_table('weekly_sales',index = 'type',aggfunc=[np.mean,np.median]) columns='' fill_value=0