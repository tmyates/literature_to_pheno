# literature_to_pheno

This repo can be used to extract Human Phenotype Ontology (HPO) terms using MetaMap from full text literature downloaded using Cadmus (https://zenodo.org/record/5618052#.YvZuGS8w2Am). Disease models consisting of HPO terms and their aggregate frequency across the input literature are generated according to entries in DDG2P (https://www.ebi.ac.uk/gene2phenotype).

The hp.obo file needs to be downloaded from https://hpo.jax.org/app/. 

A UMLS licence is required to use MetaMap (https://uts.nlm.nih.gov/uts/signup-login), and this needs to be installed locally. 

mapping_hpo requires UMLS Metathesaurus data obtainable with a licence as above. 

The ontobio package needs to be installed https://ontobio.readthedocs.io/en/latest/index.html#

The notebooks should be used sequentially on the retrieved_df2 from Cadmus. 

Notebook 4 generates comparison disease models for the same disease from multiple sources including those in http://purl.obolibrary.org/obo/hp/hpoa/phenotype_to_genes.txt. The Deciphering Developmental Disorders study (https://www.ddduk.org) data is not available publicly therefore this notebook is included as an example of methodology only. 

The mica_similarity notebook is a python implementation of the Most Informative Common Ancestor semantic similarity method as demonstrated in https://doi.org/10.1016/j.ajhg.2019.04.001. 
