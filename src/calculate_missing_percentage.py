import pandas as pd
import click


@click.command()
@click.option('--file_path')
@click.option('--output_file')

def calculate_missing_percentage(file_path, output_file):
    """
    Calculate the percentage of missing values for each column in a DataFrame.

    Parameters:
    - df: pandas DataFrame

    Returns:
    - pandas Series representing the mean of missing values for each column
    """
    # read in data file
    df = pd.read_csv(file_path)
    
    result = df.isna().mean()
    
    result.to_csv(output_file)

if __name__ == "__main__":
    calculate_missing_percentage()
