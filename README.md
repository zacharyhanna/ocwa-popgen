# ocwa-popgen

## Structure analyses  
**Tools**  
* Structure version 2.3.4 (Pritchard, Stephens & Donnelly, 2000; Falush, Stephens & Pritchard, 2003; Hubisz et al., 2009; Pritchard, Falush, Hubisz, 2012)  
* Structure Harvester version 0.6.94 (Earl & vonHoldt, 2012; Earl, 2014)  
CLUMPP version 1.1.2 (Jakobsson & Rosenberg, 2007; Jakobsson & Rosenberg, 2009)  
* StrAuto version 1.0  (Chhatre & Emerson, 2017; Chhatre & Emerson, 2018)  
* Distruct version 2.2 (Raj et al., 2014; Chhatre, 2016)  

### Program set-up  

* Obtained and unpacked Structure  
```
wget https://web.stanford.edu/group/pritchardlab/structure_software/release_versions/v2.3.4/release/structure_linux_console.tar.gz  
tar xvfz structure_linux_console.tar.gz  
```

* Obtained Structure Harvester  
```
git clone https://github.com/dentearl/structureHarvester.git  
```

* Obtained and unpacked StrAuto   
```
wget http://www.crypticlineage.net/download/strauto/strauto_1.tar.gz  
tar xvfz strauto_1.tar.gz  
```

* Obtained and unpacked CLUMPP
```
wget https://rosenberglab.stanford.edu/software/CLUMPP_Linux64.1.1.2.tar.gz  
tar xvfz CLUMPP_Linux64.1.1.2.tar.gz  
```

* Obtained and unpacked Distruct  
```
wget http://www.crypticlineage.net/download/distruct/distruct22.tar.gz  
tar xvfz distruct22.tar.gz  
```
We made a few slight modifications to the distruct2.2.py script for our plots. We have provided our modified version of the script in this repository as "distruct2.2_ocwa.py".  

### 8pop analyses  
We first ran analyzed our dataset with eight designated populations.  

#### 8pop StrAuto run  
We ran StrAuto using the LOCPRIOR with eight designated populations (see input files in the 8pop_StrAuto directory) for K=1-20.  
```
python strauto.1.py  
```
We changed the extraparams file created by the above command to enable the LOCPRIOR ("#define LOCPRIOR 1").  
```
./runstructure  
```
#### 8pop CLUMPP run  
The Structure Harvester output suggested K=2 as optimal, so we ran CLUMPP on the K=2 output (see input files in the 8pop_clumpp directory).  
```
CLUMPP paramfile_K2individ
```

#### 8pop create Distruct plot  
```
$ python distruct2.2_ocwa.py --input=StrAuto8pop -K 2 --output=StrAuto8pop_distruct2.2.png --popfile=OCWA_8pop_justPopFlags_names --poporder=OCWA_8pop_order_names  
```

### 7pop analyses  
Based upon the 8pop analyses, we removed the Channel Islands population and separately analyzed the remaining seven populations in our dataset.  

#### 7pop StrAuto run  
We ran StrAuto using the LOCPRIOR with seven designated populations (see input files in the 7pop_StrAuto directory) for K=1-20.  
```
python strauto.1.py  
```
We changed the extraparams file created by the above command to enable the LOCPRIOR ("#define LOCPRIOR 1").  
```
./runstructure  
```
#### 7pop CLUMPP run  
The Structure Harvester output suggested K=2 as potentially optimal, so we ran CLUMPP on the K=2 output (see input files in the 7pop_clumpp directory).  
```
CLUMPP paramfile_K2individ
```

#### 7pop create Distruct plot  
```
$ python distruct2.2_ocwa.py --input=StrAuto7pop -K 2 --output=StrAuto7pop_distruct2.2.png --popfile=OCWA_7pop_justPopFlags_names --poporder=OCWA_7pop_order_names  
```

### 2pop analyses  
Based upon the 8pop analyses, we separately analyzed the Channel Islands population for substructure. We designated the individuals from the northern and southern Channel Islands as separate populations.  

#### 2pop StrAuto run  
We ran StrAuto using the LOCPRIOR with two designated populations (see input files in the 2pop_StrAuto directory) for K=1-10.  
```
python strauto.1.py  
```
We changed the extraparams file created by the above command to enable the LOCPRIOR ("#define LOCPRIOR 1").  
```
./runstructure  
```
#### 2pop CLUMPP run  
The Structure Harvester output suggested K=4 as potentially optimal, so we ran CLUMPP on the K=4 output (see input files in the 7pop_clumpp directory).  
```
CLUMPP paramfile_K4individ
```

