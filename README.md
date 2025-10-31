### Weather Data Analysis Project
#### Project Overview

This project retrieves current weather data for multiple cities using the OpenWeatherMap API, stores the data in an SQLite database, and performs analysis to identify patterns and trends in temperature, humidity, and weather conditions across different cities. Visualizations are also included to provide insights at a glance.

#### Features

- Fetch weather data for multiple cities from OpenWeatherMap API.
- Store the data in a well-structured SQLite database.
- Perform data analysis:
- City-wise temperature and humidity comparisons.
- Filtering and sorting cities based on temperature and humidity thresholds.
- Grouping cities by weather conditions.
- Calculating statistical insights like average, highest, and lowest temperature/humidity.
- Visualize results using Matplotlib and Seaborn.

#### Project Structure
```
weather_sql_project/
├── data/
│   └── weather.db             # SQLite database storing weather data
├── fetch_weather.py           # Script to fetch data from OpenWeatherMap API
├── database_manager.py        # Functions for creating table, inserting, updating, deleting records
├── analysis.py                # Functions for data analysis and visualization
├── main.ipynb                 # Main script to run the project                   # File storing your API key
├── requirements.txt           # Python dependencies
└── README.md 
```

#### Setup Instructions

##### Clone the repository:
- git clone <your-repo-url>
- cd weather_sql_project
##### Install dependencies:
- pip install -r requirements.txt
- Set up your OpenWeatherMap API key:
- API_KEY=your_openweathermap_api_key
- Run the project:
- python main.py
##### This will:
- Fetch weather data for the predefined cities.
- Insert the data into weather.db.
- Perform analysis and display visualizations.