![alt text for screen readers](images/banner.png)
# Vini's Pre-Processing Tool
A simple, online, and open-source tool to make online changes on a Excel Sheets and record the applied changes in a reusable JSON archive that can be used on other sheets.

## Internal usage
The internal usage of the app is based on transform the XLSX app into a Parquet file and make the transformations into that, when the user saves the file, the system retrieves the edited file and a JSON file containing the commands.  
When a new file is inputed.

## Used technologies
- Python and AWS (Lambda and API Gateway)