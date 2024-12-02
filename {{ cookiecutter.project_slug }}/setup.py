from setuptools import setup, find_packages

setup(
    name={{ cookiecutter.project_slug }},
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Add your project's dependencies here
        # 'some_package>=1.0.0',
    ],
    entry_points={
        "console_scripts": [
            # Add command line scripts here
            # 'your_command=your_module:main_function',
        ],
    },
    author={{ cookiecutter.author_name }},
    author_email={{ cookiecutter.author_email }},
    description="A short description of your project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    # url="https://github.com/yourusername/your_project_name",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
