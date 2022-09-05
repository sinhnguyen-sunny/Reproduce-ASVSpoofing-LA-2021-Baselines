#!/bin/bash
# if necessary, load conda environment
eval "$(conda shell.bash hook)"
conda activate as-pytorch-asvspoof2021

# when running in ./projects/*/*, add this top directory
# to python path
export PYTHONPATH=$PWD/../../:$PYTHONPATH

