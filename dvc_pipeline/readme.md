## Execution Steps

### Environment Setup
Inn parent directory `deploying-a-scalable-pipeline-in-prod-demos`:
* Create the environment `udacity` and install the dependecies:
    * `$ udacity -p python3 .venv`
    * `conda activate udacity`
    * `$ pip install -r src/requirements.txt`
* `git init`
* `dvc init`

### Code Execution
In child directory `dvc_pipeline`:
* Run from dicrectory `dvc exp run dvc_pipeline`: `dvc exp run`
* Set parameters: `dvc exp run --set-param train.C=10`
* Push tracked data and parameter changes by running: `dvc push` to local storage folder `../local_remote`. It contains all data files and parameters defined in `dvc_pipeline/dvc.yaml`.
* Commit and push changes to git. In particular `dvc.lock` file containing all parameters.

### Metrics 
* Changes in metrics between two experiments: `dvc exp diff`
* Compare different experiemtns in current session: `dvc exp show` (stored locally): https://doc.dvc.org/command-reference/exp/show#exp-show.
    * Output 
    ```bash
    (udacity) dkysylychyn@MacBookPro dvc_pipeline % dvc exp show                      
    ──────────────────────────────────────────────────────────
    Experiment                 Created     C   F1 score   d
    ──────────────────────────────────────────────────────────
    workspace                  -          31        0.5   31 
    main                       07:36 PM    1    0.66667   1 
    ├── dbff0c7 [elder-ibex]   07:38 PM   31        0.5   31
    ├── d0a5399 [stony-scud]   07:37 PM   11        0.5   11
    └── 7b3576f [mangy-weft]   07:36 PM   21        0.5   21
    ──────────────────────────────────────────────────────────
    ```
* Compare different experiemtns in git commits `dvc exp show --all-commits`.
* Show current metric: `dvc metrics show`
* Show metrics for all git commits and current workspace: `dvc metrics show --all-commits`.
    * Your terminal will enter a paginated screen by default, which you can typically exit by typing q. 
    * Output
    ```bash
    (udacity) dkysylychyn@MacBookPro dvc_pipeline % dvc metrics show --all-commits
    Revision                                  Path               C     F1 score
    workspace                                 output/score.json  1     0.66667
    1faaa3d0750e49ab44c6adaaad2dec50bc57c558  output/score.json  11    0.5
    ```

## Infos
* `model.pkl`and `score.json` from `output` are tracked by DVC. 
* They are stored locally in local remote "../local_remote" Google Drive Cloud connection did not work. 
* `dvc.lock` contains files hashes that refer to local remote "../local_remote".

## Reference DVC Pipeline example
* Pipeline example here: https://github.com/treeverse/example-get-started

