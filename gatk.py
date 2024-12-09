import os
import glob


#f1=os.listdir('/staging/biology/linlary2023/SCRIPT/')
f1=glob.glob('/staging/biology/linlary2023/WES/*_1*')
f2=glob.glob('/staging/biology/linlary2023/WES/*_2*')
f1=sorted(f1)
f2=sorted(f2)
refaq='/staging/reserve/paylong_ntu/AI_SHARE/reference/GATK_bundle/2.8/b37/human_g1k_v37_decoy.fasta'
bwa="/staging/reserve/paylong_ntu/AI_SHARE/software/Sentieon/sentieon-genomics-202112/bin/bwa"
senc="/staging/reserve/paylong_ntu/AI_SHARE/software/Sentieon/sentieon-genomics-202112/bin/sentieon"
core='40'
known_Mills_indels="/staging/reserve/paylong_ntu/AI_SHARE/reference/GATK_bundle/2.8/b37/Mills_and_1000G_gold_standard.indels.b37.vcf"
known_1000G_indels="/staging/reserve/paylong_ntu/AI_SHARE/reference/GATK_bundle/2.8/b37/1000G_phase1.indels.b37.vcf"
Mapping='/staging/biology/linlary2023/Mapping/BWALL'
gpu='/opt/ohpc/Taiwania3/pkg/biology/DeepVariant/deepvariant_1.4.0-gpu.sif'
dep='/opt/deepvariant/bin/run_deepvariant'
gatk='/opt/ohpc/Taiwania3/pkg/biology/GATK/gatk_v4.2.3.0/gatk'
#print(f1)
#print(f2)
bed='/staging/biology/linlary2023/WES/truth/CTR_hg19.b37.bed'
#print(bwa)

for ff1, ff2 in zip(f1, f2):
  gr=ff1.split('WES/')[1].split('_')[0]
  Mapping1=Mapping+'/'+gr
  Calling=Mapping1+'/gatk'
  Calling1=Calling+'/'+gr
  if os.path.isdir(Calling)==False:
    os.system('mkdir '+Calling)
    os.system(gatk+' --java-options \"-Xmx180g\" Mutect2 -I '+Mapping1+'/'+gr+'.realigned.bam -O '+Calling1+'.Mutect2.vcf -R '+refaq)
    os.system('bgzip -c '+Calling1+'.Mutect2.vcf > '+Calling1+'.Mutect2.vcf.gz')
    os.system('bcftools index '+Calling1+'.Mutect2.vcf.gz')
    os.system('bcftools view -R '+ bed+' '+ Calling1+'.Mutect2.vcf.gz'+' > '+Calling1+'.Mutect2.filter.vcf')
    os.system('bcftools view -i \"strlen(ALT)=1\" '+Calling1+'.Mutect2.filter.vcf > '+Calling1+'.Mutect2.filter.snv.temp.vcf')
    os.system('bcftools view -i \"strlen(REF)=1\" '+Calling1+'.Mutect2.filter.snv.temp.vcf > '+Calling1+'.Mutect2.filter.snv.vcf')
    os.system('bcftools view -i \"strlen(ALT)>1\" '+Calling1+'.Mutect2.filter.vcf > '+Calling1+'.Mutect2.filter.inde1.vcf')
    os.system('bcftools view -i \"strlen(REF)>1\" '+Calling1+'.Mutect2.filter.vcf > '+Calling1+'.Mutect2.filter.inde2.vcf')
    os.system('bgzip -c '+Calling1+'.Mutect2.filter.inde1.vcf > '+Calling1+'.Mutect2.filter.inde1.vcf.gz')
    os.system('bgzip -c '+Calling1+'.Mutect2.filter.inde2.vcf > '+Calling1+'.Mutect2.filter.inde2.vcf.gz')
    os.system('bcftools index '+Calling1+'.Mutect2.filter.inde1.vcf.gz ')
    os.system('bcftools index '+Calling1+'.Mutect2.filter.inde2.vcf.gz ')
    os.system('bcftools concat -a -D '+Calling1+'.Mutect2.filter.inde1.vcf.gz '+Calling1+'.Mutect2.filter.inde2.vcf.gz > '+Calling1+'Mutect2.filter.inde.vcf')
    #os.system('bcftools view -e \"strlen(ALT)=strlen(REF)\" '+Calling1+'.Mutect2.filter.inde.vcf > '+Calling1+'.Mutect2.filter.indel.vcf')
    #bcftools view -e "strlen(ALT)=strlen(REF)" SRR13076390.Mutect2.filter.inde.vcf
    print('mkdir '+Calling)
    print(gatk+' --java-options \"-Xmx180g\" Mutect2 -I '+Mapping1+'/'+gr+'.realigned.bam -O '+Calling1+'.Mutect2.vcf -R '+refaq)
    print('bgzip -c '+Calling1+'.Mutect2.vcf > '+Calling1+'.Mutect2.vcf.gz')
    print('bcftools index '+Calling1+'.Mutect2.vcf.gz')
    print('bcftools view -R '+ bed+' '+ Calling1+'.Mutect2.vcf.gz'+' > '+Calling1+'.Mutect2.filter.vcf')
    print('bcftools view -i \"strlen(ALT)=1\" '+Calling1+'.Mutect2.filter.vcf > '+Calling1+'.Mutect2.filter.snv.temp.vcf')
    print('bcftools view -i \"strlen(REF)=1\" '+Calling1+'.Mutect2.filter.snv.temp.vcf > '+Calling1+'.Mutect2.filter.snv.vcf')
    print('bcftools view -i \"strlen(ALT)>1\" '+Calling1+'.Mutect2.filter.vcf > '+Calling1+'.Mutect2.filter.inde1.vcf')
    print('bcftools view -i \"strlen(REF)>1\" '+Calling1+'.Mutect2.filter.vcf > '+Calling1+'.Mutect2.filter.inde2.vcf')
    print('bgzip -c '+Calling1+'.Mutect2.filter.inde1.vcf > '+Calling1+'.Mutect2.filter.inde1.vcf.gz')
    print('bgzip -c '+Calling1+'.Mutect2.filter.inde2.vcf > '+Calling1+'.Mutect2.filter.inde2.vcf.gz')
    print('bcftools index '+Calling1+'.Mutect2.filter.inde1.vcf.gz ')
    print('bcftools index '+Calling1+'.Mutect2.filter.inde2.vcf.gz ')
    print('bcftools concat -a -D '+Calling1+'.Mutect2.filter.inde1.vcf.gz '+Calling1+'.Mutect2.filter.inde2.vcf.gz > '+Calling1+'Mutect2.filter.inde.vcf')
    #bgzip -c SRR13076390.Mutect2.vcf > SRR13076390.Mutect2.vcf.gz
    #bcftools index SRR13076390.Mutect2.vcf.gz
    #bcftools view -R /staging/biology/linlary2023/WES/truth/CTR_hg19.b37.bed  SRR13076390.Mutect2.vcf.gz > SRR13076390.Mutect2.filter.vcf
    #break
