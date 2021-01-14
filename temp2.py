n, quantity = map(int, input().split())
cost = []
for e in range(n):
	cost.append(float(input()))
	
min_cost = min(cost)
from decimal import Decimal
while(1):
    cut = int()
    for c in cost:
        cut += int(c/min_cost)
    if cut == quantity:
        break
    else:
        # min_cost = min_cost - 0.01
        min_cost = float(Decimal(min_cost) - Decimal(0.01))
print(round(Decimal(min_cost)+Decimal(0.01),2))
	