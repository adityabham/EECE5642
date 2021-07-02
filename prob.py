import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

main_df = pd.read_excel('data.xlsx')

cvrp = main_df.iloc[:7, :]
neurIPS = main_df.iloc[7:14, :]
aAAI = main_df.iloc[14:21, :]
aCL = main_df.iloc[21:28, :]
sIGIR = main_df.iloc[28:35, :]

mean_data = []
main_list = [cvrp, neurIPS, aAAI, aCL, sIGIR]
for i in main_list:
    mean_i = i.mean(axis=0)
    mean_data.append(mean_i.tolist())

column_name = ['CVRP(2014-20)', 'NeurIPS(2014-20)', 'AAAI(2014-20)', 'ACL(2014-20)', 'SIGIR(2014-20)']

disp_df = pd.DataFrame(columns=column_name,
                       index=['Average Acceptance rate',
                              'Average Num. of accepted papers',
                              'Average Num. of total submissions'])

n = 0
for j in column_name:
    disp_df[j] = mean_data[n]
    n = n + 1

print("                                                           Conferences")
print("                                                           -----------")
print(disp_df)

plot_data = disp_df.values.tolist()
x = np.array(plot_data[0])
y = np.array(plot_data[1])
z = np.array(plot_data[2])

# axes = plt.subplot(111, projection='3d')
# axes.scatter(x[0], y[0], z[0], c='red', label="CVRP(2014-20)")
# axes.scatter(x[1], y[1], z[1], c='blue', label="NeurIPS(2014-20)")
# axes.scatter(x[2], y[2], z[2], c='green', label="AAAI(2014-20)")
# axes.scatter(x[3], y[3], z[3], c='orange', label="ACL(2014-20)")
# axes.scatter(x[4], y[4], z[4], c='black', label="SIGIR(2014-20)")
# axes.set_xlabel('Average Acceptance rate')
# axes.set_ylabel('Average Num. of accepted papers')
# axes.set_zlabel('Average Num. of total submissions')
# plt.legend(loc="best")
# plt.show()
