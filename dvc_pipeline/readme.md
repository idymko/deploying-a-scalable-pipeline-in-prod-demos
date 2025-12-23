## Execution Steps
Inn parent directory `deploying-a-scalable-pipeline-in-prod-demos`:
* Create the environment `udacity` and install the dependecies:
    * `$ udacity -p python3 .venv`
    * `conda activate udacity`
    * `$ pip install -r src/requirements.txt`
* `git init`
* `dvc init`

In child directory `dvc_pipeline`:
* Run from dicrectory `dvc exp run dvc_pipeline`: `dvc exp run`
* Set parameters: `dvc exp run --set-param train.C=10`
* Push tracked data and parameter changes by running: `dvc push` to local storage folder `../local_remote`. It contains all data files and parameters defined in `dvc_pipeline/dvc.yaml`.
* Commit and push changes to git. In particular `dvc.lock` file containing all parameters.

## Metrics 
* `dvc exp show`
    * https://doc.dvc.org/command-reference/exp/show#exp-show
    * Your terminal will enter a paginated screen by default, which you can typically exit by typing q.
* Print out metrics: `dvc metrics show --all-commits`.
    * Output
    ```bash
    (udacity) dkysylychyn@MacBookPro deploying-a-scalable-pipeline-in-prod-demos % dvc metrics show --all-commits   
    Revision                                  Path                           C     F1 score
    workspace                                 dvc_pipeline/output/score.txt  12.0  0.5
    d10b69b76ea91539344b049e5aeda063fbcda070  dvc_pipeline/output/score.txt  10.0  0.5
    b34094e3b9f8f3a9a6ce60851b6842a7d5891a16  dvc_pipeline/output/score.txt  1.0   0.6667
    76eb28f492a5a6c8034f63fb8d19bd8bbcb2c2ff  dvc_pipeline/output/score.txt  0.5   0.6667
    ```

## Infos
* `model.pkl`and `score.txt` from `output` are tracked by DVC. 
* They are stored locally in local remote "../local_remote" Google Drive Cloud connection did not work. 
* `dvc.lock` contains files hashes that refer to local remote "../local_remote".

## Reference DVC Pipeline example
* Pipeline example here: https://github.com/treeverse/example-get-started

