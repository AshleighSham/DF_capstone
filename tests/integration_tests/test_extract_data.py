from etl.extract.extract import (
    extract_data,
    EXPECTED_PERFORMANCE
)
import timeit


def test_extract_daat_returns_all_data():
    expected_shape = (9999, 35)
    # Call the function to get the DataFrame
    df = extract_data()

    # Verify the dimensions of the DataFrame
    assert df.shape == expected_shape, (
        f"Expected DataFrame shape to be {expected_shape}, but got {df.shape}"
    )


def test_extract_data_performance():
    execution_time = timeit.timeit(
        "extract_data()",
        globals=globals(),
        number=1
    )

    # Call the function to get the DataFrame
    df = extract_data()

    # Load time per row
    actual_execution_time_per_row = execution_time / df.shape[0]

    # Assert that the execution time is within an acceptable range
    assert actual_execution_time_per_row <= EXPECTED_PERFORMANCE, (
        f"Expected execution time to be less than or equal to "
        f"{str(EXPECTED_PERFORMANCE)} seconds, but got "
        f"{str(actual_execution_time_per_row)} seconds"
    )
