import os
import pandas as pd
if __name__ == "__main__":
    # 在当前目录创建data文件夹
    os.makedirs('data', exist_ok=True)
    # 在data文件夹中创建CSV文件
    data_file = os.path.join('data', 'house_tiny.csv')
    print(f'拼接结果: {data_file}')

    with open(data_file, 'w') as f:
        f.write('NumRooms,Alley,Price\n')  # 列名
        f.write('NA,Pave,127500\n')  # 每行表示一个数据样本
        f.write('2,NA,106000\n')
        f.write('4,NA,178100\n')
        f.write('NA,NA,140000\n')

    data = pd.read_csv(data_file)
    print(data)


    inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2]
    # 显式指定 numeric_only=True 参数，确保只对数值列计算均值
    inputs = inputs.fillna(inputs.mean(numeric_only=True))  # 用各列的平均值填充对应列中的空值
    print(f'mean之后的数据{inputs}')
