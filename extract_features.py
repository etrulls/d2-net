import argparse

import numpy as np

import imageio

import torch

from tqdm import tqdm

import scipy
import scipy.io
import scipy.misc

from lib.model_test import D2Net
from lib.utils import preprocess_image
from lib.pyramid import process_multiscale

import os
from IPython import embed

# Argument parsing
parser = argparse.ArgumentParser(description='Feature extraction script')

            )
    else:
        raise ValueError('Unknown output type.')
