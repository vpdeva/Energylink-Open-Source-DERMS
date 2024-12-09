
def register_dataset(dataset_name, metadata):
    """Register a dataset with metadata in the data mesh."""
    return {"dataset_name": dataset_name, "metadata": metadata}

def track_lineage(source, destination, transformations):
    """Track data lineage across transformations."""
    return {"source": source, "destination": destination, "transformations": transformations}
            