import os
from glob import glob

src = '/home/trulls/imw2019-test'

seqs = [p.split('/')[-1] for p in glob('{}/*'.format(src))]

if not os.path.isdir('txt'):
    os.makedirs('txt')

for seq in seqs:
    ims = glob('{}/{}/*.jpg'.format(src, seq))
    with open('txt/list-{}.txt'.format(seq), 'w') as f:
        for im in ims:
            f.write('{}\n'.format(im))
