import pathlib

import energyflow as ef
import numpy as np
import pandas as pd
from tqdm import tqdm

home = pathlib.Path.cwd()


def generate_EFP(X, y, dim, kappa, beta):
    # Generate the set of EFPs with specified parameters of dimension, kappa aand beta
    # "p==1" tells EFPSet to only return "prime" graphs. i.e. graphs with no disconnected edges
    # normed=None should be left as None. The pre-processed data is already normalized.
    efpset = ef.EFPSet(f"d<={dim}", "p==1", beta=beta, kappa=kappa, normed=None)

    # specs gives a list of details for each EFP in the set
    # The order of parameters in the list is given as: n, e, d, v, k, c, p, h
    # The meaning of each parameter (i.e. n, e, d) is given at: https://energyflow.network/docs/efp/#efpset
    # The three important ones are n="number of vertices", d="number of edges", k="unique identifier when paired with (n,d)"
    specs = efpset.specs
    efp_labels = [f"{x[0]}_{x[2]}_{x[4]}" for x in specs]

    # Generate all EFPs from pre-processed data
    efp_df = pd.DataFrame(efpset.batch_compute(X), columns=efp_labels)

    # Append a copy of the targets to each dataset
    # This is optional but it's nice to have your labels with your training data
    efp_df["targets"] = y

    # Store the EFPs
    efp_df.to_parquet(home / "data" / "efp" / f"dim_{dim}_k_{kappa}_b_{beta}.parquet")


def main():
    # Kappa and Beta values to loop through.
    # Each pair of (kappa,beta) values will generate a seperate parquet file with EFPs with that selection of (k,b)
    kappas = [1, 2]
    betas = [1, 2]

    # Max dimension for EFPs. e.g. dim=3 will generate all EFPs with dimension <= 3
    dim = 5

    # Load pre-processed data
    # Data is a pickled dictionary containing two dataframes: features and targets
    # Features is a dataframe consisting of a list of normalized [pT, eta, phi] values
    # You can select a subset of the 5 million points by specifying a value for N

    raw_data = pd.read_pickle(home / "data" / "LL_normalized.pkl")
    X = raw_data.features.to_numpy()
    y = raw_data.targets.values

    # # Loop through (k,b) pairs and generate a dataframe of EFP values
    t = tqdm([(k, b) for k in kappas for b in betas])
    for kappa, beta in t:
        t.set_description(
            f"Processing EFPs with parameter: dim <= {dim} and (k={kappa}, b={beta})"
        )
        generate_EFP(X, y, dim, kappa, beta)


if __name__ == "__main__":
    main()
