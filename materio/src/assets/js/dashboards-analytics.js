/* jshint esversion: 11 */
/**
 * Dashboard Analytics
 */

'use strict';

(function () {
  let cardColor, labelColor, borderColor, chartBgColor;

  cardColor = config.colors.cardColor;
  labelColor = config.colors.textMuted;
  borderColor = config.colors.borderColor;
  chartBgColor = config.colors.chartBgColor;

  document.addEventListener('DOMContentLoaded', function () {
    // ✅ FIXED: Get canvas context
    const ctx = document.getElementById('weeklyOverviewChart')?.getContext('2d');

    // ✅ Only proceed if canvas exists
    if (ctx) {
      const labelData = JSON.parse(document.getElementById('collegeLabels').textContent);
      const dataData = JSON.parse(document.getElementById('collegeData').textContent);

      new Chart(ctx, {
        type: 'bar',
        data: {
          labels: labelData,
          datasets: [{
            label: 'Students',
            data: dataData,
            backgroundColor: config.colors.primary,
            borderRadius: {
              topLeft: 8,
              topRight: 8
            },
            barPercentage: 0.5,
            categoryPercentage: 0.7
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              display: false
            },
            tooltip: {
              callbacks: {
                label: function (context) {
                  return context.raw + ' students';
                }
              }
            }
          },
          scales: {
            x: {
              ticks: {
                color: labelColor,
                font: { size: 13, family: 'Inter' }
              },
              grid: {
                display: false,
                drawBorder: false,
                drawTicks: false
              }
            },
            y: {
              beginAtZero: true,
              ticks: {
                stepSize: 10,
                color: labelColor,
                font: { size: 13, family: 'Inter' }
              },
              grid: {
                borderDash: [8],
                color: borderColor
              }
            }
          }
        }
      });
    }

    // ✅ Sessions Chart logic (unchanged below)
  
    // Sessions Column Chart
    // --------------------------------------------------------------------
    const sessionsColumnChartEl = document.querySelector('#sessionsColumnChart');
    const sessionsColumnChartConfig = {
      chart: {
        height: 90,
        parentHeightOffset: 0,
        type: 'bar',
        toolbar: {
          show: false
        }
      },
      tooltip: {
        enabled: false
      },
      plotOptions: {
        bar: {
          barHeight: '100%',
          columnWidth: '20px',
          startingShape: 'rounded',
          endingShape: 'rounded',
          borderRadius: 4,
          colors: {
            ranges: [
              {
                from: 25,
                to: 32,
                color: config.colors.danger
              },
              {
                from: 60,
                to: 75,
                color: config.colors.primary
              },
              {
                from: 45,
                to: 50,
                color: config.colors.danger
              },
              {
                from: 35,
                to: 42,
                color: config.colors.primary
              }
            ],
            backgroundBarColors: [chartBgColor, chartBgColor, chartBgColor, chartBgColor, chartBgColor],
            backgroundBarRadius: 4
          }
        }
      },
      grid: {
        show: false,
        padding: {
          top: -10,
          left: -10,
          bottom: -15
        }
      },
      dataLabels: {
        enabled: false
      },
      legend: {
        show: false
      },
      xaxis: {
        labels: {
          show: false
        },
        axisTicks: {
          show: false
        },
        axisBorder: {
          show: false
        }
      },
      yaxis: {
        labels: {
          show: false
        }
      },
      series: [
        {
          data: [30, 70, 50, 40, 60]
        }
      ],
      responsive: [
        {
          breakpoint: 1350,
          options: {
            chart: {
              height: 80
            },
            plotOptions: {
              bar: {
                columnWidth: '40%'
              }
            }
          }
        },
        {
          breakpoint: 1200,
          options: {
            chart: {
              height: 100
            },
            plotOptions: {
              bar: {
                columnWidth: '20%'
              }
            }
          }
        },
        {
          breakpoint: 768,
          options: {
            chart: {
              height: 110
            },
            plotOptions: {
              bar: {
                columnWidth: '10%'
              }
            }
          }
        },
        {
          breakpoint: 480,
          options: {
            plotOptions: {
              bar: {
                columnWidth: '20%'
              }
            }
          }
        }
      ]
    };

    if (typeof sessionsColumnChartEl !== 'undefined' && sessionsColumnChartEl !== null) {
      const sessionsColumnChart = new ApexCharts(sessionsColumnChartEl, sessionsColumnChartConfig);
      sessionsColumnChart.render();
    }
  });
})();
