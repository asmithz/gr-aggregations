from gr_aggregation import aggregation as agg

new_data = [
    { "A": 10, "B": 4, "C": 3, "D": 6, "E": 10, "F": 9, "G": 6, "H": 8, "I": 10, "J": 8 },
    { "A": 4, "B": 9, "C": 8, "D": 9, "E": 7, "F": 9, "G": 6, "H": 9, "I": 3, "J": 8 },
    { "A": 10, "B": 5, "C": 2, "D": 7, "E": 9, "F": 7, "G": 5, "H": 6, "I": 7, "J": 6 },
    { "A": 7, "B": 6, "C": 9, "D": 8, "E": 6, "F": 6, "G": 10, "H": 9, "I": 9, "J": 9 },
]
borda_instance = agg.borda_count(new_data, 2)
print(borda_instance)