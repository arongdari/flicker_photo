#Flickr-Photo
Extract users trajectories from geo-tagged photo/video data of [YFCC100M](https://webscope.sandbox.yahoo.com/catalog.php?datatype=i&did=67) dataset.

--------------------
## Trajectory construction

Trajectories are constructed through following three major steps (More detail descriptions are provided in [trajectory_construction.ipynb](https://github.com/arongdari/flickr-photo/blob/master/src/trajectory_construction.ipynb)):

1. Extract photos/videos taken near Melbourne area from original YFCC100M dataset ([`src/filtering_bigbox.py`](https://github.com/arongdari/flickr-photo/blob/master/src/filtering_bigbox.py))
2. Extract initial trajectories based on the extracted photos/videos ([`src/generate_tables.py`](https://github.com/arongdari/flickr-photo/blob/master/src/generate_tables.py))
3. Filter out some abnormal trajectories using various criteria ([`src/trajectory_construction.ipynb`](https://github.com/arongdari/flickr-photo/blob/master/src/trajectory_construction.ipynb))

--------------------
## Trajectory Analysis

Some statistics and analysis about the extracted trajectories are provided in [`src/flickr_analysis.ipynb`](https://github.com/arongdari/flickr-photo/blob/master/src/flickr_analysis.ipynb)

--------------------
## Output files
###```data``` Data files
 * ```Melbourne-bbox.kml```   The two (big/small) bounding boxes of Melbourne used for extracting relevant photos/videos from original YFCC100M dataset
 * ```Melbourne-bigbox.csv```   Photos/videos taken inside of the big bounding box, output of ```src/filtering_bigbox.py```
 * ```trajectory_photos.csv```  Trajectorie file, output of ```src/generate_tables.py```
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
 * ```trajectory_stats.csv```  Stats for each trajectory, output of ```src/generate_tables.py```
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

-----------------------
## POI and Trajectory data in Melbourne

### Notebooks
 * ```src/poi_wikipedia.ipynb``` IPython notebook to extract POI information from Wikipedia webpages.
 * ```src/traj_Melb.ipynb```     IPython notebook to construct trajectories by mapping photos to POIs.
 * ```src/dataset_Melb.ipynb```  IPython notebook to describe the dataset of trajectories in Melbourne.
 * ```src/suburb-name.ipynb```   Adds the suburb name based on ABS SLA2 to ```data/poi-Melb-all.csv``` and saves it to ```data/poi-Melb-all-suburb.csv``` *GDAL is annoying to install*

### Data
 * ```data/poi-Melb-all.csv``` POI data file, generated by IPython notebook ```src/poi_wikipedia.ipynb```, ```data/poi-Melb-all-suburb.csv``` contains suburb names of POIs.
  * poiID: POI unique ID
  * poiName: POI Name
  * poiTheme: POI Category
  * poiLat: POI Latitude
  * poiLon: POI Longitude
  * poiURL: URL of Wikipedia webpage that describes this POI

 * ```data/userVisits-Melb.csv``` Trajectory data file, generated by IPython notebook ```src/traj_Melb.ipynb```.
  * photoID: Flickr Photo unique ID
  * userID: User ID
  * dateTaken: The date that this photo was taken
  * poiID: POI unique ID
  * poiTheme: POI Category
  * poiFreq: Number of photos taken at the POI
  * seqID: Trajectory unique ID

 * ```data/traj-noloop-all-Melb.csv``` Trajectories extracted from ```data/userVisits-Melb.csv``` in an approach that no loops/subtours exist,i.e. use the order of the first occurrences of POIs to form a trajectory.
  * userID: User ID
  * trajID: Trajectory ID
  * poiID: POI ID
  * startTime: When a user start to visit the POI, approximated by the time the first photo taken by the user at that POI
  * endTime: When a user leave the POI, approximated by the time the last photo taken by the user at that POI
  * #photo: Number of photos taken at the POI by the user
  * trajLen: Number of POIs in the trajectory
  * poiDuration: Visit duration (in seconds) at the POI

 * ```data/Melb_recommendations.csv``` Trajectory recommendation results of different methods using ```data/poi-Melb-all.csv``` and ```data/traj-noloop-all-Melb.csv```, ```NA``` represent failed recommendation due to e.g. ILP timeout. ```data/Melb_recommendations_F1.csv``` is the file with F1-scores of the recommended trajectories by different methods and ```data/Melb_recommendations_pairsF1.csv``` is the file with pairs-F1-scores.
  * trajID: Trajectory ID
  * REAL: The ground truth trajectory
  * PoiPopularity: Trajectory recommended using POI popularity only
  * PoiRank: Trajectory recommended using POI ranking by rankSVM
  * Markov: Trajectory recommended using POI-POI transition matrix and Viterbi decoding
  * MarkovPath: Trajectory recommended using POI-POI transition matrix and integer linear programming (ILP)
  * Rank+Markov: Trajectory recommended using both POI ranking by rankSVM and POI-POI transition matrix, and Viterbi decoding
  * Rank+MarkovPath: Trajectory recommended using both POI ranking by rankSVM and POI-POI transition matrix, and ILP 
  * StructuredSVM: Trajectory recommended using Structured Support Vector Machine
  * PersTour: Trajectory recommended using method described in [this paper](https://www.nicta.com.au/pub-download/full/8557/)
  * PersTour-L: Trajectory recommended by a method similar to PersTour, with time constraint replaced by length constraint

 * Visualisation: Please import these KMZ files to [Google My Maps](https://www.google.com/mymaps) to visualise.
  * ```data/Melb_POI.kmz``` POIs in Melbourne dataset.
  * ```data/Melb_transition_most_popular_POI.kmz``` Transitions from the most popular POI, i.e., the Federation Square.
  * ```data/Melb_transition_Margaret_Court_Arena.kmz``` Transitions from the Margaret Court Arena.
  * ```data/Melb_transition_Queen_Victoria_Market.kmz``` Transitions from the Queen Victoria Market.
  * ```data/Melb_transition_RMIT_city.kmz``` Transitions from the RMIT city.
  * ```data/Melb_transition_RMIT_city_top30.kmz``` Top 30 transitions from the RMIT city.
  * ```data/Melb_transition_University_of_Melbourne.kmz``` Transitions from the University of Melbourne.
  * ```data/Melb_transition_University_of_Melbourne_top30.kmz``` Top 30 transitions from the University of Melbourne.
  * ```data/Melb_traj_pass_Government_House.kmz``` Trajectories that include the Government House.
  * ```data/Melb_traj_pass_Melbourne_Cricket_Ground.kmz``` Trajectories that include the Melbourne Cricket Ground (MCG).
  * ```data/Melb_traj_recommendation_example.kmz``` Example of trajectories recommended by different approaches.
  * ```data/Melb_terrible_traj_photo_seq.kmz``` Example of an ugly trajectory.
