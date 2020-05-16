from distutils.core import setup
setup(
    name='wang_ds_toolbox',         # How you named your package folder (MyLib)
    packages=['wang_ds_toolbox'],   # Chose the same as "name"
    version='0.1.0',      # Start with a small number and increase it with every change you make
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    # Give a short description about your library
    description='This is a collection of data science functions that I have found extremely useful across a wide variety of use cases. This is mostly a library just for me, but feel free to use it if you want. This is a library that handles tabular data mostly. This specific version takes a lot of deprecated functions from fastai0.7 and mainly pulls from their random forest lessons. I will be continuously adding to this lib as I learn more data science things',
    author='Alec Wang',                   # Type in your name
    author_email='alswang18.programming@gmail.com',      # Type in your E-Mail
    # Provide either the link to your github or to your website
    url='https://github.com/user/alswang18',
    # I explain this later on
    download_url='https://github.com/user/reponame/archive/v_01.tar.gz',
    # Keywords that define your package best
    keywords=['Data Science', 'Random Forests', 'Visualizations'],
    install_requires=[            # I get to this in a second
        'scikit-learn', 'tqdm', 'Pillow', 'numpy', 'pandas', 'ipython', 'more-itertools', 'isoweek', 'sklearn-pandas', 'pandas-datareader', 'pandas-profiling', 'pandas-summary', 'bcolz', 'graphviz', 'matplotlib'
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Data Scientists',
        'Topic :: Data Science :: Data Science Pipeline tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
