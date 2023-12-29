# quickchart-python https://github.com/typpo/quickchart-python

from quickchart import QuickChart

qc = QuickChart()
qc.width = 500
qc.height = 300
qc.version = '2'
qc.background_color = 'rgb(216,211,211)'

qc.config = """{
  "type": "bar",
  "data": {
    "labels": [
      "Saturday",
      "Sunday",
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday"
    ],
    "datasets": [
      {
        "label": "Left",
        "backgroundColor": "#a71d28",
        "borderColor": "rgb(255, 99, 132)",
        "borderWidth": 1,
        "data": [
          -31,
          -70,
          -30,
          -33,
          -9,
          14,
          -41
        ]
      },
      {
        "label": "Join",
        "backgroundColor": "rgb(46,183,31)",
        "borderColor": "rgb(54, 162, 235)",
        "borderWidth": 1,
        "data": [
          73,
          41,
          29,
          61,
          -65,
          59,
          38
        ]
      }
    ]
  },
  "options": {
    "responsive": true,
    "legend": {
      "position": "top"
    },
    "title": {
      "display": true,
      "text": "Weekly report"
    },
    "plugins": {
      "roundedBars": true 
    }
  }
}"""

# You can get the chart URL...
print(qc.get_short_url())
