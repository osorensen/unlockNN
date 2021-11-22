"""Benchmarking script for the matbench phonons dataset."""
from ..matbench import MatbenchTrainer

if __name__ == "__main__":
    trainer = MatbenchTrainer(
        "matbench_phonons",
        "https://ml.materialsproject.org/projects/matbench_phonons.json.gz",
        "last phdos peak",
    )
    trainer.execute()
