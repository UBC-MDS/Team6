import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import click


@click.command()
@click.option('--file_path', type=str, help="Path to the CSV file containing numerical features.")
@click.option('--output_file', type=str, help="Path to save the correlation heatmap image.")

def visualize_correlation(file_path, output_file):
    """
    Visualize the correlation matrix of numerical features.

    Parameters:
    - file_path (str): Path to the CSV file containing numerical features.
    - output_file (str): Path to save the correlation heatmap image.

    Returns:
    - None

    This function reads a CSV file specified by 'file_path', selects numerical features,
    calculates the correlation matrix, and generates a heatmap. The resulting heatmap
    is saved as an image file specified by 'output_file'.
    """

    # Read in data file
    df = pd.read_csv(file_path)

    # Set up the matplotlib figure
    plt.figure(figsize=(20, 10))
    
    # Generate a heatmap using seaborn
    heatmap = sns.heatmap(df.select_dtypes(['int', 'float']).corr(), vmin=-1, vmax=1, annot=True, cmap='PuOr')
    heatmap.set_title('Features Correlating', fontdict={'fontsize': 10}, pad=12)

    # Save the heatmap as an PNG image file
    plt.savefig(output_file)
    
if __name__ == "__main__":
    visualize_correlation()