import seaborn as sns
import matplotlib.pyplot as plt

# Load the Penguins dataset
penguins = sns.load_dataset("penguins")

# Remove rows with missing values
penguins = penguins.dropna()

# Create a jointplot of flipper length vs. bill length
sns.jointplot(
    data=penguins,
    x="flipper_length_mm",
    y="bill_length_mm",
    hue="species",
    kind="scatter",
    palette="Set1",
    height=6
)

# Display the plot
plt.show()
