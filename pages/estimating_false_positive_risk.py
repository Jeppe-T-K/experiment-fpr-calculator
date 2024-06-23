import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from typing import Any

from modules.nav import Navbar

alpha, beta = Navbar()

st.markdown("# Estimate the false positive risk (FPR)")

# These two elements will be filled in later, so we create a placeholder
# for them using st.empty()

left_column, right_column = st.columns(2)

p_h0_ss = 1 - left_column.slider('Prior success rate (**1-π**)', 0.0, 1.0, 0.10, 0.01)

right_column.latex(r"\textup{FPR} = \frac{\alpha \cdot \pi}{\alpha \cdot \pi + (1-\beta) \cdot (1-\pi)}")
right_column.markdown("**π** is the prior probability of null hypothesis, that is P(H_0)")
right_column.markdown("**α** is the threshold used to determine the statistical significance (SS), commonly 0.05 for a two-tailed t-test, and 0.025 for the positive tail")
right_column.markdown("**β** is the type-II error (usually 0.2 for 80% power)")

fpr = lambda prior_pi, alpha_, beta_: alpha_ * prior_pi / (alpha_ * prior_pi + (1-beta_) * (1-prior_pi))

st.write("The false positive risk is: ", np.round(fpr(p_h0_ss, alpha, beta)*100, 1), "%")

previous_pis = np.linspace(0.01, 0.5, 101)
alphas = [0.005, 0.01, 0.05, 0.1, alpha]
fpr_df = pd.concat(
    [
        pd.DataFrame(
            data=np.array([previous_pis, [alpha_]*len(previous_pis)]).T,
            columns=["prior_pi", "alpha"])
        for alpha_ in alphas
    ],
)
fpr_df["fpr"] = fpr_df.apply(lambda x: fpr(1-x["prior_pi"], x["alpha"], beta),
                             axis=1)

fig, ax = plt.subplots()
ax.grid()
fpr_plot = sns.lineplot(data=fpr_df, x="prior_pi", y="fpr", hue="alpha", ax=ax)
st.pyplot(fig)
