import kagglehub

# Download latest version
path = kagglehub.dataset_download("joebeachcapital/top-10000-spotify-songs-1960-now")

print("Path to dataset files:", path)

