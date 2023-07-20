# connected-health-joint-angle-visualisation
Repository for Connected Health Joint Angle Visualisation

## Visualisation
Joint angle plotting and sample data

#### Usage
1. Install matplotlib
```
python -m pip install -U pip
python -m pip install -U matplotlib
```
2. Run the program
```
python3 Visualise.py joint graph-interval dimension frames-json-file
```
Example:
```
python3 Visualise.py elbow 30 2d ./Sample-Data/frames-1-10.json
```
Notes:
```
Help
        -h  : Print help
        -i  : Ignore erroneous keypoints
        -w  : Print warnings
        -s  : Save parsed json data
        -S  : Save visualisation graph
```

### Sample-Data
Sample data for visualisation
