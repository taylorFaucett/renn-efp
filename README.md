# Generate EFPs 

This script gives an example of the generation process for the EFPs used in the paper "Mapping Machine-Learned Physics into a Human-Readable Space"
Link: https://arxiv.org/abs/2010.11998

If you are using conda, the necessary dependencies are given in the `environment.yml` file and can be installed with

```
conda env create -f environment.yml
```

Otherwise, you just need numpy, pandas, tqdm (for nice progress bars) and energyflow to run this script. These can be installed with pip instead, using:

```
pip install numpy pandas tqdm energyflow
```

The script `generate_efp.py` takes in a pair of kappa, beta values and a max graph dimension and outputs a pandas dataframe with all EFPs matching that criteria. The dataframe is then saved as a parquet file under the directory `data/efp`. Some example files are given containing 500 generated datapoints (e.g. the table below shows the first few columns and rows from `data/efp/dim_5_k_2_b_2.parquet`). The column headers (e.g. 2_1_0) refers to the n, d and k numbers of the graph. `n_d_k = 2_1_0` tells you that the graph has 2 nodes, 1 edge and unique identifier 0 (i.e. to distinguish between any other graphs that might have the same number of nodes and edges but in a different configuration).

|    |    1_0_0 |       2_1_0 |       2_2_0 |       2_3_0 |       2_4_0 |       2_5_0 |
|---:|---------:|------------:|------------:|------------:|------------:|------------:|
|  0 | 0.426704 | 0.00645015  | 0.00141954  | 0.000415171 | 0.000151909 | 6.25341e-05 |
|  1 | 0.565734 | 0.00079564  | 1.44671e-05 | 2.80761e-07 | 6.28402e-09 | 1.82549e-10 |
|  2 | 0.156292 | 0.00139294  | 0.000151456 | 1.97074e-05 | 3.14421e-06 | 6.18503e-07 |
|  3 | 0.800919 | 0.000488304 | 3.80144e-05 | 3.12724e-06 | 2.65635e-07 | 2.29621e-08 |
|  4 | 0.264212 | 0.000788507 | 3.09005e-05 | 1.47133e-06 | 8.62341e-08 | 6.46898e-09 |

Note that the main dataset has 5 Million events. Depending on your computer, you may need to break this task into smaller batches and/or generate subsets of your data in batches of the EFPSet. 
