#About Project

First, I also refer to some other people's codes, thanks to the people who wrote these techniques!

In this project, I use the text library from sogou. Thanks for offering.

Now, I simply say the main flow of the project.

1. CHI method for feature selection in file `train-feature-selection.py`
2. TF-IDF algorithm for feature weight in file `train-feature-weight.py` and `test-feature-weight.py`
3. SVM algorithm for classifying with the open source tool `libsvm-3.21`

In the step 3, we will use the following commands to use the tool `libsvm-3.21`.

1. Scale the file `train.svm` to [0, 1], the command is `svm-scale -l 0 -u 1 train.svm > trainscale.svm`
2. Scale the file `test.svm` to [0, 1], the command is `svm-scale -l 0 -u 1 test.svm > testscale.svm`
3. Training the file `trainscale.svm`, the command is `svm-train -s 1 trainscale.svm trainscale.model`
4. Predict the file `testscale.svm`, the command is `svm-predict testscale.svm trainscale.model testscale.result`

At last, the accuracy is 80.2%.

Of course, there are many mistakes and shortcomings, we can learn and progress together, thank you!