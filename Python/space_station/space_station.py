import pandas as pd 
import plotly.express as xp
import requests
from requests.exceptions import HTTPError
import time

def main(method, period, sleep, output):
    ''' Track the position of the International Space Stationa and plot it on a map. '''
    # TO DO: Optional saving DataFrame to csv file,
    #        Print out location of ISS when using 'oneshot'.
    
    df = pd.DataFrame(columns = ["timestamp", "latitude", "longitude"])
    if method == 'oneshot':
        pos = check_iss()
        pos.to_csv('iss_location.csv', mode = 'a', header = False)
        plot_pos(pos,output = output)
        
    else:
        start_time = time.time()
        while(time.time() - start_time <= period):
            df = pd.concat([df,check_iss()], ignore_index = True)
            time.sleep(sleep)
        
        df.to_csv('iss_location.csv', mode = 'a', header = False)
        plot_pos(df, output = output)
        
# Get request
def get_request():
    ''' Requesting data from the Open Notify API'''
    
    url = "http://api.open-notify.org/iss-now.json"

    try:
        response = requests.get(url)    
        # Check the status of the reponse, if succesful no Exception will be raised.
        response.raise_for_status()

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return None

    except Exception as err:
        print(f'An error as occurred: {err}')
        return None

    else:
        #print("Succesful data retrieval of API.")
        return response.json()



def check_iss():
    ''' Put the JSON data from the request in a Pandas DataFrame and return it.'''
    
    js = get_request()

    if js:
        return pd.DataFrame([[pd.to_datetime(js["timestamp"], unit = 's'),
                            js["iss_position"]["latitude"],
                            js["iss_position"]["longitude"]]],
                        columns = ["timestamp", "latitude", "longitude"])
        
    else:
        # Try again, should have got an error message already from get_request()
        check_iss()

    
def plot_pos(df, output):
    ''' Plots the position of the ISS on a map of the Earth.
        Saving the interactive figure to an HTML file.
        TO DO: make saving it optional.'''
    
    fig = xp.scatter_geo(df, lat = 'latitude', lon = 'longitude',
                    hover_name = 'timestamp',
                    projection = 'natural earth')
    fig.update_layout(title_text=f"Tracking of the International Space Station.",
                      title_font_size=30,
                      title_x = 0.5,
                      title_xanchor = 'center')
    fig.write_html(f'{output}.html')
    fig.show()
    

if __name__ == '__main__':
    
    import argparse
    
    msg = 'Tracking the International Space Station using Open Notify'
    parser = argparse.ArgumentParser(description = msg, prog = 'space_station.py')
    
    parser.add_argument('-m', '--method', nargs = '?', default = 'tracking', choices = ['tracking', 'oneshot'], type = str,
                       help = '''What method to use. 
                       tracking: gives the position of the ISS during a period of time, depending on the "period" and "sleep" parameters.
                       oneshot: returns the current location of the ISS. Default = %(default)s''')
    parser.add_argument('-p', '--period', nargs = '?', default = 1200, type = int,
                       help = 'How long to keep track of the ISS in seconds. Default = %(default)s')
    parser.add_argument('-s', '--sleep', nargs = '?', default = 60, type = int,
                       help = 'Time between position tracking during given period of time in seconds. Default = %(default)s')
    parser.add_argument('-o', '--output', nargs = '?', default = 'ISS_tracking', type = str,
                       help = 'Name for the HTML file. Default = %(default)s')
    parser.add_argument('--version', action = 'version', version = '%(prog)s 0.0')
    
    args = parser.parse_args()

    main(method = args.method, period = args.period, sleep = args.sleep, output = args.output)
