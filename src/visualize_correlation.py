import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import click


@click.command()
@click.option('--file_path')
@click.option('--output_file')

def visualize_correlation(file_path, output_file):
    """
    Visualize the correlation matrix of numerical features.

    Parameters:
    - file_path: str, Path to the input CSV file.
    - output_file: str, Path to save the correlation heatmap image.

    Returns:
    - heatmap
    """
    df = pd.read_csv(file_path)
    plt.figure(figsize=(12, 7))
    
    heatmap = sns.heatmap(df.select_dtypes(['int', 'float']).corr(), vmin=-1, vmax=1, annot=True, cmap='PuOr')
    heatmap.set_title('Features Correlating isAlive', fontdict={'fontsize': 10}, pad=12)

    plt.savefig(output_file)
    
if __name__ == "__main__":
    visualize_correlation()
