#Flickr-Photo
Extract trajectories of users from geo-tagged photo/video data from [YFCC100M](https://webscope.sandbox.yahoo.com/catalog.php?datatype=i&did=67) dataset.

--------------------
## Trajectory construction

Trajectories are constructed through following three major steps (More detail descriptions are provided in [trajectory_construction.ipynb](https://github.com/arongdari/flickr-photo/blob/master/src/trajectory_construction.ipynb)):

1. Extract photos/videos taken near Melbourne area from original YFCC100M dataset ([`src/filtering_bigbox.py`](https://github.com/arongdari/flickr-photo/blob/master/src/filtering_bigbox.py))
2. Extract initial trajectories based on the extracted photos/videos ([`src/generate_tables.py`](https://github.com/arongdari/flickr-photo/blob/master/src/generate_tables.py))
3. Filter out some abnormal trajectories using various criteria ([`src/trajectory_construction.ipynb`](https://github.com/arongdari/flickr-photo/blob/master/src/trajectory_construction.ipynb))

--------------------
## Trajectory Analysis

Some statistics and analysis about the extracted trajectories are provided in [`src/trajectory_construction.ipynb`](https://github.com/arongdari/flickr-photo/blob/master/src/flickr_analysis.ipynb)

--------------------
## Output files
###```data``` Data files
 * ```Melbourne-bbox.kml```   The two (big/small) bounding boxes of Melbourne used for extracting relevant photos/videos from original YFCC100M dataset
 * ```Melbourne-bigbox.csv```   Photos/videos taken inside of the big bounding box, output of ```src/filtering_bigbox.py```
 * ```Melb-table1.csv```  Trajectorie file, output of ```src/generate_tables.py```
  * Each line represents one photo/video with following information
  * Trajectory_ID: trajectory ID of entry (multiple entries consist single trajectory)
  * Photo_ID: Unique Photo(Video) ID of entry
  * User_ID: User ID
  * Timestamp: When a photo/video has been taken
  * Longitude: Longitude of entry
  * Latitude: Latitude of entry
  * Accuracy: GPS Accuracy level (16 - the most accurate, 1 - the least accurate)
  * Marker: 0 if the entry is photo, 1 if the entry is video
  * URL: flickr URL to the entry
 * ```Melb-table2.csv```  Stats for each trajectory, output of ```src/generate_tables.py```
  * Each line shows statistics about corresponding trajectory
  * Trajectory_ID: Unique trajectory ID
  * User_ID: User ID
  * #Photo: Number of photos+videos in the trajectory
  * Start_Time: When the first photo/video has been taken
  * Travel_Distance(km): Sum of the distances between consecutive points (Euclidean Distance)
  * Total_Time(min): The time gap between the first photo and the last photo
  * Average_Speed(km/h): Travel_Distances(km)/Total_Time(h)

### ```src``` Source files
 * ```filtering_bigbox.py```  Python3 scripts to extract photos taken in the big bounding box from YFCC100M dataset
 * ```generate_tables.py```  Python3 scripts to generate trajectories and stats of trajectories
 * ```traj_visualise.py```   Python3 scripts to generate KML files to visualise trajectories
