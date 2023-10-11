from prefect import flow, task


@task(log_prints=True)
def log_me():
    print('📋 log from task')

@flow(retries=3)
def etl_web_to_gcs() -> None:
    """The main function."""
    log_me()

if __name__ == "__main__":
    etl_web_to_gcs()
