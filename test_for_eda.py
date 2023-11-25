import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from visualize_correlation import visualize_correlation  # Replace 'your_module' with the actual module or script name

# Test if the function ran withouth error
def test_visualize_correlation():
    # Use test data for testing
    test_df = test_df

    # Use pytest's built-in fixture to capture the standard output
    with pytest.raises(SystemExit):
        visualize_correlation(test_df)

    # Assertions to check if the function ran without errors
    assert plt.gcf() is not None

# Test if the relations is correlation
def test_visualize_correlation_is_correlation():
    test_df = test_df

    with pytest.raises(SystemExit):
        visualize_correlation(test_df)

    # Check if the color scale is present
    color_scale = plt.gci().get_array()
    assert color_scale is not None

    # Check if the color scale values are within the expected range of -1 to 1
    assert all(-1 <= val <= 1 for val in color_scale)
