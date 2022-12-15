---
title: 'aPhyloGeo: Multi-platform application for analyze phylogenetic trees with climatic parameters'
tags:
  - bioinformatics
  - consensus
  - least Square distance
  - multiple sequence alignment
  - phylogeny
  - phylogeography
authors:
  - name: Nadia Tahiri
    affiliation: 1
    orcid: 0000-0002-1818-208X
    corresponding: true
    email: Nadia.Tahiri@USherbrooke.ca
affiliations:
  - name: département d’Informatique, Université de Sherbrooke, 2500 Boulevard de l’Université, Sherbrooke, Québec J1K 2R1, Canada
    index: 1
date: 14 December 2022
bibliography: paper.bib

# Optional fields if submitting to a AAS journal too, see this blog post:
# https://blog.joss.theoj.org/2018/12/a-new-collaboration-with-aas-publishing
aas-doi: 10.3847/xxxxx <- update this with the DOI from AAS once you know it.
aas-journal: Astrophysical Journal <- The name of the AAS journal.
---

# Summary

A cross-platform application for phylogenetic tree analysis with climate parameters (`aPhyloGeo`) is a pipeline for performing phylogenetic analyses from genetic and climate data. The pipeline provides a suite of analyses adapted to different scenarios, designed to allow the analysis of data sets represented by three different levels: 1) genetic, 2) climatic, and 3) biogeography correlation, all in one package. These levels of similarity (assessed by least squares distance) influence the assumptions used to consider a correlation between the genetics of a species and its habitat during the reconstruction of the multiple alignment required for phylogenetic inference. By selecting an appropriate gene list for the available data defined on a set of species to explain the adaptation of the species according to the Darwinian hypothesis, the user can be confident that these assumptions are taken into account in `aPhyloGeo`.

# Statement of need

Climate change and other anthropogenic variables have a major impact on biodiversity and population dynamics. In order to better explain the mechanisms underlying these perturbed ecosystem states, biologists have used phylogeographic approaches. These approaches attempt to determine the relationship between the genetic structure of the populations studied and their geographical distribution by considering their present or past geoclimatic history.

In this study, we are particularly interested in the development of bioinformatics tools for the phylogeographic analysis of viruses [1] and endemic or invasive species. Knowing the urgency of the current climate situation (COP27 - Climate Change and COP15 - Convention on Biological Diversity) and expected in the future, it is therefore essential to develop tools respecting bioinformatics software development standards in order to characterize genetic diversity and phenotypic traits according to environmental conditions.

# State of the field

# Pipeline

![The workflow of the algorithm. The operations within this workflow include several blocks.](../img/Fig_1.png)

The blocks are highlighted by three different colors.

* The first block (the light blue color) is responsible for creating the trees based on the climate data - performs the function of input parameter validation (see YAML file).
* The second block (the dark yellow color) is responsible for creating the trees based on the genetic data - performs the function of input parameter validation (see YAML file).
* The third block (the light green color) allows the comparaison between the phylogenetic trees (i.e., with genetic data) and the climatic trees - denoted phylogeography step.

This is the most important block and the basis of this study, through the results of which the user receives the output data with the necessary calculations.

Moreover, our approach is optimal since it is elastic and adapts to any computer by using parallelism and available GPUs/CPUs according to the resource usage per unit of computation (i.e., to realize the processing of a single genetic window - see the worflow below).
**Multiprocessing**: Allows multiple windows to be analyzed simultaneously (recommended for large datasets)

In this work, we applied software packages of the following versions: [Biopython](https://biopython.org/) version 1.79 (BSD 3-Clause License).



Single dollars ($) are required for inline mathematics e.g. $f(x) = e^{\pi/x}$

Double dollars make self-standing equations:

$$\Theta(x) = \left\{\begin{array}{l}
0\textrm{ if } x < 0\cr
1\textrm{ else}
\end{array}\right.$$

You can also use plain \LaTeX for equations
\begin{equation}\label{eq:fourier}
\hat f(\omega) = \int_{-\infty}^{\infty} f(x) e^{i\omega x} dx
\end{equation}
and refer to \autoref{eq:fourier} from text.



# Conclusion
The ALPPACA pipeline provides a suite of phylogenetic analyses for different scenarios, all in one package. This enables a variety of uses without having to download several tools and programs, and the Nextflow framework allows for user-friendly and reproducible use of the pipeline. Additional tracks may be added to ALPPACA in the future, such as clustering based on core/whole genome multi locus sequence typing, or additions to existing tracks, such as recombination detection in the core gene analysis. Clustering analysis using FastANI (https://github.com/ParBLiSS/FastANI) will be added as a separate track, to assist users in selecting the correct track by evaluating genetic diversity in their dataset.

# Acknowledgements

This work was supported by the Natural Sciences and Engineering Research Council of Canada, the University of Sherbrooke grant, and the Centre de recherche en écologie de l'UdeS (CREUS). The author would like to thank the Department of Computer Science, University of Sherbrooke, Quebec, Canada for providing the necessary resources to conduct this research. The computations were performed on resources provided by Compute Canada and Compute Quebec - the National and Provincial Infrastructure for High Performance Computing and Data Storage. The author would like to thank the students of the Université du Québec à Montréal for their great contribution to the development of the software.

# References
