import webbrowser
# from datetime import datetime
def open_site(site_url):
    try:
        webbrowser.open(site_url)
        return "site successfully opened in browser"
    except Exception as e:
        return e
    
