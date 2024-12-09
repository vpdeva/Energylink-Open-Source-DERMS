
def track_data_lineage(source, transformations, destination):
    """Track the data lineage from source to destination.""" 
    lineage = {
        "source": source,
        "transformations": transformations,
        "destination": destination
    }
    return lineage
            