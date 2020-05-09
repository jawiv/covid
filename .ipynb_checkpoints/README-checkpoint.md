# covid

Notebooks now use the [Covidtracking](https://covidtracking.com) dataset

### Directions
1.  Click below to load a temporary jupyter environment to view the notebooks.
2.  Once binder has loaded, click on the "New" button in the top right-side. Select "Terminal". This will open a new window.
3.  At the command prompt, type "python update_data.py" and hit enter. This script will show some error details (as it is running some commands that are not useful in this temporary environment. Pay no attention to them. It will update the covid dataset to the most currently up to date version). Close this browser tab.
4.  In the file list, open any of the following files:

    * **covid.ipynb** - compares the current covid status in different states and vs the US. Can edit the list of states.
    * **ihme_model_hospital_bed_error.ipynb** - shows the error in the ihme model vs actual data. This is compared to the latest ihme model, but there are historical ihme models by date in the ihme/ folder.
    * **covid-tn-over-time.ipynb** - shows timeseries information about the state of Tennessee
    * **covid-phasing.ipynb** - shows some phasing qualifiers that can be measured by the covid dataset.
    * **covid-over-time.ipynb** - shows timeseries information about the United States as a whole
    * **covid-nc-over-time.ipynb** - shows timeseries information about the state of North Carolina
    * **covid-less-ny.ipynb** - compares the current covid status in different states and vs the US without NY state data. Can edit the list of states (but cannot include NY)
    
3.  Click "Cell" in the menu bar, and "Run All"
4.  Adjust any states in the states_to_watch list in the third cell (for covid.ipynb or covid-less-ny.ipynb).

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jawiv/covid.git/master)

Future enhancements will remove most of this code to make it easier to get straight to the data and see where to alter the list.


Install the qgrid-jupyterlab extension and enable:
`jupyter labextension install qgrid2`
[Github: qgrid](https://github.com/quantopian/qgrid)