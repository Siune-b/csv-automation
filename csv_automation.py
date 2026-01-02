import pandas as pd
import glob

csv_files = glob.glob("csv_folder/*.csv")

df_list = [pd.read_csv(file) for file in csv_files]
combined_df = pd.concat(df_list, ignore_index=True)

combined_df.drop_duplicates(inplace=True)

combined_df.columns = [col.strip().lower().replace(" ", "_") for col in combined_df.columns]

combined_df.to_csv("merged_cleaned.csv", index=False)

print("CSV files merged and cleaned successfully!")
