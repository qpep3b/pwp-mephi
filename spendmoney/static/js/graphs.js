function buildCompareChart(data) {
    let compareGraphChart = new Chart(document.getElementById('compareGraph'), {
        type: 'bar',
        data: {
            labels: ['Доходы', 'Расходы'],
            datasets: [{
                label: '',
                data: [data.budget, data.expense],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                ],
                borderWidth: 1,
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            },
            plugins: {
                legend: {
                    display: false
                }
            }
        },
    })

    return compareGraphChart
}

function buildPieChart(data, categories) {
    let compareGraphChart = new Chart(document.getElementById('categoriesPie'), {
        type: 'pie',
        data: {
            labels: categories,
            datasets: [{
                label: '',
                data: categories.map(category => data[category]),
                backgroundColor: [
                    'rgba(255,57,69,0.2)',
                    'rgba(255,158,0,0.2)',
                    'rgba(255,255,0,0.2)',
                    'rgba(0,241,0,0.2)',
                    'rgba(0,169,255,0.2)',
                    'rgba(0,0,204,0.2)',
                ],
                hoverOffset: 4,
            }]
        },
    })

    return compareGraphChart
}