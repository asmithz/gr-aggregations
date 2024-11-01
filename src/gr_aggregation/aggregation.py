from .borda_count import BordaCount


def start_borda_count(data: list, factor: int) -> dict:
    borda_instance = BordaCount(data, factor)
    return borda_instance.borda_result()
