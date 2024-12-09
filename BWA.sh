#!/bin/bash
#SBATCH -A MST109178        # Account name/project number
#SBATCH -J Bwall      # Job name
#SBATCH -p ngs92G           # Partition Name
#SBATCH -c 14               # core preserved
#SBATCH -o Bout.log          # Path to the standard output file 
#SBATCH -e Berr.log          # Path to the standard error ouput file
#SBATCH --mem=92G           # memory used
#SBATCH --mail-user=linlary@ntu.edu.tw
#SBATCH --mail-type=END



export SENTIEON_LICENSE=140.110.16.119:8990
python BWA.py
