import setuptools

# reading README file helps you during publishing your package on PyPI
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


# specifying initial version 
__version__ = "0.0.0"

REPO_NAME = "NLP_Text_Summarizer_Project"
AUTHOR_USER_NAME = "ChaitaliKPatil"
SRC_REPO = "textSummarizer"   # it will be a new package.
AUTHOR_EMAIL = "patilchaitali71@gmail.com"



# code for local package setup
# it will  look for constructor file __init__ in every folder and will install it as a local package.
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)

# now you can install the requirements. Make sure you have -e . in your requirements.txt.