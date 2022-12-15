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

A cross-platform application for phylogenetic tree analysis with climate parameters (`aPhyloGeo`) is a pipeline for performing phylogenetic analyses from genetic and climate data. The pipeline provides a suite of analyses adapted to different scenarios, designed to allow the analysis of data sets represented by three different levels: 1) genetic, 2) climatic, and 3) biogeography correlation, all in one package. These levels of similarity (assessed by least squares distance in \autoref{eq:ls}) influence the assumptions used to consider a correlation between the genetics of a species and its habitat during the reconstruction of the multiple alignment required for phylogenetic inference. By selecting an appropriate gene list for the available data defined on a set of species to explain the adaptation of the species according to the Darwinian hypothesis, the user can be confident that these assumptions are taken into account in `aPhyloGeo`.

# Statement of need

Climate change and other anthropogenic variables have a major impact on biodiversity and population dynamics. In order to better explain the mechanisms underlying these perturbed ecosystem states, biologists have used phylogeographic approaches. These approaches attempt to determine the relationship between the genetic structure of the populations studied and their geographical distribution by considering their present or past geoclimatic history.

In this study, we are particularly interested in the development of bioinformatics tools for the phylogeographic analysis of viruses [@nadia_tahiri-proc-scipy-2022] and endemic or invasive species. Knowing the urgency of the current climate situation (COP27 - Climate Change and COP15 - Convention on Biological Diversity) and expected in the future, it is therefore essential to develop tools respecting bioinformatics software development standards in order to characterize genetic diversity and phenotypic traits according to environmental conditions.

# State of the field

# Pipeline

The `aPhyloGeo` pipeline is written in python3.9, and the code and documentation are publicly available on GitHub  (https://github.com/tahiri-lab/aPhyloGeo). The user has the option of running the pipeline using different cparameterss, such as docker, bootstrap threshold, or least square distance threshold. 

![The workflow of the algorithm. The operations within this workflow include several blocks.](../img/Fig_1.png)

The blocks are highlighted by three different colors.

* The first block (the light blue color) is responsible for creating the trees based on the climate data - performs the function of input parameter validation (see YAML file) and using Neighbor-joining algorithm (see [@gascuel2006neighbor]).
* The second block (the dark yellow color) is responsible for creating the trees based on the genetic data - performs the function of input parameter validation (see YAML file).
* The third block (the light green color) allows the comparaison between the phylogenetic trees (i.e., with genetic data) and the climatic trees - denoted phylogeography step using Least Square distance (see \autoref{eq:ls} and [@felsenstein1997alternating]).

\begin{equation}\label{eq:ls}
ls(T_1, T_2) = \sum_{1 \le i \le j \le n} \lvert \delta(i,j) - \xi(i,j) \rvert
\end{equation}
where $T_1$ is the phylogenetic tree 1, $T_2$ is the phylogenetic tree 2, $i$ and $j$ are two species, $\delta(i,j)$ is the distance between specie $i$ and specie $j$ in $T_1$, $\xi(i,j)$ is the distance between specie $i$ and specie $j$ in $T_2$, and $n$ is the total number of species.

This is the most important block and the basis of this study, through the results of which the user receives the output data with the necessary calculations.

Moreover, our approach is optimal since it is elastic and adapts to any computer by using parallelism and available GPUs/CPUs according to the resource usage per unit of computation (i.e., to realize the processing of a single genetic window - see the worflow below).
**Multiprocessing**: Allows multiple windows to be analyzed simultaneously (recommended for large datasets)

In this work, we applied software packages of the following versions: [Biopython](https://biopython.org/) version 1.79 (BSD 3-Clause License), [Bio](https://pandas.pydata.org/) version 1.5.2 (New BSD License), and [numpy](https://numpy.org/) version 1.21.6 (BSD 3-Clause License).

# Conclusion
The `aPhyloGeo` pipeline provides a suite of phylogeographic analyses for different datasets (genetic and climatic), all in one package. This allows for a variety of uses without having to download multiple tools and programs, making the pipeline easy to use and reproducible. Additional avenues may be added to `aPhyloGeo` in the future, such as integration of the Nextflow framework, clustering based on multiple sequence alignments similarity, an efficient alignment method, and new metrics (e.g., Robinson and Foulds distance, Quartet metric, and bipartition) will be added as potential choices, to help users select the best choice for their data by evaluating the genetic diversity in their dataset.

# Acknowledgements

This work was supported by the Natural Sciences and Engineering Research Council of Canada, the University of Sherbrooke grant, and the Centre de recherche en écologie de l'UdeS (CREUS). The author would like to thank the Department of Computer Science, University of Sherbrooke, Quebec, Canada for providing the necessary resources to conduct this research. The computations were performed on resources provided by Compute Canada and Compute Quebec - the National and Provincial Infrastructure for High Performance Computing and Data Storage. The author would like to thank the students of the Université du Québec à Montréal for their great contribution to the development of the software.

# References
