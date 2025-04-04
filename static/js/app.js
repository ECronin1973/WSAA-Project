$(document).ready(function () {
    const apiUrl = "http://127.0.0.1:5000/api/grouped-fatalities"; // API endpoint for grouped data

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
            error: function (error) {
                console.error("Error fetching data:", error); // Debugging
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

    // Render the chart using Chart.js
    function renderChart(data) {
        const ctx = document.getElementById("fatalitiesChart").getContext("2d");

        // Prepare data for the chart
        const labels = data.map(record => `${record.Month} ${record.Year}`);
        const fatalities = data.map(record => record.Fatalities);

        new Chart(ctx, {
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