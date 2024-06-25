import rioxarray
import xarray
from scipy.ndimage import generic_filter

# Function for generic_filter
def mean_filter(window):
    return window.mean()

# Array for generic_filter
covariate = rioxarray.open_rasterio("Uganda Covariate Rasters/elevation.tif")
covariate_values = covariate.to_numpy()

# Convert raster distance (degrees) to pixel size for generic_filter
smooth_distances = [5, 11, 51] # in km

# Apply smoothing
for distance in smooth_distances:
    smoothed = generic_filter(covariate_values, mean_filter, size=distance)
    smoothed_data_xr = xarray.DataArray(smoothed, dims=covariate.dims, coords=covariate.coords, attrs=covariate.attrs)
    smoothed_data_xr.rio.to_raster("Uganda Smoothed Rasters/smooth_uganda_elevation_" + str(distance*2) + "km_2018.tif")