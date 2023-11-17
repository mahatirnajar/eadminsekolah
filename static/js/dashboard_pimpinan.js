const ctx = document.getElementById("Chart").getContext("2d");
const data = {
  labels: {{labels | safe}},
  datasets: [
    {
      label: "aku",
      backgroundColor: "#0353a4",
      data: [
        9000,
        5000,
        5240,
        3520,
        2510,
        3652,
        4555,
        7850,
        8850,
        4000,
        5000,
        4520,
        4457,
        9200,
        8750,
        9500,
        10000,
        11010,
        11432,
        9850,
        9000,
        5000,
        5240,
        3520,
        2510,
        3652,
        4555,
        7850,
        8850,
        4000,
        5000,
        4520,
        4457,
        9200,
        8750,
        9500,
        10000,
        11010,
        11432,
        9850
      ]
    },
    {
      label: "Short",
      backgroundColor: "#ff8552",
      data: [
        3000,
        4000,
        6000,
        3500,
        3600,
        8060,
        9120,
        8900,
        9300,
        10010,
        9500,
        6300,
        7200,
        3600,
        4600,
        5300,
        5500,
        6900,
        5800,
        4900,
        3000,
        4000,
        6000,
        3500,
        3600,
        8060,
        9120,
        8900,
        9300,
        10010,
        9500,
        6300,
        7200,
        3600,
        4600,
        5300,
        5500,
        6900,
        5800,
        4900
      ]
    },
    {
      label: "Spreading",
      backgroundColor: "#4ecdc4",
      data: [
        6000,
        7200,
        6500,
        4600,
        3600,
        9200,
        8600,
        7500,
        3600,
        5000,
        6050,
        7300,
        6800,
        6900,
        7240,
        9240,
        8640,
        7600,
        6900,
        6750,
        6000,
        7200,
        6500,
        4600,
        3600,
        9200,
        8600,
        7500,
        3600,
        5000,
        6050,
        7300,
        6800,
        6900,
        7240,
        9240,
        8640,
        7600,
        6900,
        6750
      ]
    }
  ]
};

const options = {
  scales: {
    yAxes: [{ stacked: true }],
    xAxes: [
      {
        stacked: true,
        ticks: { maxRotation: 90, minRotation: 90 }
      }
    ]
  }
};

const chart = new Chart(ctx, {
  // The type of chart we want to create
  type: "bar",
  // The data for our dataset
  data: data,
  // Configuration options go here
  options: options
});
