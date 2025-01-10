from astrapy import DataAPIClient

# Initialize the client
client = DataAPIClient("YOUR_TOKEN")
db = client.get_database_by_api_endpoint(
  "https://5448cb8c-5119-4e75-b373-5d766145cfc5-us-east-2.apps.astra.datastax.com",
    keyspace="social_media_analytics",
)
      
print(f"Connected to Astra DB: {db.list_collection_names()}")