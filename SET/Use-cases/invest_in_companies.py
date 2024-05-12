# Danh sách các công ty
companies = {
    'company1': {'industry': 'IT', 'market_cap': 100, 'profit': 10},
    'company2': {'industry': 'Finance', 'market_cap': 200, 'profit': 20},
    'company3': {'industry': 'Healthcare', 'market_cap': 150, 'profit': 15},
    'company4': {'industry': 'IT', 'market_cap': 120, 'profit': 12},
    'company5': {'industry': 'Finance', 'market_cap': 180, 'profit': 18},
    'company6': {'industry': 'Healthcare', 'market_cap': 130, 'profit': 13},
    'company7': {'industry': 'IT', 'market_cap': 140, 'profit': 14},
    'company8': {'industry': 'Finance', 'market_cap': 160, 'profit': 16},
    'company9': {'industry': 'Healthcare', 'market_cap': 110, 'profit': 11},
}

# Nhà đầu tư muốn đầu tư vào các công ty IT, có vốn hóa nhỏ và lợi nhuận cao
field_groups = {
    'IT': {'company1', 'company4', 'company7'},
    'Finance': {'company2', 'company5', 'company8'},
    'Healthcare': {'company3', 'company6', 'company9'}
}

market_cap_groups = {
    'Small': {'company1', 'company4', 'company7'},
    'Medium': {'company3', 'company6', 'company9'},
    'Large': {'company2', 'company5', 'company8'}
}

profit_groups = {
    'High': {'company1', 'company4', 'company7'},
    'Medium': {'company2', 'company5', 'company8'},
    'Low': {'company3', 'company6', 'company9'}
}

# Tìm danh sách các công ty mà nhà đầu tư có thể đầu tư
investable_companies = set(field_groups['IT']) & set(market_cap_groups['Small']) & set(profit_groups['High'])

print(f"Nhà đầu tư có thể đầu tư vào các công ty: {investable_companies}")
