# Convert a NetCDF file into zarr file

import xarray
from pathlib import Path

file_netcdf = 'GFS_s_on.nc'
file_zarr = 'GFS.zarr'

# Define the dataset path
dataset_dir = Path('.')
dataset_dir = dataset_dir.resolve()
dataset_dir.mkdir(parents=True, exist_ok=True)
dataset_path_netcdf = dataset_dir / file_netcdf
dataset_path_zarr = dataset_dir / file_zarr

print(dataset_path_netcdf)
print(dataset_path_zarr)

# Open the netCDF dataset
dataset = xarray.open_dataset(dataset_path_netcdf, engine="h5netcdf")
# Convert to Zarr with the same chunking as original NetCDF file
# GFS file
dataset.chunk({"valid_time":1, "isobaricInhPa":1, "latitude":-1, "longitude":-1}).to_zarr(dataset_path_zarr)

# CMEMS file
#dataset.chunk({"time":1, "lat":-1, "lon":-1}).to_zarr(dataset_path_zarr)

