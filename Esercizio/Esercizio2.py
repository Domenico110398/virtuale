# %%
import pandas as pd
import numpy as np

# Create a DataFrame with random values
np.random.seed(42)  # For reproducibility
df = pd.DataFrame(np.random.rand(10, 4), columns=['A', 'B', 'C', 'D'])

# Define a function to highlight specific columns with different colors
def highlight_columns(s):
    color_map = {
        'A': 'background-color: lightblue;', 
        'B': 'background-color: lightgreen;', 
        'C': 'background-color: lightcoral;', 
        'D': 'background-color: lightgoldenrodyellow;'
    }
    return [color_map.get(s.name, '')] * len(s)

# Apply styling
styled_df = df.style.apply(highlight_columns)

# Display the styled DataFrame
styled_df


