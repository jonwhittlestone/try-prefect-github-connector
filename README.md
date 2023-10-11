# try-prefect-github-connector

## Prerequisites
- Activate virtualenv and install deps
    ```sh
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

    ```

- Run prefect
    ```sh
    prefect server start
    ```

## Steps

1. Create block

```sh
python make_gh_block.py
```


2. Run deployment

```sh
python gh_deployment.py
```

3. Run agent

```sh
prefect agent start --pool "default-agent-pool" --work-queue "default"
```

Output

```bash
14:55:25.509 | INFO    | prefect.agent - Submitting flow run 'eade693f-9bdd-4155-a6b4-0e66e1f80d83'                                                                                    [47/89]
14:55:25.591 | INFO    | prefect.infrastructure.process - Opening process 'almond-panda'...                                                                                                   
14:55:25.603 | INFO    | prefect.agent - Completed submission of flow run 'eade693f-9bdd-4155-a6b4-0e66e1f80d83'                                                                              
<frozen runpy>:128: RuntimeWarning: 'prefect.engine' found in sys.modules after import of package 'prefect', but prior to execution of 'prefect.engine'; this may result in unpredictable beha
viour                                                                                                                                                                                         
14:55:27.875 | INFO    | Flow run 'almond-panda' - Downloading flow code from storage at None
14:55:28.753 | INFO    | Flow run 'almond-panda' - Created task run 'log_me-0' for task 'log_me'
14:55:28.754 | INFO    | Flow run 'almond-panda' - Executing 'log_me-0' immediately...
14:55:28.869 | INFO    | Task run 'log_me-0' - 📋 log from task stored at GitHub.com
14:55:28.894 | INFO    | Task run 'log_me-0' - Finished in state Completed()
...
```
