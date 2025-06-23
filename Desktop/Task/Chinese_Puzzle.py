heads = 35
legs = 94

for chickens in range(heads + 1):
    rabbits = heads - chickens
    total_legs = chickens * 2 + rabbits * 4
    if total_legs == legs:
        print(f"Chickens: {chickens}, Rabbits: {rabbits}")
        break
