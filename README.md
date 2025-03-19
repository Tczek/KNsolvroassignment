# KNsolvroassignment

## Project Overview
This project is designed to work with **Conda**. Please note that unexpected **issues** may occur when installing dependencies via:
pip install -r requirements.txt

## Installation and Setup
To run the program, follow these steps:

1. **Ensure Conda is installed** on your system.
2. **Extract the project folder** if you downloaded it as a `.zip` file.
3. **Place the extracted folder** in your desired location.
4. **Open Anaconda Prompt** and navigate to the project directory:

   ```sh
   cd path/to/KNsolvroassignment
   ```

5. **Create the Conda environment** by running:

   ```sh
   conda env create -f environment.yml
   ```

6. **Activate the environment**:

   ```sh
   conda activate KNsolvroassignment
   ```

7. **Run the main script**:

   ```sh
   python main.py
   ```

> **Note:** The first run may take some time as **Matplotlib** builds the font cache.

## Running Jupyter Notebook
After successful execution, a Jupyter Notebook should automatically open in your web browser. You may need an authentication token.

1. To retrieve the token, run the following command in Anaconda Prompt:

   ```sh
   jupyter server list
   ```

2. Copy the token and set up a password.
3. You should now see **interactive plot and visualizations**.

**Enjoy!** 🚀

