from setuptools import setup,find_packages

with open('requirements.txt','r') as f:
    requirements = f.read().splitlines()
setup(
    name='Anime_recommender',
    version='0.1',
    description='An Streamlit app for recommending anime based on user preferences',
    install_requires=requirements,
    packages=find_packages(),
    author='Saul Villarados',
)
#pip install -e . 