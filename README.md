# Intro to simple apps

The purpose of this repo is to teach the basics of managing a virtual environment and running a simple python script (app.py). The results can be deployed as a static webpage following [these instructions](https://austinlasseter.medium.com/how-to-host-a-static-website-on-an-amazon-s3-bucket-be25a613586a).

## Python virtual environments

When you’re working on an application and you plan to deploy it to the cloud, you need to get in the habit of always working in a python environment. This can be a little tedious at first, but it helps make sure that the list of libraries that are installed on one machine will be identical to the list of libraries installed on another. Failing to do this will result in a lot of conflict down the road.

* [More about virtual environments](https://docs.python.org/3/library/venv.html#)

There are two ways to make virtual environments - pip and conda. Sagemaker is built using the Anaconda distribution of python (so it uses conda), but it’s also compatible with pip environments. However, the heroku platform is not compatible with Anaconda environments, and your requirements.txt file will choke on heroku if you create it using conda. So let’s use pip.

Because we’re going to be working a lot with Heroku, we also need to be aware of which python versions Heroku supports (it only supports a few versions). You can read more about that [here] (https://devcenter.heroku.com/articles/python-support)


## Requirements files

For the purpose of today’s lesson, here’s what you should do.
Step | Instructions | Terminal Command |
--- | ---      | ---  |
1 | Confirm that Sagemaker already has installed python version 3.9 | python --version |
2 | Create a new environment named `env` | python -m venv env | 
3 | Activate the new environment to use it | source env/bin/activate | 
4 | Install the basic requirements | pip install -r requirements.txt |
5 | Add another installation | pip install numpy |
6 | Update the requirements file | pip freeze > requirements.txt |


Take a moment to check out the new requirements file that’s been created. It lists all of your python dependencies which are installed in your environment. It will also be used to install these dependencies on heroku. This is a pretty basic list - for more advanced apps, you’ll need to have more libraries installed. 

## The `env` folder

We’ve also got a new folder called “env” which contains all the binary files used to install these libraries - that’s going to slow things down a lot when we try to push to github. To avoid that logjam, we need a hidden file called “.gitignore” which will tell git to “ignore” everything in the /env/ folder. But for reasons no one is sure about, JupyterLab won’t display hidden files in the left-hand navigation. Instead you have to open it using the “git” tab in the ribbon. 

Open up the .gitignore and make sure that /env/ is listed at the top as “env/” – I’ve provided a template with a lot of other common garbage files as well.

## The `.gitignore` file
The files required to install Python libraries (known as 'binaries') take up a lot of space, and we don't want to clutter github with them. So it's important to make sure you have a file at the top level of your repo, named `.gitignore`, which lists the name of your environment folder (which for us is called `env`). You can view the gitignore file in one of two ways:
* click on the "Git" button at the top of the SMSL ribbon, and select `.gitignore'.
* view it in terminal with `nano .gitignore`.

## Testing the app

We have a very simple application called `app.py`. Try running it in terminal with the following command: 
- `python app.py`

You'll get and error message indicating that it requires an additional library that's not included in our virtual environment. Solve this as follows:
- `pip install dash`

Now try running it again. This time you'll see that it's created a new file in the `docs`. Our simple app worked!

