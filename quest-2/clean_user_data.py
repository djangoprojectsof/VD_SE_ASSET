import pandas as pd
import re

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def clean_user_data(input_csv, output_csv):
    df = pd.read_csv(input_csv)

    df.drop_duplicates(subset='user_id', keep='first', inplace=True)

    df = df[df['email'].apply(is_valid_email)]


    df.to_csv(output_csv, index=False)

input_csv = 'user_data.csv'
output_csv = 'cleaned_user_data.csv'

clean_user_data(input_csv, output_csv)
print(f"Cleaned data has been written to {output_csv}.")
