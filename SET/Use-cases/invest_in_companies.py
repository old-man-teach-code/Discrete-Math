

# Nhà đầu tư muốn đầu tư vào các công ty IT, có vốn hóa nhỏ và lợi nhuận cao
# Một công ty có thể thuộc nhiều nhóm tiêu chí khác nhau (vốn hóa, lợi nhuận, ngành nghề, thi trường, ...)

# Danh sách toàn bộ các công ty
companies = ['Công ty A', 'Công ty B', 'Công ty C', 'Công ty D', 'Công ty E', 'Công ty F', 'Công ty G', 'Công ty H', 'Công ty I', 'Công ty J']

# Danh sách các công ty theo từng nhóm ngành nghề (1 công ty có thể thuộc nhiều nhóm ngành nghề)
field_groups = {
    'IT': ['Công ty A', 'Công ty B', 'Công ty C', 'Công ty D'],
    'Finance': ['Công ty E', 'Công ty F'],
    'Healthcare': ['Công ty G'],
    'Retail': ['Công ty H', 'Công ty I', 'Công ty J']
}

# Danh sách các công ty theo từng nhóm vốn hóa (1 công ty chỉ thuộc 1 nhóm vốn hóa)
market_cap_groups = {
    'Small': ['Công ty A', 'Công ty B', 'Công ty C', 'Công ty D'],
    'Medium': ['Công ty E', 'Công ty F', 'Công ty G'],
    'Large': ['Công ty H', 'Công ty I', 'Công ty J']
}

# Danh sách các công ty theo từng nhóm lợi nhuận (1 công ty chỉ thuộc 1 nhóm lợi nhuận)
profit_groups = {
    'Low': ['Công ty B', 'Công ty C'],
    'Medium': ['Công ty D', 'Công ty E', 'Công ty F'],
    'High': ['Công ty A', 'Công ty G', 'Công ty H', 'Công ty I', 'Công ty J']
}

# Danh sách các công ty theo từng nhóm thi trường (1 công ty có thể có nhiều nhóm thi trường)
market_groups = {
    'US': ['Công ty A', 'Công ty B', 'Công ty C'],
    'EU': ['Công ty C', 'Công ty D', 'Công ty E'],
    'Asia': ['Công ty A', 'Công ty G', 'Công ty C', 'Công ty H', 'Công ty I', 'Công ty J'],
    'Vietnam': ['Công ty D', 'Công ty E', 'Công ty F'],
    'Others': ['Công ty F']
}


# Tìm danh sách các công ty mà nhà đầu tư có thể đầu tư (có vốn hóa nhỏ và lợi nhuận cao, thuộc ngành IT, và có mặt ở thị trường Châu Á)
investable_companies = list(set(market_cap_groups['Small']) & set(profit_groups['High']) & set(field_groups['IT']) & set(market_groups['Asia']))

print(investable_companies)