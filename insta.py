import instaloader

# Create an instance of Instaloader
loader = instaloader.Instaloader()

# Define the profile name you want to scrape
profile_name = 'href_psvk_new_ver'

try:
    # Retrieve the profile metadata
    profile = instaloader.Profile.from_username(loader.context, profile_name)

    # Print basic profile info
    print("Username:", profile.username)
    print("Full Name:", profile.full_name)
    print("Number of Posts:", profile.mediacount)
    print("Number of Followers:", profile.followers)
    print("Number of Followees:", profile.followees)

    # Download profile picture
    loader.download_profile(profile_name, profile_pic_only=True)

    # Retrieve and print posts metadata
    posts = profile.get_posts()
    for post in posts:
        print("\nPost:", post.shortcode)
        print("Likes:", post.likes)
        print("Comments:", post.comments)
        print("Caption:", post.caption)
        print("Post URL:", post.url)
        print("Media URL:", post.url + 'media/')

        # Download the post media
        loader.download_post(post, target=profile_name)

except instaloader.exceptions.ProfileNotExistsException:
    print(f"Profile {profile_name} does not exist.")
except Exception as e:
    print("An error occurred:", str(e))