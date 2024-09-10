import pandas as pd

x_values = [8, 10, 12]
y_values = [10, 13, 16]

df = pd.DataFrame({'x': x_values, 'y': y_values})

df['mean_x'] = df['x'].mean()
df['mean_y'] = df['y'].mean()
df['deviation_x'] = df['x'] - df['mean_x']
df['deviation_y'] = df['y'] - df['mean_y']

df['product_of_deviations'] = df['deviation_x'] * df['deviation_y']

sum_of_product_of_deviations = df['product_of_deviations'].sum()

df['square_of_deviations_x'] = df['deviation_x'] ** 2

sum_of_square_of_deviations_x = df['square_of_deviations_x'].sum()

m = sum_of_product_of_deviations / sum_of_square_of_deviations_x

c = df['mean_y'].mean() - m * df['mean_x'].mean()

print(df)
print("m (slope):", m)
print("c (intercept):", c)