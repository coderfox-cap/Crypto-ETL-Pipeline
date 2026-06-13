from extract import extract_data
from transform import transform_data
from load import load_data, load_history
from logger import logger


def run_pipeline():

    try:

        logger.info("Starting pipeline")

        raw_df = extract_data()

        clean_df = transform_data(raw_df)

        load_data(clean_df)

        load_history(clean_df)

        logger.info(
            "Pipeline completed successfully."
        )

    except Exception as e:

        logger.error(
            f"Pipeline failed: {e}"
        )

        raise


if __name__ == "__main__":
    run_pipeline()