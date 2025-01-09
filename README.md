
# Polifact Scraper

Polifact Scraper is a command-line tool designed to scrape fact-checking data from the [PolitiFact](https://www.politifact.com/) website. It supports scraping data by speaker, category, and date range, and provides detailed statistics for analysis.

## Features

- **Data Scraping**:
  - Supports filtering by category (e.g., `mostly-true`, `false`, `pants-fire`, etc.).
  - Supports filtering by speaker (e.g., `joe-biden`, `donald-trump`).
  - Automatically handles paginated content.

- **Data Storage**:
  - Save scraped data as a CSV file.
  - Generate statistical reports on the scraped data (e.g., category distribution, time trends).

- **Flexible Usage**:
  - Control behavior through command-line arguments.
  - Customize the output file path.
## Installation

### Clone the Repository

Clone the repository and navigate to the project directory:
```bash
git clone https://github.com/yourusername/polifact-scraper.git
cd polifact-scraper
```
### Install Dependencies

Run the following command to install the required Python libraries:
```bash
pip install -r requirements.txt
```
### Install as a Package (Local Development)
To use the tool as a command-line interface locally, run:
```bash
pip install .
```
## Usage Examples

### Scrape All Categories for a Speaker

Scrape all statements made by `Joe Biden` and save the results to a CSV file:
```bash
polifact -s joe-biden -c all -o ./results.csv
```
Scrape Joe Biden's pants-fire statements:
```bash
polifact -s joe-biden -c pants-fire -o ./pants-fire.csv
```
Enable Statistics
Display statistical information for the scraped data:
```bash
polifact -s joe-biden -c all --stats
```
