# Example data

This data is included as a convenience for testing unlockNN and demonstrating
its usage with more minimalist examples. It can be loaded using
`unlocknn.download.load_data(fname)`, where `fname` is the name of the data
file _without the file extension_.

Currently, the only included data is `binary_e_form.parquet`, which includes
binary compounds that lie on the convex hull and their formation
energies in eV, from the [Materials Project](https://materialsproject.org/).
