import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

with open('data.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

df_long = pd.melt(df, id_vars=['name', 'vore'], value_vars=['awake', 'sleep_rem', 'sleep_total'], 
                  var_name='variable', value_name='value')

fig, ax = plt.subplots(figsize=(10, 8))

size_order = [5, 10, 15, 20]

sns.scatterplot(data=df_long, x='variable', y='name', size='value', hue='vore', 
                sizes=(20, 200), palette='husl', alpha=0.8, edgecolor='gray', legend=False, ax=ax)

for index, row in df_long.iterrows():
    ax.annotate(f"{row['value']:.1f}", (row['variable'], row['name']), 
                textcoords="offset points", xytext=(10, 0), ha='left', va='center', fontsize=8, color='black')

ax.set_title("Sleep Metrics by Animal", fontsize=16)
ax.set_xlabel("Sleep Metrics", fontsize=12)
ax.set_ylabel("Animals", fontsize=12)


legend_labels = {
    "carni": "Carnivore", "herbi": "Herbivore", "insect": "Insectivore", "omni": "Omnivore"
}

for category in df['vore'].unique():
    ax.scatter([], [], c=sns.color_palette("husl")[df['vore'].unique().tolist().index(category)], 
               label=legend_labels[category], s=100)

for size in size_order:
    ax.scatter([], [], c='gray', alpha=0.6, s=size * 10, label=f'{size}')

ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), title="Categories/Values", 
          ncol=1, frameon=False)

plt.tight_layout()

plt.savefig("balloon_plot.png")

plt.show()
