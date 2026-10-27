"""Build a feed for a community you choose.

See the course lab page for the demonstration checklist.
"""

from lab_classes import User, Tweet


def build_feed():
    lloyd = User("lloyd")
    gameclub = User("gameclub")
    users = [lloyd, gameclub]

    posts = [
        Tweet("gameclub", "Game night starts at seven! #Games #BringSnacks!"),
        Tweet("lloyd", "Bringing a new board game tonight. #Games"),
        Tweet("gameclub", "Update: we are meeting in the lounge."),
    ]

    # Two people follow the club, then one unfollows.
    gameclub.follow()
    gameclub.follow()
    gameclub.unfollow()
    lloyd.follow()

    # Someone likes the announcement, then removes their like.
    posts[0].like()
    posts[0].like()
    posts[0].unlike()
    posts[1].like()

    return users, posts


def main():
    users, posts = build_feed()

    print("ACCOUNTS")
    for user in users:
        print(user)
        print("Followers:", user.followers)

    print("\nPOSTS")
    for post in posts:
        print(post)
        print("Likes:", post.likes)
        print("Hashtags:", post.hashtags())


if __name__ == "__main__":
    main()