##### -----------------------------------------------------------------------------------
#####
#####    input.py Template for strAuto Python Script (v. 1.0)
#####    Copyright (C) 2016 by Vikram Chhatre and Kevin Emerson
#####
#####    This program is free software: you can redistribute it and/or modify
#####    it under the terms of the GNU General Public License as published by
#####    the Free Software Foundation, either version 3 of the License, or
#####    (at your option) any later version.
#####
#####    This program is distributed in the hope that it will be useful,
#####    but WITHOUT ANY WARRANTY; without even the implied warranty of
#####    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#####    GNU General Public License for more details.
#####
#####    You should have received a copy of the GNU General Public License
#####    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#####
##### -----------------------------------------------------------------------------------
#####                        INSTRUCTIONS FOR USE
#####
#####    Please fill out following information.
#####    Do not make any changes to the information already existent in this file.
#####    Simply add information about your data set and the analysis.
#####
##### -----------------------------------------------------------------------------------

##########                         ##########
##########  Questions begin below  ##########
##########                         ##########

## 1. How many populations are you assuming? [Integers]
maxpops = 20

## 2. How many burnin you wish to do before collecting data [Integers]
burnin = 100000

## 3. How long do you wish to collect the data after burnin [Integers]
mcmc = 1000000

## 4. Name of your dataset.  Don't remove quotes. No spaces allowed. Exclude the '.str' extension.
##    e.g. dataset = "sim" if your datafile is called 'sim.str'
dataset = "OCWA_8pops"

## 5. How many runs of Structure do you wish to do for every assumed cluster K? [Integers]
kruns = 20

## 6. Number of individuals [Integers]
numind = 178

## 7. Number of loci [Integers]
numloci = 10

## 8. What is the ploidy [Integers 1 through n]
ploidy = 2

## 9. How is the missing data coded? Write inside quotes. e.g. missing = "-9"
missing = "-9"

## 10. Does the data file contain every individual on 2 lines (0) or 1 line (1). [Boolean]
onerowperind = 1

## 11. Do the individuals have labels in the data file?  [Boolean]
label = True

## 12. Are populations identified in the data file? [Boolean]
popdata =  True

## 13. Do you wish to set the popflag parameter? [Boolean]
popflag = True

## 14. Does the data file contain location identifiers (Not the same as population identifier) [Boolean]
locdata = False

## 15. Does the data file contain phenotypic information? [Boolean]
pheno = False

## 16. Does the data file contain any extra columns before the genotype data begins? [Boolean]
extracols = False

## 17. Does the data file contain a row of marker names at the top? [Boolean]
markers = True

## 18. Are you using dominant markers such as AFLP? [Boolean]
dominant = False

## 19. Does the data file contain information on map locations for individual markers? [Boolean]
mapdist = False

## 20. Is the data in correct phase? [Boolean]
phase = False

## 21. Is the phase information provided in the data? [Boolean]
phaseinfo = False

## 22. Does the phase follow markov chain? [Boolean]
markov = False

## 23. Do you want to make use of parallel processing [Boolean]
##     Note that you must have GNU parallel installed and available
##     www.gnu.org/s/parallel
##     You can check availability of the program by running 'which parallel' at the
##     command prompt. If a destination of the file is returned, then it is available.
##     If not available, it must be installed locally or through your system administrator.

parallel = True

## 24. How would you like to define the number of cores for parallel processing ['number' or 'percent']
##     Use 'percent' if you would like to define the percentage of available cores to use.  For instance,
##     on a quad-core machine you might use 'percent' here and '75' for cores to use 3 of the 4 processors.
##     Use 'number' if you want to explicitely define the number of cores used.

core_def = 'number'

## 25. How many cores would you like to use [integer]
##     This represents either a pecentage or the physical number of cores as defined in core_def (#24).

cores = 12

## 26. Would you like to automatically run structureHarvester?  [boolean]
##     Note that you must have program installed and available.
##     https://users.soe.ucsc.edu/~dearl/software/structureHarvester/

harvest = True

########## End of questions ##########
########## Please do not write any other information in this file ###########
