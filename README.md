# Road Safety Analysis Project

## Overview

This project aims to analyze road deaths in Ireland over the past five years, assessing monthly trends to determine whether fatalities have increased or decreased. The program also investigates correlations between road safety campaigns and reductions in road deaths. Users can update or delete data via the API, ensuring a dynamic and user-friendly experience.

## Author

- Name: Edward Cronin
- Student ID: g00425645
- Email: g00425645@atu.ie

## Table of Contents

[Overview](#overview)
[Author](#author)
[Features](#features)
[Technical Stack](#technical-stack)
[Implementation Steps](#implementation-steps)
[Pre-Requisites](#prerequisites)
[How to Download this Repository](#how-to-download-this-repository)
[Code of Conduct](#code-of-conduct)
[Dependencies](#dependencies)
[Data Content Relevant To Task](#data-content-relevant-to-task)
[Project Structure](#project-structure)
[Notebooks](#notebooks)
[Licence](#license)
[References](#references)

## Features

- **Data Representation**: Handles data in CSV, XML, and JSON formats.
- **Data Analysis**: Identifies monthly trends in road fatalities over five years and visualizes them with charts.
- **API Integration**: Fetches and interacts with data from the Road Safety Authority of Ireland API.
- **CRUD Functionality**: Allows users to Create, Read, Update, and Delete data directly from the application.
- **Authentication**: Uses OAuth for secure access and data management.
- **Visualization**: Provides user-friendly charts for clear trend analysis.

## Technical Stack

1. **Backend**
   - RESTful API development with Flask.
   - Integration with the Road Safety Authority API for data retrieval and updates.
2. **Frontend**
   - Interactive web interface using jQuery and AJAX.
   - Hosted on a cloud platform
3. **Data Analysis**
   - Data manipulation and analysis with `pandas`.
   - Visualization with `matplotlib` or `seaborn`.
4. **Testing**
   - API testing with Postman or CURL.
5. **Authentication**
   - Secure access using OAuth. (To Be Explored Further!!)

## Implementation Steps

1. **Accessing the API**
   - Retrieve road safety data using HTTP methods (`GET`) via CURL or Postman.
   - Parse data from CSV, XML, or JSON formats for monthly analysis.

2. **Data Analysis**
   - Analyze road deaths for trends using Python libraries.
   - Generate charts and visualizations to highlight changes in road fatalities.

3. **Connecting Campaign Data**
   - Cross-reference road safety campaigns and initiatives for potential correlations.
   - Integrate campaign data into the analysis.

4. **Interactive CRUD Operations**
   - Enable users to update or delete data directly via the API.
   - Develop CRUD functionalities using Flask for the backend.

5. **Frontend Development**
   - Create a user-friendly web interface for data visualization.
   - Use jQuery and AJAX for seamless asynchronous data retrieval.

6. **Deployment**
   - Host the project on ? (To be determindes during project).

7. **Authentication**
   - Implement OAuth for secure and authenticated data access.

## Prerequisites

- **Languages**: Python, JavaScript, HTML, CSS.
- **Tools**: Postman, CURL, Git, Flask.
- **Libraries**: `pandas`, `numpy`, `matplotlib`, `seaborn`, jQuery, AJAX.

## How to Download this Repository

To download this repository, you can use the following command:

```bash
git clone https://github.com/ECronin1973/WSAA-Project
```

## Code of Conduct

Please read the CODE_OF_CONDUCT.md file for details on our code of conduct.

## Dependencies

The dependencies for this project are listed in the requirements.txt file.

## Data Content Relevant To Task

To Be Added

## Project Structure

To Be Added

## Notebooks

To Be Added

## License

This project is licensed under the Apache License 2.0. See the LICENSE file for details.



## References

To be added
