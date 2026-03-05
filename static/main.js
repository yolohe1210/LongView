window.addEventListener("DOMContentLoaded", () => {
    // pie chart
    const dataTag = document.getElementById("portfolio-data");

    if (dataTag) {
        const portfolioData = JSON.parse(dataTag.textContent);

        const labels = portfolioData.map(a => a.asset);
        const values = portfolioData.map(a => a.current_value);

        const ctx = document.getElementById("allocationChart");

        new Chart(ctx, {
            type: "pie",
            data: {
                labels: labels,
                datasets: [{
                    label: "Current Value",
                    data: values,
                    backgroundColor: [
                        "#5fa8d3", "#62b6cb", "#bee9e8", "#cae9ff", "#1b4965"
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true
            }
        });
    }


    // line chart
    const historyTag = document.getElementById("portfolio-history");
    if (historyTag) {
        const historyData = JSON.parse(historyTag.textContent);
        const trendLabels = historyData.map(a => a.date);
        const trendValues = historyData.map(a => a.value);

        const trendCtx = document.getElementById("profitTrendChart");

        new Chart(trendCtx, {
            type: "line",
            data: {
                labels: trendLabels,
                datasets: [{
                    label: "Portfolio Value",
                    data: trendValues,
                    fill: true,
                    backgroundColor: "rgba(95,168,211,0.2)",
                    borderColor: "#5fa8d3",
                    tension: 0.3
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: false,
                        title: { display: true, text: "Value ($)" }
                    },
                    x: {
                        title: { display: true, text: "Date" }
                    }
                }
            }
        });
    }
});