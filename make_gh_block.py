from prefect.filesystems import GitHub

# alternative to creating GitHub block in the UI

gh_block = GitHub(
   name="try-prefect-github-connector", 
   repository="https://github.com/jonwhittlestone/try-prefect-github-connector",
   #access_token="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" # only required for private repos
)

# gh_block.get_directory("week_2_workflow_orchestration/prefect/hwk_04") # specify a subfolder of repo
gh_block.save("try-prefect-github-connector", overwrite=True)
