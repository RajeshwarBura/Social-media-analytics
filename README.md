# Social-media-analytics
# Social Media Performance Analysis

## Objective

This project aims to build a basic analytics module to analyze engagement data from mock social media accounts. It utilizes **Langflow** for workflow creation and GPT integration and **DataStax Astra DB** for database operations.

---

## Features

1. **Fetch Engagement Data**  
   - Simulate a dataset containing social media engagement metrics (e.g., likes, shares, comments) across different post types (carousel, reels, static images).  
   - Store the dataset in **DataStax Astra DB**.

2. **Analyze Post Performance**  
   - Create a Langflow workflow to:
     - Accept post types as input.
     - Query the Astra DB dataset to calculate average engagement metrics for each post type.

3. **Generate Insights**  
   - Use GPT integration in Langflow to derive simple, actionable insights from the data, such as:  
     - "Carousel posts have 20% higher engagement than static posts."  
     - "Reels drive 2x more comments compared to other formats."

---

## Tools and Technologies

1. **Langflow**  
   - Workflow creation and GPT-based insights generation.  
   - Enables a no-code/low-code environment for defining data flows.  

2. **DataStax Astra DB**  
   - A fully managed Cassandra-as-a-Service database for storing and querying engagement data.

---

## Prerequisites

1. **Langflow**  
   - Install Langflow from [Langflow's GitHub repository](https://github.com/logspace-ai/langflow).

2. **DataStax Astra DB**  
   - Create an account at [DataStax Astra](https://www.datastax.com/products/datastax-astra).  
   - Set up a free-tier database and obtain credentials.  

3. **Python Requirements**  
   - Install required Python packages:  
     ```bash
     pip install cassandra-driver langflow openai
     ```

---

## Setup and Usage

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/social-media-performance-analysis.git
cd social-media-performance-analysis
```

### 2. Configure Astra DB
- Download your **Astra DB Secure Connect Bundle** from the Astra DB dashboard.  
- Place it in the project root directory and rename it to `secure-connect-database.zip`.

### 3. Simulate Engagement Data
- Run the `data_loader.py` script to generate and upload mock engagement data into your Astra DB:
  ```bash
  python data_loader.py
  ```

### 4. Build Workflow in Langflow
- Launch Langflow:
  ```bash
  langflow
  ```
- Open Langflow in your browser and:
  1. Define inputs for the workflow (post types).  
  2. Add a custom node for querying Astra DB.  
  3. Use GPT integration to process the query results and generate insights.  
  4. Save and test the flow.

### 5. Analyze Data
- Input post types into the Langflow workflow and view the performance metrics and generated insights.

---

## Example Dataset

| Post Type      | Likes | Shares | Comments | Total Engagement |
|----------------|-------|--------|----------|------------------|
| Carousel       | 150   | 30     | 20       | 200              |
| Reels          | 250   | 50     | 60       | 360              |
| Static Images  | 100   | 15     | 10       | 125              |

---

## Example Outputs

1. **Performance Metrics**  
   - Average likes for carousel posts: 150  
   - Average comments for reels: 60  

2. **Insights**  
   - "Carousel posts have 20% higher engagement than static posts."  
   - "Reels drive 2x more comments compared to other formats."  

---

## Contributing

Contributions are welcome! Please submit a pull request or open an issue if you have suggestions or improvements.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

- **Langflow**: For enabling intuitive workflow creation.  
- **DataStax Astra DB**: For providing a reliable database solution.  
- **OpenAI**: For GPT integration and generating meaningful insights.
