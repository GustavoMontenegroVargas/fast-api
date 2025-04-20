# python-pro

[Add your project desciption here as same in pyproject.toml]

This is a template GitHub repo that you can use for starting your python development journey. Follow the instructions listed below to learn how to use it.

Content:

- [Set up your development environment](#set-up-your-development-environment)
- [Adding more project dependencies](#adding-more-project-dependencies)
- [Working with makefile](#working-with-makefile)
- [Working with notebooks](#working-with-notebooks)

___________________

## Set up your development environment

0. If using Visual Studio Code install the following extensions: 

> python

> even_better_toml

Having python dev ecosystem for VS Code will make these steps efortless. If you are using a different IDE, look for a similar extension or try the steps to check the ecosystem features are integrated by default.

In the other hand, `even_better_toml` is used to have suggestions when modifying your `.toml` file. 

1. Install uv: 

```bash
pip install uv
```

or

```bash
pip3 install uv
```

UV is used as package manager due to its dependency conflicts resolution speed.

2. Locate your terminal at the repo's root folder. Then, create a new virtual env by running:

```bash
uv sync
```

Considerations:

- A new virtual environment based in the pyproject.toml will be created installing the main dependencies under "dependencies".

- Virtual Envs are highly recommended to avoid compatibility issues in your base OS.

- Folders & python files under "packages" will be available across all your repo files within the same .venv. So, you can work in nested files as working relative to root. For this case, "src" & "consts.py". This is possible due to this configuration installs your repo project as editable. Meaning, as main dependency. 

- You should create a .venv for each repo that you have. UV + pyproject.toml makes the repo's dev envs highly replicable.  

3. Activate it by running:

-  For Mac/Linux:

```bash
source .venv/bin/activate
```

- For Windows:

```shell
.venv\Scripts\activate
```

You will notice that your repo's project name will be appear at the left side of your terminal. This means that your new python environment was configured correctly. 

In order to confirm the editable mode of your project, run the following:

```bash
uv pip show project-name
```

The details of your project will be displayed as package. 

_____________________

Now, that your env is set up, you can start coding with **.py** scripts as usual with **.venv** as python-interpreter. For installing your dev dependencies from an optional group, just run:

```bash
make dev
```
___________________

## Adding more project dependencies

The `pyproject.toml` file supports main & optional depdendencies. `Main deprendencies` are used as the core of all your project, but the optional are used when you just want to perform some specifc tasks, reducing the size of your environment.

If you would like to add more dependencies to your current virtual environment as main dependency, but at the same time that it is replicated directly in your pyproject.toml, use:

```bash
uv add package-name
```

This will install the package in your same venv and then it will be automatically written in the `dependencies` group in the `pyproject.toml`. So, the next time that you want to build or re-build the same env, this package will be already included. 

Optional dependencies can be installed manually as follows:

```bash
uv pip install -e .["my-optional-group-name"]
```

We use uv to indicate that we want to install the depdencies in the virtual environment instead of the base OS. For example, `dev` dependencies is a group listed in the `pyproject.toml` under `[project.optional-dependencies]`. You should follow the same syntax if you want to create a new one. The real way to install the `dev` dependency group is:

```bash
uv pip install -e .[dev]
```
___________________

## Working with makefile

You can choose installing optional dev dependency group as showed above or just running:

```bash
make dev
```

This does the same thing and runs the same command, the difference is that the last one uses a shortcut from a `makefile`. 

This repo has also a `makefile` template for adding shortcuts to common, repetitive or complex terminal commands. In order to create a new shortcut or `recipe`, use the following syntax in the `makefile`:

```bash
dev: 
	@echo "Installing development dependencies"
	uv pip install -e .[dev]
```

In order to call them in your terminal, you just need to type `make shortcut`:

```bash
make dev
```

Use `make test` to run all the tests related to this project.
___________________

## Working with notebooks

You can also use jupyter notebooks with the same .venv configuration as jupyter kernel. 

1. Install the `jupyter` extensión. 

2. Go to `notebooks > everything_works.ipynb` file & click on `select kernel`.

3. Choose `python environments > .venv`. Make sure that the `.venvs` refers to the repo where you created it. 

If no `.venv` is displayed, you will need to modify your Python extension in VS Code.

Go `extensions > python > engine  symbol > settings > Python: Venv Folders`. Then, add the absolute path of your repo as new item. Python extension will use it to look for existing virutal environments. Finally, reload the VS Code Window to get the last changes.

4. Run all cells of `everything_works.ipynb` in order to check the set up. 

If an issue with `ipykernel` raises, then make sure to run `make dev` where thata dependency is listed. Reload the window and retry to run the notebook.

___________________

**Happy Coding!**








