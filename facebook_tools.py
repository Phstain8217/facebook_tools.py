import os
import requests

# Function to display the banner
def display_banner():
    banner = """
    =========================================     
╔═══╦╗──╔═══╗╔╗────────
║╔═╗║║──║╔═╗╠╝╚╗───────
║╚═╝║╚═╗║╚══╬╗╔╬══╦╦══╗
║╔══╣╔╗║╚══╗║║║║╔╗╠╣╔╗║
║║──║║║╠╣╚═╝║║╚╣╔╗║║║║║
╚╝──╚╝╚╩╩═══╝╚═╩╝╚╩╩╝╚╝          
    |       THE SYSTEM KILLER BLOOD SECTOR        |
            |   FACEBOOK TOOLS BLOODSECTOR   | ===========================================
    """
    print(banner)

# Function to mass report a Facebook post
def mass_report(post_id, reason):
    url = f"https://graph.facebook.com/v12.0/{post_id}/reports"
    payload = {
        'reason': reason,
        'access_token': 'YOUR_ACCESS_TOKEN'  # Replace with your access token
    }
    response = requests.post(url, data=payload)
    return response.json()

# Function to log Facebook reactions
def log_reactions(post_id):
    url = f"https://graph.facebook.com/v12.0/{post_id}/reactions"
    payload = {
        'access_token': 'YOUR_ACCESS_TOKEN'  # Replace with your access token
    }
    response = requests.get(url, params=payload)
    return response.json()

# Function to share a post
def share_post(post_id):
    url = f"https://graph.facebook.com/v12.0/{post_id}/shares"
    payload = {
        'access_token': 'YOUR_ACCESS_TOKEN',  # Replace with your access token
        'message': 'Check this out!'
    }
    response = requests.post(url, data=payload)
    return response.json()

# Function to enable two-factor authentication
def enable_two_factor_auth(user_id):
    url = f"https://graph.facebook.com/v12.0/{user_id}/two_factor_authentication"
    payload = {
        'access_token': 'YOUR_ACCESS_TOKEN',  # Replace with your access token
        'enabled': True
    }
    response = requests.post(url, data=payload)
    return response.json()

# Main function to run the tools
if __name__ == "__main__":
    display_banner()  # Show the banner

    # Example usage of the functions
    post_id = '1234567890'  # Replace with the actual post ID
    user_id = '0987654321'  # Replace with the actual user ID

    # Mass report
    report_response = mass_report(post_id, 'Spam')
    print("Mass Report Response:", report_response)

    # Log reactions
    reactions = log_reactions(post_id)
    print("Reactions:", reactions)

    # Share post
    share_response = share_post(post_id)
    print("Share Response:", share_response)

    # Enable two-factor authentication
    auth_response = enable_two_factor_auth(user_id)
    print("Two-Factor Authentication Response:", auth_response)