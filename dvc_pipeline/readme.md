* Run from parent dicrectory `deploying-a-scalable-pipeline-in-prod-demos`: `dvc exp run dvc_pipeline/dvc.yaml`
* Push tracked data changes `dvc` by running: `dvc push` to local storage folder "../local_remote".
* Commit and push changes to git. In particular `*.loc` file containing all parameters.
* Print out metrics: `dvc metrics show --all-commits`.
```bash
(udacity) dkysylychyn@MacBookPro deploying-a-scalable-pipeline-in-prod-demos % dvc metrics show --all-commits   
Revision                                  Path                           C     F1 score
workspace                                 dvc_pipeline/output/score.txt  12.0  0.5
d10b69b76ea91539344b049e5aeda063fbcda070  dvc_pipeline/output/score.txt  10.0  0.5
b34094e3b9f8f3a9a6ce60851b6842a7d5891a16  dvc_pipeline/output/score.txt  1.0   0.6667
76eb28f492a5a6c8034f63fb8d19bd8bbcb2c2ff  dvc_pipeline/output/score.txt  0.5   0.6667
```

Proper pipeline example here: 
https://github.com/treeverse/example-get-started
