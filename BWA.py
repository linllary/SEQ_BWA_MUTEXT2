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
#print(f1)
#print(f2)

#print(bwa)

for ff1, ff2 in zip(f1, f2):
    gr=ff1.split('WES/')[1].split('_')[0]
    Mapping1=Mapping+'/'+gr
    os.system('mkdir '+Mapping1)
    os.system('('+bwa+' mem -M -R '+'\'@RG\\tID:'+gr+'\\tSM:'+gr+'\\tPL:ILLUMINA\''+' -t '+core+' -K 1000000 '+refaq+' '+ff1+' '+ff2+' || echo -n \'error\')'+ ' | '+senc+' util sort -r '+refaq+' -o '+Mapping1+'/'+gr+'.sorted.bam -t '+core+' --sam2bam -i-')
    os.system(senc+' driver -t '+core+' -i '+Mapping1+'/'+gr+'.sorted.bam --algo LocusCollector --fun score_info '+Mapping1+'/'+gr+'.score.txt')
    os.system(senc+' driver -t '+core+' -i '+Mapping1+'/'+gr+'.sorted.bam --algo Dedup --rmdup --score_info '+Mapping1+'/'+gr+'.score.txt --metrics '+Mapping1+'/'+gr+'.metrix.txt '+Mapping1+'/'+gr+'.deduped.bam')
    os.system(senc+' driver -r '+refaq+' -t '+core+' -i '+Mapping1+'/'+gr+'.deduped.bam --algo Realigner -k '+known_Mills_indels+' -k '+known_1000G_indels+' '+Mapping1+'/'+gr+'.realigned.bam')
    print('mkdir '+Mapping1)
    print('('+bwa+' mem -M -R '+'\'@RG\\tID:'+gr+'\\tSM:'+gr+'\\tPL:ILLUMINA\''+' -t '+core+' -K 1000000 '+refaq+' '+ff1+' '+ff2+' || echo -n \'error\')'+ ' | '+senc+' util sort -r '+refaq+' -o '+Mapping1+'/'+gr+'.sorted.bam -t '+core+' --sam2bam -i-')
    print(senc+' driver -t '+core+' -i '+Mapping1+'/'+gr+'.sorted.bam --algo LocusCollector --fun score_info '+Mapping1+'/'+gr+'.score.txt')
    print(senc+' driver -t '+core+' -i '+Mapping1+'/'+gr+'.sorted.bam --algo Dedup --rmdup --score_info '+Mapping1+'/'+gr+'.score.txt --metrics '+Mapping1+'/'+gr+'.metrix.txt '+Mapping1+'/'+gr+'.deduped.bam')
    print(senc+' driver -r '+refaq+' -t '+core+' -i '+Mapping1+'/'+gr+'.deduped.bam --algo Realigner -k '+known_Mills_indels+' -k '+known_1000G_indels+' '+Mapping1+'/'+gr+'.realigned.bam')
    #break

