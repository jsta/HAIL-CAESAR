import rasterio
import xarray as xr
import matplotlib.pyplot as plt

# fname_expected = "test/known_good_answers/boscastle50m_72hr_u/WaterDepths3360.asc"
fname_result = "test/results/boscastle50m_72_u/Elevations4200.asc"

out_data = rasterio.open(fname_result).read(1)
out_data = xr.DataArray(out_data)

fig, ax = plt.subplots()
out_data.plot(ax=ax)
ax.set_title("test")
fig.savefig("output.pdf")
plt.close(fig)
