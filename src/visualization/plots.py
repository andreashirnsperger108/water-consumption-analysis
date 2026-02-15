from __future__ import annotations
import matplotlib.pyplot as plt
import pandas as pd

def plot_series(df: pd.DataFrame, x: str, y: str, title: str = ""):
    fig, ax = plt.subplots()
    ax.plot(df[x], df[y])
    ax.set_title(title or f"{y} over {x}")
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    fig.tight_layout()
    return fig, ax
