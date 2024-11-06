// account_info.js
document.addEventListener('DOMContentLoaded', () => {
    const fileTypeData = JSON.parse('{{ file_counts|safe }}');
    const storageUsed = {{ storage_used }};

    const fileTypeChart = new Chart(document.getElementById('fileTypeChart').getContext('2d'), {
        type: 'pie',
        data: {
            labels: Object.keys(fileTypeData),
            datasets: [{
                data: Object.values(fileTypeData),
                backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56'],
            }]
        },
        options: {
            title: {
                display: true,
                text: 'File Types'
            }
        }
    });

    const storageUsageChart = new Chart(document.getElementById('storageUsageChart').getContext('2d'), {
        type: 'doughnut',
        data: {
            labels: ['Used', 'Free'],
            datasets: [{
                data: [storageUsed, 100 - storageUsed],  // Assuming 100 GB total
                backgroundColor: ['#4BC0C0', '#FF6384'],
            }]
        },
        options: {
            title: {
                display: true,
                text: 'Storage Usage'
            }
        }
    });
});
