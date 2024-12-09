#!/bin/bash
#SBATCH -A MST109178        # Account name/project number
#SBATCH -J Mutect2      # Job name
#SBATCH -p ngs186G           # Partition Name
#SBATCH -c 28               # core preserved
#SBATCH -o gout.log          # Path to the standard output file 
#SBATCH -e gerr.log          # Path to the standard error ouput file
#SBATCH --mem=186G           # memory used
#SBATCH --mail-user=linlary@ntu.edu.tw
#SBATCH --mail-type=END



export SENTIEON_LICENSE=140.110.16.119:8990
module load biology/bcftools/1.13
module load biology/htslib/1.13
#module load libs/singularity/3.7.1
#module load pkg/Anaconda3
#source /opt/ohpc/Taiwania3/pkg/anaconda3/bin/activate
#source activate
#conda init
#source activate
#conda deactivate
#conda activate
python gatk.py
