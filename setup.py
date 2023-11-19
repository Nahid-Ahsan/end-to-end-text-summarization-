import setuptools

with open("README.md", "r", encoding = 'utf-8') as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "end-to-end-text-summarization-"
AUTHOR = "Nahid-Ahsan"
SRC_REPO = "textSummerizer"
AUTHOR_EMAIL = "nahidahsan74@gmail.com"

setuptools.setup(
    name =  SRC_REPO,
    version = __version__,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    description = "End to end text summarization",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/{AUTHOR}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": "https://github.com/{AUTHOR}/{REPO_NAME}/issues",
    },
    packages_dir = {"": "src"},
    packages = setuptools.find_packages(where="src")

    )