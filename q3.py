import geopandas as gpd
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource, HoverTool
from bokeh.palettes import Viridis256
from bokeh.transform import linear_cmap
import numpy as np

# Path to your downloaded shapefile
shapefile_path = "D:/Hassan/7th assessment 2/geodata"

# Load the shapefile
world = gpd.read_file(shapefile_path)

# Print columns to identify potential country name column
print("Columns in dataset:", world.columns)

# Check for column containing country names and map it to 'name'
if 'ADMIN' in world.columns:  # Example: Use 'ADMIN' as country names
    world.rename(columns={'ADMIN': 'name'}, inplace=True)
elif 'SOVEREIGNT' in world.columns:  # Fallback example
    world.rename(columns={'SOVEREIGNT': 'name'}, inplace=True)
else:
    print("No suitable column for country names found. Adding placeholders.")
    world['name'] = 'Unknown'

# Add synthetic population data if 'pop_est' is missing
if 'pop_est' not in world.columns:
    print("'pop_est' column is missing. Adding synthetic data...")
    world['pop_est'] = np.random.randint(1000000, 200000000, size=len(world))

# Prepare the GeoJSON data
geo_source = GeoJSONDataSource(geojson=world.to_json())

# Create a Bokeh figure
p = figure(
    title="Interactive World Map",
    width=800,
    height=500,
    tools="pan,wheel_zoom,reset",
    tooltips=[("Country", "@name"), ("Population", "@pop_est")],
)

# Add patches for countries
mapper = linear_cmap(
    field_name='pop_est',
    palette=Viridis256,
    low=world["pop_est"].min(),
    high=world["pop_est"].max(),
)

p.patches(
    'xs',
    'ys',
    source=geo_source,
    fill_color=mapper,
    fill_alpha=0.7,
    line_color="white",
    line_width=0.5,
)

# Add HoverTool
p.add_tools(HoverTool(tooltips=[("Country", "@name"), ("Population", "@pop_est")]))
p.axis.visible = False

# Save the output to an HTML file and open it in a browser
output_file("interactive_world_map.html")
show(p)
