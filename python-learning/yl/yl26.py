revenue = {
    'Johnver': [190,325,682,829],
    'Vanston': [140,19,14,140],
    'Danbree': [1926,293,852,609],
    'Vansey': [14,1491,56,120],
    'Mundyke': [143,162,659,87]
}

expenses = {
    'Johnver': [120,300,50,67],
    'Vanston': [65,10,299,254],
    'Danbree': [890,23,1290,89],
    'Vansey': [54,802,12,129],
    'Mundyke': [430,235,145,76]
}

total_revenue = {}
for key in revenue:
    total_revenue[key] = [r-e for r, e in zip(revenue[key], expenses[key])]
    total_revenue[key] = [x if x>0 else 0 for x in total_revenue[key]]

commission = {}
for key in total_revenue:
    commission[key] = round(sum(total_revenue[key])*0.062)

for key,value in commission.items():
    print(f"{key} : {value}")
