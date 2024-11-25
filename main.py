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