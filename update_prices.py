import pandas as pd
import json

def update_prices():
    try:
        # 读取Excel文件
        df = pd.read_excel('products.xlsx')
        
        # 转换为字典列表
        products = []
        for _, row in df.iterrows():
            product = {
                'id': str(row['id']),
                'name': str(row['name']),
                'price': float(row['price'])
            }
            products.append(product)
        
        # 生成JSON数据
        data = {'products': products}
        
        # 写入prices.json文件
        with open('prices.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print('Prices updated successfully from Excel')
    except Exception as e:
        print(f'Error updating prices: {e}')

if __name__ == '__main__':
    update_prices()
