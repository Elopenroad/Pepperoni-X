from quickchart import QuickChart



def voice(online, voiceActive , backgroundcolor):
    qc = QuickChart()
    qc.width = 500
    qc.height = 300
    qc.version = '2'
    qc.background_color = str(backgroundcolor)

    qc.config = {
        "type": "doughnut",
        "data": {
            "datasets": [
                {
                    "data": [online, voiceActive],
                    "backgroundColor": [
                        "rgb(27, 216, 23)",
                        "rgb(9, 239, 184)",
                    ],
                    "label": "Dataset 1",
                },
            ],
            "labels": ["Online", "Voice Active"],
        },
        "options": {
            "title": {
                "display": True,
                "text": "Server Live Analyzing",
                'fontColor': '#000',
            },
                'legend': {
                    'labels': {
                        'fontStyle': 'bold',
                        'fontColor': '#000',
                    }
                    },
            # 'plugins': {
            #     'backgroundImageUrl': 'https://th.bing.com/th/id/R.ed1b6b961ee930d1fc86b0cee37d38c7?rik=%2bLNzFLbqt5uf5g&pid=ImgRaw&r=0',
            # }
        },
    }

    url = qc.get_url()
    return url


# from quickchart import QuickChart

# def voice1(online, voiceActive):
#     qc = QuickChart()
#     qc.width = 500
#     qc.height = 300
#     qc.version = '2'

#     # Convert the parameters to strings and format them in the configuration
#     qc.config = f"""{{
#     type: 'bar',
#     data: {{
#         labels: ['Online', 'Voice Active'],
#         datasets: [
#         {{
#             label: 'Server Live Analyzing',
#             data: [{online}, {voiceActive}],
#             backgroundColor: 'rgba(54, 162, 235, 0.5)',
#             borderColor: 'rgb(54, 162, 235)',
#             borderWidth: 1,
#         }},
#         ],
#     }},
#     options: {{
#         plugins: {{
#         datalabels: {{
#             anchor: 'end',
#             align: 'top',
#             color: '#fff',
#             backgroundColor: 'rgba(34, 139, 34, 0.6)',
#             borderColor: 'rgba(34, 139, 34, 1.0)',
#             borderWidth: 1,
#             borderRadius: 5,
#             formatter: (value) => {{
#             return value ;
#             }},
#         }},
#         }},
#     }},
#     }}"""

#     url = qc.get_url()
#     return url
