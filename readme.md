# Japan Real Estate Transaction Trend Analysis

## Overview

This project aims to analyze real estate transaction trends in Japan over the recent five years. While the project currently includes data analysis for the first and second quarters of 2023, the intention is to extend the analysis to cover a five-year period.

The analysis will focus on properties within the main 23 wards of Tokyo.

The project includes data cleaning, filtering, and calculation steps, followed by the use of Excel to create pivot tables for a detailed analysis.

## Data Source

The original data used for this project can be downloaded from the [MLIT (Ministry of Land, Infrastructure, Transport and Tourism )](https://www.land.mlit.go.jp/webland_english/download.html). The data is available in CSV format.

## Project Structure

The project consists of the following key components:

1. **Python Script & Data Cleaning**: A Python script, `data_cleaning.py`, is used to clean and preprocess the raw data. The script performs the following tasks:

   - Reads CSV files and solves encoding issues.
   - Filters data to include only transactions within the main 23 wards of Tokyo.
   - Removes irrelevant columns.
   - Filters out transactions related to apartments and private houses.
   - Converts 'Area(m^2)' to a numeric data type and calculates the unit price per square meter.
   - Saves the cleaned data to new CSV files in the "clean_data" folder.

2. **Pivot Table Analysis**: After data cleaning, Excel is used to create pivot tables for detailed analysis. The pivot tables help uncover trends and insights about real estate transactions in Japan for the specified period.

3. **Visualization with Charts**: The project includes the use of charts within pivot tables to visualize the analysis results.

## Running the Python Script

To clean the data and prepare it for analysis, use the following command in your terminal or command prompt:

```bash
python data_cleaning.py input_folder_path output_folder_path
```

Future Work

The current project covers the analysis of the first and second quarters of 2023. However, the project's future scope is to extend the analysis to cover a five-year period. This will provide a more comprehensive view of real estate transaction trends in Japan over the years.
