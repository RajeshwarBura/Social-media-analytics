from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

def connect_to_astra():
    """
    Connect to Astra DB using the Secure Connect Bundle.

    Returns:
        session: The Cassandra session for querying the database.
    """
    # Path to your secure connect bundle
    SECURE_CONNECT_BUNDLE = "path/to/secure_connect_bundle.zip"

    try:
        # Authentication with the secure connect bundle
        auth_provider = PlainTextAuthProvider(
            username="your-client-id",  # From the secure connect bundle
            password="your-client-secret"  # From the secure connect bundle
        )
        cluster = Cluster(cloud={'secure_connect_bundle': SECURE_CONNECT_BUNDLE}, auth_provider=auth_provider)
        session = cluster.connect()

        print("Connection to Astra DB successful!")
        return session

    except Exception as e:
        print(f"Error connecting to Astra DB: {e}")
        return None


def query_engagement_data(session, post_type):
    """
    Query the database to get average engagement metrics for a given post type.

    Args:
        session: The Cassandra session.
        post_type: The type of post to query (e.g., 'carousel').

    Returns:
        dict: A dictionary with the average metrics.
    """
    try:
        query = f"""
        SELECT AVG(likes) AS avg_likes, AVG(shares) AS avg_shares, AVG(comments) AS avg_comments 
        FROM social_media_analytics.engagement_data 
        WHERE post_type = '{post_type}';
        """
        result = session.execute(query).one()

        if result:
            return {
                "avg_likes": result.avg_likes,
                "avg_shares": result.avg_shares,
                "avg_comments": result.avg_comments
            }
        else:
            return None

    except Exception as e:
        print(f"Error querying engagement data: {e}")
        return None


# Main script
if __name__ == "__main__":
    # Connect to Astra DB
    session = connect_to_astra()

    if session:
        # Set the keyspace (replace 'social_media_analytics' with your actual keyspace name)
        session.set_keyspace('social_media_analytics')

        # Query for a specific post type
        post_type = "carousel"  # Example: 'carousel', 'reel', or 'static_image'
        metrics = query_engagement_data(session, post_type)

        if metrics:
            print(f"Engagement Metrics for {post_type.capitalize()} posts:")
            print(f" - Average Likes: {metrics['avg_likes']}")
            print(f" - Average Shares: {metrics['avg_shares']}")
            print(f" - Average Comments: {metrics['avg_comments']}")
        else:
            print(f"No data found for post type: {post_type}")
