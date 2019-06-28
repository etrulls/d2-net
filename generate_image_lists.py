import os
from glob import glob

src = '/cvlabdata1/cvlab/datasets_eduard/imw2019-test'

seqs = [p.split('/')[-1] for p in glob(f'{src}/*')]

for seq in seqs:
    ims = glob(f'{src}/{seq}/*.jpg')
    with open(f'list-{seq}.txt', 'w') as f:
        for im in ims:
            f.write(f'{im}\n')
