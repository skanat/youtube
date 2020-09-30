# Python script for YouTube data collection
# Uses pandas Python Data Analysis Library


# Required Python libraries
import pandas as pd

# Retrieve YouTube data for a single channel
from googleapiclient.discovery import build

youTubeApiKey = ""  # Input your youTubeApiKey
youtube=build('youtube','v3',developerKey=youTubeApiKey)
channelId='UCt4t-jeY85JegMlZ-E5UWtA'  # Input the ID of the Youtube channel that you want to extract data

snippetdata=youtube.channels().list(part='snippet',id=channelId).execute()
print(snippetdata)

# Remove irrelevant parts of the data
snippetdata["items"][0]["snippet"].pop('thumbnails')
snippetdata["items"][0]["snippet"].pop('localized')
print(snippetdata)

# This is for displaying the whole dataframe in the output
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

# Constructs a dataframe from the relevant part of the snippet data
df = pd.DataFrame(snippetdata["items"][0]["snippet"],index=[0])
print(df)

# Writes the dataframe to an Excel file
writer = pd.ExcelWriter('C:/Users/zsk405/PycharmProjects/Youtube/ChannelInfo.xlsx', engine='openpyxl')
df.to_excel(writer)
writer.save()

# Writes the dataframe to a CSV file
df.to_csv("C:/Users/zsk405/PycharmProjects/Youtube/ChannelInfo.csv",sep=',',index=False)


