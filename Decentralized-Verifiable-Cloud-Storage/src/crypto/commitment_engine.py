from src.utils.hash_utils import generate_hash

class CommitmentEngine:
    def __init__(self):
        # Freshness/version counter for streaming data
        self.version_counter = 0

    def create_commitment(self, data: str) -> dict:
        """
        Create commitment for incoming streaming data block.
        """
        self.version_counter += 1
        commitment_value = generate_hash(data, self.version_counter)

        return {
            "data": data,
            "counter": self.version_counter,
            "commitment": commitment_value
        }

    def verify_commitment(self, data: str, counter: int, stored_commitment: str) -> bool:
        """
        Verify integrity and freshness of retrieved data.
        """
        recalculated_hash = generate_hash(data, counter)
        return recalculated_hash == stored_commitment