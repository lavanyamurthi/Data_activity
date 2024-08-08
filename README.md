# TODO List

## Completed
- Transformed and standardized data from `us_softball_league.tsv` and `unity_golf_club.csv`.
- Combined data from multiple sources into a single dataset.
- Replaced company IDs with names from `companies.csv`.
- Identified and handled suspect records.
- Set up SQLite database and ingested cleaned data.

## Next Steps
1. **Data Validation**: Implement additional validation checks to ensure data consistency and integrity.
2. **Error Handling**: Improve error handling and logging for data processing scripts.
3. **Performance Optimization**: Optimize data processing for large datasets (e.g., batch processing).
4. **Database Enhancements**: 
   - Normalize database schema for better scalability.
   - Consider using PostgreSQL for more advanced features and performance.
5. **Automation**: Automate the entire ETL process using scheduled jobs or data pipelines.
6. **Testing**: Write unit and integration tests for data processing scripts and database interactions.
7. **Documentation**: Improve documentation for each component of the project.

## Remaining Work
- Add additional data validation and error handling.
- Test the ingestion system with larger datasets.
- Refactor code for better readability and maintainability.
- Develop an end-to-end test suite.
- Explore additional features or enhancements based on project requirements.