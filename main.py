

# Create an instance of the VectorDatabase
vector_db = VectorDatabase()

# Insert vectors into the database
vector_db.insert("vector_1", np.array([0.1, 0.2, 0.3]))
vector_db.insert("vector_2", np.array([0.4, 0.5, 0.6]))
vector_db.insert("vector_3", np.array([0.7, 0.8, 0.9]))

# Search for similar vectors
query_vector = np.array([0.15, 0.25, 0.35])
similar_vectors = vector_db.search(query_vector, k=2)
print("Similar vectors:", similar_vectors)

# Retrieve a specific vector by its key
retrieved_vector = vector_db.retrieve("vector_1")
print("Retrieved vector:", retrieved_vector)