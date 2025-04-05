$(document).ready(function () {
    const apiUrl = "http://127.0.0.1:5000/api/grouped-fatalities"; // API endpoint for grouped data
    let fatalitiesChart; // Declare chart instance globally to manage updates

    // Fetch data from the API
    function fetchData() {
        $.ajax({
            url: apiUrl,
            method: "GET",
            success: function (data) {
                console.log("Data fetched successfully:", data); // Debugging
                populateTable(data);
                renderChart(data);
            },
            error: function () {
                console.error("Error fetching data");
                displayError("Failed to load data from the server.");
            }
        });
    }

    // Populate the table with data
    function populateTable(data) {
        const tableBody = $("#fatalitiesTable tbody");
        tableBody.empty(); // Clear existing rows
        data.forEach((record, index) => {
            const row = `
                <tr>
                    <td>${index + 1}</td>
                    <td>${record.Year}</td>
                    <td>${record.Month}</td>
                    <td>${record.Fatalities}</td>
                </tr>
            `;
            tableBody.append(row);
        });
    }

    // Display error messages to the user
    function displayError(message) {
        const errorDiv = $("#errorMessage");
        errorDiv.text(message).show(); // Show error message
    }

    // Render the chart using Chart.js
    function renderChart(data) {
        const ctx = document.getElementById("fatalitiesChart").getContext("2d");

        // Prepare data for the chart
        const labels = data.map(record => `${record.Month} ${record.Year}`);
        const fatalities = data.map(record => record.Fatalities);

        // Clear the existing chart if it exists
        if (fatalitiesChart) {
            fatalitiesChart.destroy();
        }

        // Create a new chart instance
        fatalitiesChart = new Chart(ctx, {
            type: "line",
            data: {
                labels: labels,
                datasets: [{
                    label: "Monthly Fatalities",
                    data: fatalities,
                    borderColor: "rgba(75, 192, 192, 1)",
                    backgroundColor: "rgba(75, 192, 192, 0.2)",
                    borderWidth: 2,
                    fill: true
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        display: true,
                        position: "top"
                    }
                },
                scales: {
                    x: {
                        title: {
                            display: true,
                            text: "Month"
                        }
                    },
                    y: {
                        title: {
                            display: true,
                            text: "Fatalities"
                        },
                        beginAtZero: true
                    }
                }
            }
        });
    }

    // Fetch data on page load
    fetchData();
});
