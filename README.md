
# RAG using SLMs

This repository contains a stripped down version of Retrieval-Augmented Generation (RAG) based Small Language Model (SLM) development performed at HCLTech Inc


## Use Case

- SLMs are a lightweight alternative to conventional LLMs and are typically trained on a corpus of high-quality documents with a smaller number of tokens
- They can be run using less compute power locally on hardware such as laptops and mobile phones
- Private, on-device processing of data ensures privacy for sensitive business data
- Fully local processing eliminates the need for an internet connection and reliance on the cloud


## Pre-requisites

Before running any of the notebooks present in this repository perform the following actions:

1. **Ollama**: Ollama is a convenient wrapper application to get started with developing using some of the most popular small language models (SLMs) locally on your computer. Install Ollama [here](https://ollama.com/download).
  - After installing Ollama, you can download any SLM that is present on the [models](https://ollama.com/library) page. As an example, installing the Microsoft Phi3 model can be done using:
  ```bash
    ollama pull phi3
  ```
  - To start Ollama server (which will be used by Langchain or the Ollama library in Python) use
  ```bash
    ollama serve
  ```
2. **Installing Required Dependencies**: Install all the required Python packages required to run the Python notebooks. The recommended way is to do this in a virtual Python environment. If you're using Anaconda this can be achieved in the Anaconda Navigator GUI or using the command:
  ```bash
    conda create -n your_env_name python=python_version -y
    conda activate your_env_name
  ```
  - To install all dependencies use
  ```bash
    pip install -r requirements. txt
  ```
  - OR you can also install the conda environment directly from the file provided in the repository
  ```bash
    conda env create -f environment.yml
  ```

