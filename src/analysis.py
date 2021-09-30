"""
This script performs a regression
"""
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from pathlib import Path


def regression():
    # Load data and format datetime
    df = pd.read_csv(
        Path("raw/raw_data.csv"),
        index_col=0,
    )
    reg = smf.ols(formula='total ~ alcohol + no_previous + not_distracted', data=df).fit()
    latex_results = reg.summary().as_latex()
    open(Path('output/regression.tex'), 'w').write(latex_results)


def chart():
    # Load data and format datetime
    df = pd.read_csv(
        Path("raw/raw_data.csv"),
        index_col=0,
    )
    fig, ax = plt.subplots()
    ax.scatter(df["total"], df["alcohol"])
    plt.savefig(Path("output/scatter.pdf"))


if __name__ == "__main__":
    regression()
    chart()
