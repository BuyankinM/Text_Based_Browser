iris = {}


def add_iris(id_n: int,
             species: str,
             petal_length: float,
             petal_width: float,
             **kwargs):

    iris[id_n] = {"species": species,
                  "petal_length": petal_length,
                  "petal_width": petal_width,
                  **kwargs}
