# -Cryo-ET-Tomography--MBZUAI

This code is designed to simulate cryo-electron tomography (cryo-ET) data from a protein structure file (PDB file). Here's a breakdown of how it works and what each part does:

1. Converting PDB to Density Map (pdb2density):
Purpose: The pdb2density function converts a PDB file (which contains atomic coordinates of a molecule) into a 3D electron density map.
Steps:
The PDB file is parsed to extract atomic coordinates.
These coordinates are mapped onto a 3D grid, where each atom contributes to the electron density at its grid position.
The density map is saved in the MRC file format, which is commonly used for storing 3D electron density maps.
2. Simulating Tomograms:
Generate Tomogram (generate_tomogram):

Purpose: To generate 2D projections of the 3D density map at different tilt angles, simulating the tomogram.
Steps:
The 3D density map is rotated according to specified tilt angles.
A projection is generated using the weak_projection_theorem (placeholder for a physical simulation).
The projection is processed to simulate electron interactions and the application of a Contrast Transfer Function (CTF).
Noise Addition (add_noise):

Purpose: Placeholder function intended to add noise to the simulated tomograms, though it’s not implemented in the current code.
3. Reconstructing and Visualizing the Tomogram:
Reconstruct Tomogram (reconstruct_tomogram):
Purpose: Placeholder function for reconstructing the tomogram from 2D projections. It currently returns the input tomogram as-is.
Visualize Tomogram (visualize_tomogram):
Purpose: Displays slices of the reconstructed tomogram using Matplotlib.
Steps:
Extracts slices from the 3D tomogram and displays them as 2D images.
4. Simulating Cryo-ET (simulate_cryo_et):
Purpose: This is the main function that ties everything together, simulating a series of cryo-ET tomograms from a PDB file.
Steps:
Calls pdb2density to create the 3D density map.
Generates multiple tomograms by varying tilt angles.
Removes the temporary density map file.
Returns the simulated tomograms.
What the Code Achieves:
The code takes a molecular structure (PDB file) and simulates the process of cryo-electron tomography, creating a set of 2D projections that mimic what might be observed in an actual cryo-ET experiment.
These projections can be reconstructed into a 3D tomogram, and the slices of this tomogram can be visualized.
