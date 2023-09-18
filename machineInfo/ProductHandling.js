
const button2 = document.getElementById("button2");
button2.addEventListener("click", () => {
  window.location.href = "../index.html";
});


document.addEventListener("DOMContentLoaded", () => {
  const dataContainer = document.getElementById("data-container-high");

  fetch("http://127.0.0.1:5000/api/get_SinterProductHandling")
    .then((response) => response.json())
    .then((data) => {
      console.log("High", data.High.length);
      const count= data.High.length
      const countDisplayHigh = document.getElementById("countDisplayHigh");

      if (countDisplayHigh) {
        countDisplayHigh.textContent = `High Health Score (${count})`;
      } else {
        console.error("Element with id 'countDisplay' not found.");
      }
      if (count === 0) {
        const noDataDiv = document.createElement("div");
        noDataDiv.classList.add("no-data-message");
        noDataDiv.textContent = "No data available";
        dataContainer.appendChild(noDataDiv);
      } else {
      data.High.forEach((item) => {
        const div = document.createElement("div");
        div.classList.add("data-item");
        // Generate a unique ID for each pie chart container
        const pieChartContainerId = `pieChartContainer_${item.MachineNo}`;
        div.innerHTML = `
          <div class="machine-grid">
          <div class="machine-grid-item"> <p class="machine">${item.MachineNo}</p></div>
          <div class="machine-grid-item"><p id="${pieChartContainerId}"></p> </div>
          <div class="machine-grid-item"><p class="type">${item.MachineType}</p></div>  
          <div class="machine-grid-item"></div>
          <div class="machine-grid-item">
          <p class="count"><i class="fas fa-exclamation-triangle"></i> ${item.AlertCount} alerts</p>
          </div>
         <div class="machine-grid-item">
         <strong class="strong">${item.HealthScore}%</strong> 
          </div>
        </div>
        `;
        dataContainer.appendChild(div);
        // Create and render the pie chart in the respective container
        const color = "#00df59"; // Replace with your desired color value
        const small_pie_fig = {
          data: [
            {
              type: "pie",
              labels: ["", ""],
              values: [item.HealthScore, 100 - item.HealthScore],
              hole: 0.85,
              textinfo: "none",
              marker: {
                colors: [color, "rgb(240,240,240)"],
              },
            },
          ],
          layout: {
            showlegend: false,
            width: 25,
            height: 25,
            margin: {
              l: 0,
              r: 0,
              b: 0,
              t: 0,
              pad: 0,
            },
          },
        };
        const container = document.getElementById(pieChartContainerId);
        Plotly.newPlot(container, small_pie_fig);
      });
   } })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
});


document.addEventListener("DOMContentLoaded", () => {
  const dataContainer = document.getElementById("data-container-medium");

  fetch("http://127.0.0.1:5000/api/get_SinterProductHandling")
    .then((response) => response.json())
    .then((data) => {
      console.log("Med", data.Med.length);
      const count= data.Med.length
      const countDisplayMed = document.getElementById("countDisplayMed");

      if (countDisplayMed) {
        countDisplayMed.textContent = `Medium Health Score (${count})`;
      } else {
        console.error("Element with id 'countDisplay' not found.");
      }
      if (count === 0) {
        const noDataDiv = document.createElement("div");
        noDataDiv.classList.add("no-data-message");
        noDataDiv.textContent = "No data available";
        dataContainer.appendChild(noDataDiv);
      } else {
      data.Med.forEach((item) => {
        const div = document.createElement("div");
        div.classList.add("data-item");
        // Generate a unique ID for each pie chart container
        const pieChartContainerIdMed = `pieChartContainer_${item.MachineNo}`;
        div.innerHTML = `
          <div class="machine-grid">
          <div class="machine-grid-item"> <p class="machine">${item.MachineNo}</p></div>
          <div class="machine-grid-item"><p id="${pieChartContainerIdMed}"></p> </div>
          <div class="machine-grid-item"><p class="type">${item.MachineType}</p></div>  
          <div class="machine-grid-item"></div>
          <div class="machine-grid-item">
          <p class="count"><i class="fas fa-exclamation-triangle"></i> ${item.AlertCount} alerts</p>
          </div>
         <div class="machine-grid-item">
         <strong class="strong">${item.HealthScore}%</strong> 
          </div>
        </div>
        `;
        dataContainer.appendChild(div);
        // Create and render the pie chart in the respective container
        const color = "#feb308"; // Replace with your desired color value
        const small_pie_fig_Med = {
          data: [
            {
              type: "pie",
              labels: ["", ""],
              values: [item.HealthScore, 100 - item.HealthScore],
              hole: 0.85,
              textinfo: "none",
              marker: {
                colors: [color, "rgb(240,240,240)"],
              },
            },
          ],
          layout: {
            showlegend: false,
            width: 25,
            height: 25,
            margin: {
              l: 0,
              r: 0,
              b: 0,
              t: 0,
              pad: 0,
            },
          },
        };
        const container = document.getElementById(pieChartContainerIdMed);
        Plotly.newPlot(container, small_pie_fig_Med);
      });
    }
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
});


document.addEventListener("DOMContentLoaded", () => {
  const dataContainer = document.getElementById("data-container-low");

  fetch("http://127.0.0.1:5000/api/get_SinterProductHandling")
    .then((response) => response.json())
    .then((data) => {
      console.log("Low", data.Low.length);
      const count= data.Low.length
      const countDisplayLow = document.getElementById("countDisplayLow");

      if (countDisplayLow) {
        countDisplayLow.textContent = `Low Health Score (${count})`;
      } else {
        console.error("Element with id 'countDisplay' not found.");
      }
      if (count === 0) {
        const noDataDiv = document.createElement("div");
        noDataDiv.classList.add("no-data-message");
        noDataDiv.textContent = "No data available";
        dataContainer.appendChild(noDataDiv);
      } else {
      data.Low.forEach((item) => {
        const div = document.createElement("div");
        div.classList.add("data-item");
        // Generate a unique ID for each pie chart container
        const pieChartContainerIdLow = `pieChartContainer_${item.MachineNo}`;
        div.innerHTML = `
          <div class="machine-grid">
          <div class="machine-grid-item"> <p class="machine">${item.MachineNo}</p></div>
          <div class="machine-grid-item"><p id="${pieChartContainerIdLow}"></p> </div>
          <div class="machine-grid-item"><p class="type">${item.MachineType}</p></div>  
          <div class="machine-grid-item"></div>
          <div class="machine-grid-item">
          <p class="count"><i class="fas fa-exclamation-triangle"></i> ${item.AlertCount} alerts</p>
          </div>
         <div class="machine-grid-item">
         <strong class="strong">${item.HealthScore}%</strong> 
          </div>
        </div>
        `;
        dataContainer.appendChild(div);
        // Create and render the pie chart in the respective container
        const color = "#df0000"; // Replace with your desired color value
        const small_pie_fig_low = {
          data: [
            {
              type: "pie",
              labels: ["", ""],
              values: [100 - item.HealthScore,item.HealthScore],
              hole: 0.85,
              textinfo: "none",
              marker: {
                colors: [color, "rgb(240,240,240)"],
              },
            },
          ],
          layout: {
            showlegend: false,
            width: 25,
            height: 25,
            margin: {
              l: 0,
              r: 0,
              b: 0,
              t: 0,
              pad: 0,
            },
          },
        };
        const container = document.getElementById(pieChartContainerIdLow);
        Plotly.newPlot(container, small_pie_fig_low);
      });
   } })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
});
