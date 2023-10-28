import pandas as pd
import os
import sys

main_23_wards = [
    'Chiyoda Ward', 'Chuo Ward', 'Minato Ward', 'Shinjuku Ward', 'Bunkyo Ward',
    'Taito Ward', 'Sumida Ward', 'Koto Ward', 'Shinagawa Ward', 'Meguro Ward',
    'Ota Ward', 'Setagaya Ward', 'Shibuya Ward', 'Nakano Ward', 'Suginami Ward',
    'Toshima Ward', 'Kita Ward', 'Arakawa Ward', 'Itabashi Ward', 'Nerima Ward',
    'Adachi Ward', 'Katsushika Ward', 'Edogawa Ward'
]


def clean_data(input_path, output_path):
    df = pd.read_csv(input_path, encoding='shift_jis')

    # solve the encoding issue by replace Japanese : to _
    df.columns = df.columns.str.replace("：", "_")

    # only take data that within the main 23 wards
    df = df[df['City,Town,Ward,Village'].isin(main_23_wards)]

    # remove irrelevant columns - columns that related to frontage
    df.drop(list(df.filter(regex='Frontage')), axis=1, inplace=True)

    # remove irrelevant columnds - Total floor area(m^2) & Prefecture
    df.drop(['Prefecture', 'Total floor area(m^2)'], axis=1, inplace=True)

    # filter out transactions that related to houses - apartment sales & private house sales
    df = df[df['Type'].isin(['Pre-owned Condominiums, etc.',
                            'Residential Land(Land and Building)'])]

    # Convert 'Area(m^2)' to a numeric data type (float)
    df['Area(m^2)'] = pd.to_numeric(df['Area(m^2)'], errors='coerce')

    # fill the column with proper calculation
    df['Transaction-price(Unit price m^2)'] = (
        df['Transaction-price(total)'] / df['Area(m^2)'] / 1000000).round(2)

    # save to new file
    df.to_csv(output_path, index=False)


if __name__ == "__main__":

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    csv_files = [file for file in os.listdir(
        input_folder) if file.endswith('.csv')]

    for file in csv_files:
        input_file_path = os.path.join(input_folder, file)
        output_file_path = os.path.join(output_folder, file)
        clean_data(input_file_path, output_file_path)
