# Ứng dụng sử dụng tập hợp trong bài toán đầu tư

## Mô tả bài toán
Một nhà đầu tư muốn có được danh sách các công ty mà anh ta có thể đầu tư. Các công ty được phân loại thành các nhóm khác nhau dựa trên những tiêu chí khác nhau như ngành nghề, vốn hóa, lợi nhuận, v.v. Mỗi công ty có thể thuộc nhiều nhóm khác nhau. Nhà đầu tư muốn có danh sách các công ty mà anh ta có thể đầu tư sao cho tối ưu theo một số tiêu chí nhất định.

## Cách giải quyết bài toán
Để giải quyết bài toán này, chúng ta sẽ sử dụng tập hợp để lưu trữ thông tin về các công ty và các nhóm mà chúng thuộc về. Mỗi tiêu chí đầu tư sẽ được biểu diễn bằng một tập hợp các công ty. Khi đó, việc tìm ra danh sách các công ty mà nhà đầu tư có thể đầu tư sẽ là giao của các tập hợp này.

## Triển khai sử dụng Python
Dưới đây là một ví dụ về cách triển khai giải pháp cho bài toán trên bằng Python:

```python
# Danh sách các công ty
companies = {
    'company1': {'industry': 'IT', 'market_cap': 100, 'profit': 10},
    'company2': {'industry': 'Finance', 'market_cap': 200, 'profit': 20},
    'company3': {'industry': 'Healthcare', 'market_cap': 150, 'profit': 15},
    'company4': {'industry': 'IT', 'market_cap': 120, 'profit': 12},
    'company5': {'industry': 'Finance', 'market_cap': 180, 'profit': 18},
}

# Danh sách các nhóm công ty theo ngành nghề
field_groups = {
    'IT': ['company1', 'company4'],
    'Finance': ['company2', 'company5'],
    'Healthcare': ['company3'],
}

# Danh sách các nhóm công ty theo vốn hóa
market_cap_groups = {
    'Small': ['company1', 'company4'],
    'Medium': ['company2', 'company3'],
    'Large': ['company5'],
}
# Danh sách các nhóm công ty theo lợi nhuận
profit_groups = {
    'Low': ['company1', 'company3'],
    'Medium': ['company2', 'company4'],
    'High': ['company5'],
}

# Tìm danh sách các công ty mà nhà đầu tư có thể đầu tư
investable_companies = set(field_groups['IT']) & set(market_cap_groups['Small']) & set(profit_groups['Low'])

print(investable_companies)
```



