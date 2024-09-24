from graphrag.vector_stores import VectorStoreFactory
from graphrag_astra.astradb import AstraDBVectorStore


def register_astradb():
    VectorStoreFactory.register("astradb", AstraDBVectorStore)


__all__ = ["register_astradb", "AstraDBVectorStore"]
