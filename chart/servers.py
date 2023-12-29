from quickchart import QuickChart

def server(server_value):
    qc = QuickChart()
    qc.width = 500
    qc.height = 300
    qc.version = '2'

    qc.config = f"""
    {{
        type: 'bar',
        data: {{
            labels: ['servers'],
            datasets: [
                {{
                    label: 'Servers-Log',
                    data: [{server_value}],
                    backgroundColor: 'rgba(54, 162, 235, 0.5)',
                    borderColor: 'rgb(54, 162, 235)',
                    borderWidth: 1,
                }},
            ],
        }},
        options: {{
            plugins: {{
                datalabels: {{
                    anchor: 'end',
                    align: 'top',
                    color: '#fff',
                    backgroundColor: 'rgba(34, 139, 34, 0.6)',
                    borderColor: 'rgba(34, 139, 34, 1.0)',
                    borderWidth: 1,
                    borderRadius: 5,
                    formatter: (value) => {{
                        return value;
                    }},
                }},
            }},
        }}
    }}
    """

    url = qc.get_url()
    return url

# Call the server() function with your server parameter