#### 2pop create Distruct plot  
```
$ python distruct2.2_ocwa.py --input=StrAuto2pop -K 2 --output=StrAuto2pop_distruct2.2.png --popfile=OCWA_2pop_justPopFlags_names --poporder=OCWA_2pop_order_names  
```

## IMa2 analyses

We ran IMa2p version 58a02604e58b6a2bc3c1ccbb75767dafbb6fa781 (Sethuraman & Hey 2015; Sethuraman, 2017) three separate times with these settings.  
```
mpirun -np 10 IMa2p -hn 15 -q1183.5505060899999 -m6.7593228669463 -t23.6710101218 -
b1000000 -r2 -r5 -l20000 -p6 -u1 -hfg -ha0.999 -hb0.3 -i IMa2_input -o run_out  
```

## Citing the repository

Please cite this repository as follows (you should also add which version you used):  

<a href="https://orcid.org/0000-0002-0210-7261" target="orcid.widget" rel="noopener noreferrer" style="vertical-align:top;"><img src="https://orcid.org/sites/default/files/images/orcid_16x16.png" style="width:1em;margin-right:.5em;" alt="ORCID iD icon">Hanna ZR</a>, Henderson JB, Wall JD. 2017. SPOW-BDOW-introgression-scripts. *Zenodo*. [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1065056.svg)](https://doi.org/10.5281/zenodo.1065056)


[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1648691.svg)](https://doi.org/10.5281/zenodo.1648691)

## References  
Chhatre VE. 2016. Distruct. Version 2.2. [Accessed 2018 Jun 21]. Available from: http://www.crypticlineage.net/pages/distruct.html  

Chhatre VE., Emerson KJ. 2017. StrAuto: automation and parallelization of STRUCTURE analysis. *BMC Bioinformatics* 18:192. DOI: 10.1186/s12859-017-1593-0.  

Chhatre VE., Emerson KJ. 2018. StrAuto. Version 1.0. [Accessed 2018 Jun 21]. Available from: http://www.crypticlineage.net/pages/software.html  

Earl DA., vonHoldt BM. 2012. STRUCTURE HARVESTER: a website and program for visualizing STRUCTURE output and implementing the Evanno method. *Conservation Genetics Resources* 4:359–361. DOI: 10.1007/s12686-011-9548-7.  

Earl D. 2014. Structure Harvester. 2014. Structure Harvester. Version 0.6.94. [Accessed 2018 Jun 21]. Available from: https://github.com/dentearl/structureHarvester  

Falush D., Stephens M., Pritchard JK. 2003. Inference of Population Structure Using Multilocus Genotype Data: Linked Loci and Correlated Allele Frequencies. *Genetics* 164:1567–1587.  

Hubisz MJ., Falush D., Stephens M., Pritchard JK. 2009. Inferring weak population structure with the assistance of sample group information. *Molecular Ecology Resources* 9:1322–1332. DOI: 10.1111/j.1755-0998.2009.02591.x.  

Jakobsson M., Rosenberg NA. 2007. CLUMPP: a cluster matching and permutation program for dealing with label switching and multimodality in analysis of population structure. *Bioinformatics* 23:1801–1806. DOI: 10.1093/bioinformatics/btm233.  

Jakobsson M., Rosenberg NA. 2009. CLUMPP: CLUster Matching and Permutation Program. Version 1.1.2. [Accessed 2018 Jun 21]. Available from: https://rosenberglab.stanford.edu/clumpp.html  

Pritchard JK., Stephens M., Donnelly P. 2000. Inference of Population Structure Using Multilocus Genotype Data. *Genetics* 155:945–959.  

Pritchard JK., Falush D., Hubisz MJ. 2012. Structure. Version 2.3.4. [Accessed 2018 Jun 21]. Available from: https://web.stanford.edu/group/pritchardlab/structure.html  

Raj A., Stephens M., Pritchard JK. 2014. fastSTRUCTURE: Variational Inference of Population Structure in Large SNP Data Sets. *Genetics* 197:573–589. DOI: 10.1534/genetics.114.164350.  

Sethuraman A, Hey J. 2015. IMa2p – parallel MCMC and inference of ancient demography under the Isolation with migration (IM) model. *Molecular Ecology Resources* 16:206–215. DOI: 10.1111/1755-0998.12437.  

Sethuraman A. 2017. IMa2p. Version 58a02604e58b6a2b. [Accessed 2018 Jun 21]. Available from: https://github.com/arunsethuraman/ima2p
