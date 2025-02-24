# Fake Reviews Generator with Apache Airflow

This project is designed to generate fake reviews using **Apache Airflow** and store metadata in a **PostgreSQL** backend. The pipeline utilizes dynamic Directed Acyclic Graphs (DAGs) to create fake reviews either from neutral starting prompts or by specifying keywords for more targeted reviews. The generated reviews are then cleaned, classified, and evaluated for authenticity.

### Key Features

- **Dynamic Task Flow**:  
  The DAG dynamically determines the task flow based on input. It branches into two workflows:
  - **Generate Starting Prompts**: Creates neutral prompts to serve as seed content for fake reviews.
  - **Generate Review by Keyword**: If a keyword is provided, the system generates reviews based on that keyword.

- **Fake Review Generation**:  
  - **Starting Prompts Generation**: Generates a set number (e.g., 100) of neutral prompts for use in creating fake reviews.
  - **Fake Review Creation**: The system uses these prompts to generate reviews. If a keyword is specified, reviews are generated around the keyword (e.g., "product").

- **Post-Processing**:  
  After the reviews are generated, they undergo a cleaning process to ensure they are concise, with a maximum of three sentences.

- **Fake Review Detection**:  
  The reviews are classified as either fake or genuine using a pre-defined detection model.

### Workflow Steps

1. **Task Selection**:  
   The workflow begins by checking if a **keyword** is provided. If so, it generates reviews based on the keyword. If not, it defaults to generating neutral starting prompts.

2. **Starting Prompts Generation**:  
   The system generates a set number (default: 100) of neutral starting prompts that will serve as the foundation for generating fake reviews.

3. **Review Creation**:  
   Using the generated prompts, fake reviews are created. If a keyword is provided, reviews are generated specifically for that keyword.

4. **Review Cleaning**:  
   The generated reviews are cleaned to remove extraneous content, ensuring that each review is concise and limited to 3 sentences.

5. **Fake Review Detection**:  
   The cleaned reviews are analyzed and classified as either fake or genuine based on a detection model.

### Dependencies

The project uses the following Python libraries:

- **Apache Airflow**: For orchestrating the workflow.
- **Custom Python Functions**: For generating prompts, creating reviews, cleaning reviews, and detecting fake reviews.

---

## Airflow Docker Setup

### Prerequisites

Ensure that you have the following tools installed:

- **Docker**: [Download Docker](https://www.docker.com/get-started)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)

### Setup

1. **Clone the repository** to your local machine:

   ```bash
   git clone https://github.com/manal-herradi/fake_reviews_generator.git
   cd fake_reviews_generator
   ```

### Services Overview

- **PostgreSQL**: Stores Airflow metadata.
- **Airflow Webserver**: Provides a web UI for monitoring and managing workflows (accessible via port `5500`).
- **Airflow Scheduler**: Schedules and executes Airflow tasks.

### Running the Setup

1. **Start the containers**:

   ```bash
   docker-compose up -d
   ```

   This command starts all the necessary services in detached mode.

2. **Access the Airflow Web UI**:

   Open your browser and navigate to [http://localhost:5500](http://localhost:5500).  
   Login with the credentials:
   - **Username**: admin
   - **Password**: admin123

3. **Running DAGs**:

   You can trigger DAGs manually via the Airflow Web UI by selecting the DAG you want to run and clicking "Trigger DAG".

4. **Stopping the containers**:

   To stop the services, run:

   ```bash
   docker-compose down
   ```
