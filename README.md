# evaluation
Evaluation of annnotations and data extraction

## Description

The project is devoted to the evaluation of metaphor annotations and corrections between two or more annotators. The current project includes different files aimed to evaluate the agreement between annotatord and extract information needed for the agreement calculation.

## Usage

1. The script ``Agreement_Calculating.py`` gets two files with annotators' labels in CSV-format and calculates F1-Score and Cohen's Kappa to evaluate the agreement between two annotators. Run it as follows:
    ```
    python3 Agreement_Calculating.py labels1.csv labels2.csv
    ```

2. The script ``TSV_Extraction.py`` gets the file in the TSV format, which was got during the annotation work with Inception (https://inception-project.github.io/). The file contains sentences or lines (depends on annotator's work format) and their labels. The script extract lines and the corresponding labels and saves to output to the TXT format. Run the script as follows:
    ```
    python3 TSV_Extraction.py file.tsv output.txt
    ```
    
### Other files are following.
