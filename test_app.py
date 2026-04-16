import chromedriver_autoinstaller
chromedriver_autoinstaller.install() # This line automatically downloads the correct "keys" for your version of Chrome

from app import app

def test_header_exists(dash_duo):
    # start the app in a testing environment
    dash_duo.start_server(app)
    
    # look for the h1 header tag
    dash_duo.wait_for_element("h1", timeout=10)

def test_visualisation_exists(dash_duo):
    # start the app in a testing environment
    dash_duo.start_server(app)
    
    # look for the graph by its id
    dash_duo.wait_for_element("#sales-line-chart", timeout=10)

def test_region_picker_exists(dash_duo):
    # start the app in a testing environment
    dash_duo.start_server(app)
    
    # look for the radio buttons by their id
    dash_duo.wait_for_element("#region-filter", timeout=10)