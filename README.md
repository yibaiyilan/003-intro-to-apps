# 003 Intro to apps

The purpose of this repo is to teach the basics of managing a virtual environment and running a simple python script (app.py). The results can be deployed as a static webpage following [these instructions](https://austinlasseter.medium.com/how-to-host-a-static-website-on-an-amazon-s3-bucket-be25a613586a).

## Python virtual environments

When you’re working on an application and you plan to deploy it to the cloud, you need to get in the habit of always working in a python environment. This can be a little tedious at first, but it helps make sure that the list of libraries that are installed on one machine will be identical to the list of libraries installed on another. Failing to do this will result in a lot of conflict down the road.

* [More about virtual environments](https://docs.python.org/3/library/venv.html#)

There are two ways to make virtual environments - pip and conda. Sagemaker is built using the Anaconda distribution of python (so it uses conda), but it’s also compatible with pip environments. However, the heroku platform is not compatible with Anaconda environments, and your requirements.txt file will choke on heroku if you create it using conda. So let’s use pip.

Because we’re going to be working a lot with Heroku, we also need to be aware of which python versions Heroku supports (it only supports a few versions). You can read more about that [here] (https://devcenter.heroku.com/articles/python-support)


## Steps to create your environment

For the purpose of today’s lesson, here’s what you should do.
Step | Instructions | Terminal Command |
--- | ---      | ---  |
1 | Confirm that Sagemaker already has installed python version 3.9 | python --version |
2 | Create a new environment named `env` | python -m venv env | 
3 | Activate the new environment to use it | source env/bin/activate | 
4 | Install the basic requirements | pip install -r requirements.txt |
5 | Add another installation | pip install dash |
6 | Update the requirements file | pip freeze > requirements.txt |

