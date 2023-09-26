from borda_count import BordaCount

def borda_count(data: list, factor: int):
    new_borda = BordaCount(data, factor)
    return new_borda.borda_result()