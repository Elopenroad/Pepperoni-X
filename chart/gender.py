from quickchart import QuickChart

def gender(male, female, lgbt):
    qc = QuickChart()
    qc.width = 500
    qc.height = 300
    qc.version = '2'
    
    # Use f-strings to format the parameters in the datasets list
    qc.config = f"""
    {{
        type: 'pie',
        data: {{
            datasets: [
                {{
                    data: [{male}, {female}, {lgbt}],
                    backgroundColor: [
                        'rgb(0, 0, 255)',
                        'rgb(228, 0, 124)',
                        'rgb(128, 0, 128)',
                    ],
                    label: 'Dataset 1',
                }},
            ],
            labels: ['Male-{male}', 'Female-{female}', 'Custom-{lgbt}'],
        }},
        options: {{
            legend: {{
                labels: {{
                    fontSize: 10,
                    fontStyle: 'bold',
                    fontColor: '#000',
                }},
            }},
            title: {{
                display: true,
                text: ' Gender Challenge',
                fontSize: 20,
                fontColor: '#000',
            }},
        }},
    }}
    """

    # You can get the chart URL...
    url = qc.get_url()
    return url



gender(male=12 , female=20 , lgbt=23)