import argparse
import pandas as pd

# Define the required columns
required_columns = ["STATION","DATE","LATITUDE","LONGITUDE","ELEVATION","NAME","IMMA_VER","ATTM_CT","TIME_IND","LL_IND","SHIP_COURSE","SHIP_SPD","ID_IND","WIND_DIR_IND","WIND_DIR","WIND_SPD_IND","WIND_SPEED","VV_IND","VISIBILITY","PRES_WX","PAST_WX","SEA_LVL_PRES","CHAR_PPP","AMT_PRES_TEND","IND_FOR_TEMP","AIR_TEMP","IND_FOR_WBT","WET_BULB_TEMP","DEW_PT_TEMP","SST_MM","SEA_SURF_TEMP","TOT_CLD_AMT","LOW_CLD_AMT","LOW_CLD_TYPE","CLD_HGT","MID_CLD_TYPE","HI_CLD_TYPE","WAVE_DIR","WAVE_PERIOD","WAVE_HGT","SWELL_DIR","SWELL_PERIOD","SWELL_HGT","TEN_BOX_NUM","ONE_BOX_NUM","DECK","SOURCE_ID","PLATFORM_ID","DUP_STATUS","DUP_CHK","NIGHT_DAY_FLAG","TRIM_FLAG","NCDC_QC_FLAGS","SOURCE_EXCLUSION_FLAG","OB_SOURCE","STA_WX_IND","PAST_WX2","DIR_OF_SWELL2","PER_OF_SWELL2","HGT_OF_SWELL2","THICKNESS_OF_I","CONCEN_OF_SEA_ICE","STAGE_OF_DEVELP","ICE_OF_LAND_ORIGIN","ICE_SIT_TREND","IND_FOR_PRECIP","AMT_PRECIP","DUR_OF_PER"]

# Set up argument parsing
parser = argparse.ArgumentParser(description="Preprocess a CSV file by ensuring required columns exist.")
parser.add_argument("csv_file", type=str, help="Raw CSV file")
parser.add_argument("output_file", type=str, help="Output CSV file")
args = parser.parse_args()

# Read the CSV file
csv_file = args.csv_file
output_file = args.output_file
df = pd.read_csv(csv_file)

# Ensure all required columns exist, add missing columns with NaN values
for col in required_columns:
    if col not in df.columns:
        df[col] = pd.NA  # Pandas native missing value

# Reorder columns to match the required structure
df = df[required_columns]

# Convert integer-like columns back to integers where possible
for col in df.columns:
    if pd.api.types.is_numeric_dtype(df[col]):
        if all(df[col].dropna().apply(lambda x: isinstance(x, (int, float)) and x == int(x))):  
            df[col] = df[col].astype("Int64")  # Ensures nullable integer format

# Save the updated CSV
df.to_csv(args.output_file, index=False)

print("Preprocessing complete. Missing columns added with null values.")
