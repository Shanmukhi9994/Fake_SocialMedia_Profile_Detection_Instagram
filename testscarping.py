import instaloader

# Create an instance of Instaloader
L = instaloader.Instaloader()

# Optionally, login to Instagram if you need access to private profiles or additional features
# L.interactive_login("your_username")

# Fetch a profile by username
profile = instaloader.Profile.from_username(L.context, 'srkr_cine_club')

# Iterate over the profile's posts and extract desired information
for post in profile.get_posts():
    # Extract post details
    post_details = {
        'shortcode': post.shortcode,
        'url': post.url,
        'caption': post.caption,
        'likes': post.likes,
        'comments': post.comments,
        'timestamp': post.date_utc,
        'bio': profile.biography,

    }
    print(post_details)

# You can also fetch a specific post by its shortcode
# post = instaloader.Post.from_shortcode(L.context, 'shortcode')