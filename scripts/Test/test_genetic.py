from Alignement import AlignSequences
import aPhyloGeo
from Bio import AlignIO
from io import StringIO
# from Bio import Phylo
# from Bio.Phylo.PhyloXML import Phylogeny
import os
from Params import Params
from pathlib import Path
# import pytest

current_file = os.path.dirname(__file__)

# @pytest.fixture(scope="module")
# def climaticTreesSetup():
#     return aPhyloGeo.climaticPipeline(_params)

# @pytest.fixture
# def alignementSetup()->list:
#     '''
#     This fixture will be used to create the diffrent alignement objects

#     Returns:
#         list: list of alignement objects
#     '''
#     small = AlignSequences(Params(os.path.join(os.path.dirname(__file__), "params_small.yaml")))
#     very_small = AlignSequences(Params(os.path.join(os.path.dirname(__file__), "params_very_small.yaml")))
#     return [very_small, small]

# @pytest.mark.usefixtures('climaticTreesSetup')
# class TestGenetic:

#     def test_genetic_createBootStrap(self):
#         assert True

#     def test_genetic_filterResults(self):
#         assert True


class TestGenetic():

    def setup_class(self):
        '''
        This fixture will be used to create the diffrent alignement objects

        Returns:
            list: list of alignement objects
        '''
        print("Begin setup for test class test_genetic...")

        params_small = Params(os.path.join(os.path.dirname(__file__), "params_small.yaml"))
        params_very_small = Params(os.path.join(os.path.dirname(__file__), "params_very_small.yaml"))
        small = AlignSequences(params_small)
        very_small = AlignSequences(params_very_small)

        self.alignementSetup = [very_small, small]
        self.paramSetup = [params_very_small, params_small]

    def test_centroidKey(self):

        print("Begin test_centroidKey...")
    
        for alignement in self.alignementSetup:
            
            test_case = alignement.p.reference_gene_filename[0:-6]
            centroid = alignement.centroidKey
            filename = Path(current_file + "/TestFiles/GetSequenceCentroid/" + test_case)

            with open(filename, 'r') as f:
                centroid_file = f.read()
                assert centroid == centroid_file

    def test_aligned(self):

        print("Begin test_aligned...")
    
        for alignement in self.alignementSetup:
            
            test_case = alignement.p.reference_gene_filename[0:-6]
            aligned = alignement.aligned

            for key in aligned.keys():
                expected = AlignSequences.fileToDict(current_file + "/TestFiles/AlignSequence/" + test_case + "/" + key, '.fasta')
                assert aligned[key] == expected

    def test_heuristicMSA(self):

        print("Begin test_heuristicMSA...")
    
        for alignement in self.alignementSetup:
            
            test_case = alignement.p.reference_gene_filename[0:-6]
            starAlignement = alignement.heuristicMSA            
            expected = AlignSequences.fileToDict(current_file + "/TestFiles/StarAlignement/" + test_case, '.fasta')
            assert starAlignement == expected

    def test_windowed(self):

        print("Begin test_windowed...")

        for alignement in self.alignementSetup:
            
            test_case = alignement.p.reference_gene_filename[0:-6]
            windowed = alignement.windowed

            for key in windowed.keys():
                expected = AlignSequences.fileToDict(current_file + "/TestFiles/SlidingWindow/" + test_case + "/" + key, '.fasta')
                assert windowed[key] == expected

    def test_msaSet(self):

        print("Begin test_msaSet...")

        for alignement in self.alignementSetup:
            
            test_case = alignement.p.reference_gene_filename[0:-6]
            msa = alignement.msaSet
            
            for key in msa.keys():
                filename = Path(current_file + "/TestFiles/MakeMSA/" + test_case + "/" + (key + ".fasta"))
                f = open(filename, "r")
                data = ""
                noOfLines = 0
                for line in f:
                    data += line
                    noOfLines += 1
                f.close()
                expected = str(AlignIO.read(StringIO(data), "fasta"))
                actual = str(msa[key])

                # for all the lines in expected
                for i in range(noOfLines):
                    if expected[i] not in actual:
                        assert False

    # def test_createBootStrap(self):
    #     for alignement, params in zip(self.alignementSetup, self.paramSetup)):

    #         test_case = alignement.p.reference_gene_filename[0:-6]

    #         trees = aPhyloGeo.createBoostrap(alignement.msaSet, params)
    #         # open the file
    #         expected = Phylo.parse(current_file + "\\TestFiles\\CreateBootstrap\\" + test_case + ".xml", "phyloxml")
    #         actual = [str(Phylogeny.from_tree(tree)) for tree in list(trees.values())]
    #         for tree in actual:
    #             print(tree)
            
    #         for tree in expected:
    #             print(str(tree))
    #             if str(tree) not in actual:
    #                 assert False

    def test_filterResults(self):

        print("Begin test_filterResults...")

        for alignement in self.alignementSetup:
            test_case = alignement.p.reference_gene_filename[0:-6]

            assert True
    
    def test_createGeneticList(self):

        print("Begin test_createClimaticList...")
        
        for alignement in self.alignementSetup:
            test_case = alignement.p.reference_gene_filename[0:-6]

            assert True
    
    def test_writeOutputFile(self):

        print("Begin test_writeOutputFile...")

        for alignement in self.alignementSetup:
            test_case = alignement.p.reference_gene_filename[0:-6]

            assert True
