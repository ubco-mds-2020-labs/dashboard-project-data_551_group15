import pandas as pd

# Load the data
gdp = pd.read_csv('../data/GDP.csv', skiprows=[i for i in range(0, 4)])

# Handling null values and deleting non usable information.
gdp.drop(gdp.index[0], inplace=True)
gdp['Geography'] = gdp['Geography'].fillna(method='ffill')
gdp['North American Industry Classification System (NAICS) 7 8'] = gdp[
    'North American Industry Classification System (NAICS) 7 8'].fillna(method='ffill')
gdp.reset_index(inplace=True)
gdp.drop('index', axis=1, inplace=True)
gdp = gdp[:-27]
gdp = gdp.replace(',', '', regex=True)
gdp.replace(to_replace="..", value="0", inplace=True)

# Indicating the correct data types
gdp['North American Industry Classification System (NAICS) 7 8'] = \
    gdp['North American Industry Classification System (NAICS) 7 8'].str.split('[').str[0]
gdp['Geography'] = gdp['Geography'].astype('string')
gdp['North American Industry Classification System (NAICS) 7 8'] = gdp[
    'North American Industry Classification System (NAICS) 7 8'].astype('string')
gdp['Reference period'] = pd.to_numeric(gdp['Reference period'])
gdp['Chained (2012) dollars 9'] = pd.to_numeric(gdp['Chained (2012) dollars 9'])

# Renaming the columns
gdp.rename(columns={"North American Industry Classification System (NAICS) 7 8": "Industry", "Reference period": "Year",
                    "Chained (2012) dollars 9": "GDP"}, inplace=True)

# Adding the growth rates columns
gdp['Percent Change'] = gdp.GDP.pct_change()
gdp.loc[gdp.Year == 1997, "Percent Change"] = 0

# For geographical data:
# import geopandas as gpd
# can = gpd.GeoDataFrame.from_file("lpr_000b16a_e.shp")
# merged=can.set_index('PRENAME').join(gdp.set_index('Geography'))
# merged.reset_index(inplace=True)
# merged.drop('index', axis=1, inplace=True)
#
# merged.head()

# test the output
if __name__ == "__main__":
    print(gdp.head())
