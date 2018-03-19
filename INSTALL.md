# Setup the environment for deep_bortox


## git repo setup

We added faceswap as a [git submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules), so you just need to clone this repo with:

```bash
$ git clone git@github.com:DomagojKorais/deep_bortox.git
```

And then update and downloads the submodules with:

```bash
$ git submodules init
$ git submodules update
```

## Cosilt setup

First of all, **move on a computing node**! because the master nodes uses old packages.

```bash
$ qsub -I -l nodes=1:ppn=24 -l walltime=4:00:00 -q jrc
```

The `jrc` queue is available (as of 2018/03/17), and provides computing nodes with two K20s NVIDIA cards each.

A "meta-module" which loads all the modules needed by TensorFlow 1.6.0 is available, and can be loaded with:

```bash
$ module load tensorflow/1.6.0/cuDNN/7.1/cuda/9.0/python/3.6.4/gnu/6.4.0
```

Now python 3.6 is loaded, the virtualenv package is available. Create a virtualenv (a sort of "virtual machine" for python packages) with:

```bash
$ mkdir ~/.venvs/
$ virtualenv ~/.venvs/deepfake/
```

Now, every time we want to use our packages, we need to load the meta-module and activate the virtualenv just created with:

```bash
$ source ~/.venvs/deepfake/bin/activate
```

We can then move to the git repository previously downloaded, enter the faceswap directory, and install the python packages required. As of 2018/03/17 we need to trick a bit the file with the requirements to make it install the already available TF 1.6.0 package:

```bash
$ sed -i 's/tensorflow-gpu==1.5.0/tensorflow-gpu==1.6.0/' requirements-gpu-python36-cuda9.txt
```

Then load a more recent cmake package with:

```bash
$ module load cmake/3.4.3
```

needed to compile the `dlib` dependency.

And eventually, install the requirements with:

```bash
$ pip install -r requirements-gpu-python36-cuda9.txt
```

## Normal usage

After we set the environment up, a normal usage would be:

```bash
$ module load tensorflow/1.6.0/cuDNN/7.1/cuda/9.0/python/3.6.4/gnu/6.4.0
$ source ~/.venvs/deepfake/bin/activate
$ cd /path/to/deep_bortox/faceswap/
```

and we're ready to go:
```bash
$ ./faceswap.py # ...
```
