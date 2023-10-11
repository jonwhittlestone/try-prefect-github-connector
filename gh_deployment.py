from prefect.filesystems import GitHub
from flow import etl_web_to_gcs
from prefect.deployments import Deployment
from prefect.filesystems import GitHub

block = GitHub.load("try-prefect-github-connector")

deployment = Deployment.build_from_flow(
    flow=etl_web_to_gcs,
    name="gh-deploy",
    version=1,
    storage=block,
    # work_queue_name="demo",
    # work_pool_name="default-agent-pool",
)

if __name__ == "__main__":
    deployment.apply()
