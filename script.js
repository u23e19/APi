document.addEventListener("DOMContentLoaded", () => {
  const dataContainer = document.getElementById("data-container");

  fetch("http://localhost:5000/api/get_Division") // Replace with your actual API endpoint
    .then((response) => response.json())
    .then((data) => {
      const item = data;
      const card = document.createElement("div");
      card.classList.add("card");
      card.innerHTML = `
    
    <div class="grid-container-division">
        <div class="grid-item-division" id="rawMaterial">
            <p class="key">Raw Material Transport
            <p class="value">${item.Raw_Material_Transport} alerts <i style="text-indent: 60px;"
                    class="fas fa-arrow-right"></i></p>
    
    
    
        </div>
        <div class="grid-item-division" id="health">
            <p class="key">Hearth Layer and Return Fines Handling </p>
            <p class="value">${item.Hearth_Layer_and_Return_Fines_Handling} alerts <i style="text-indent: 60px;"
                    class="fas fa-arrow-right"></i></p>
    
        </div>
        <div class="grid-item-division" id="chilled">
            <p class="key">Chilled Water System</p>
            <p class="value">${item.Chilled_Water_System} alerts <i style="text-indent: 60px;"
                    class="fas fa-arrow-right"></i></p>
    
    
        </div>
        <div class="grid-item-division" id="ignition">
            <p class="key">Ignition Furnace</p>
            <p class="value">${item.Ignition_Furnace} alerts <i style="text-indent: 60px;" class="fas fa-arrow-right"></i>
            </p>
    
    
        </div>
        <div class="grid-item-division" id="mixing">
            <p class="key">Mixing and Nodulizing Plant</p>
            <p class="value">${item.Mixing_and_Nodulizng_Plant} alerts <i style="text-indent: 60px;"
                    class="fas fa-arrow-right"></i></p>
    
    
        </div>
        <div class="grid-item-division" id="dedusting">
            <p class="key">Plant Dedusting</p>
            <p class="value">${item.Plant_Dedusting} alerts <i style="text-indent: 60px;" class="fas fa-arrow-right"></i>
            </p>
    
        </div>
        <div class="grid-item-division" id="fanDucts">
            <p class="key">Process Fans and Ducts</p>
            <p class="value">${item.Process_Fans_and_Ducts} alerts <i style="text-indent: 60px;"
                    class="fas fa-arrow-right"></i></p>
    
        </div>
        <div class="grid-item-division" id="gasDedusting">
            <p class="key">Process Gas Dedusting </p>
            <p class="value">${item.Process_Gas_Dedusting} alerts <i style="text-indent: 60px;"
                    class="fas fa-arrow-right"></i></p>
    
        </div>
    
        <div class="grid-item-division" id="dosing">
            <p class="key">Dosing Plant </p>
            <p class="value">${item.Dosing_Plant} alerts <i style="text-indent: 60px;" class="fas fa-arrow-right"></i></p>
    
        </div>
    
        <div class="grid-item-division" id="sinterCooler">
            <p class="key"> Sinter Cooler </p>
            <p class="value">${item.Sinter_Cooler} alerts <i style="text-indent: 60px;" class="fas fa-arrow-right"></i></p>
    
    
        </div>
        <div class="grid-item-division" id="sinterMachine">
            <p class="key"> Sinter Machine </p>
            <p class="value">${item.Sinter_Machine} alerts <i style="text-indent: 60px;" class="fas fa-arrow-right"></i></p>
    
        </div>
    
        <div class="grid-item-division" id="productHandling">
            <p class="key"> Sinter Product Handling </p>
            <p class="value">${item.Sinter_Product_Handling} alerts <i style="text-indent: 60px;"
                    class="fas fa-arrow-right"></i></p>
    
        </div>
    
        <div class="grid-item-division" id="sinterScreening">
            <p class="key">Sinter Screening </p>
            <p class="value">${item.Sinter_Screening} alerts <i style="text-indent: 60px;" class="fas fa-arrow-right"></i>
            </p>
    
        </div>
    
        <div class="grid-item-division" id="waterSystem">
            <p class="key">Water System </p>
            <p class="value">${item.Water_System} alerts <i style="text-indent: 60px;" class="fas fa-arrow-right"></i></p>
    
        </div>
    </div>
    
    
    `;
      const rawMaterial = card.querySelector("#rawMaterial");
      rawMaterial.addEventListener("click", () => {
        window.location.href = "machineInfo/raw.html";
      });

      const waterSystem = card.querySelector("#waterSystem");
      waterSystem.addEventListener("click", () => {
        window.location.href = "machineInfo/waterSystem.html";
      });

      const sinterScreening = card.querySelector("#sinterScreening");
      sinterScreening.addEventListener("click", () => {
        window.location.href = "machineInfo/sinterScreening.html";
      });

      const productHandling = card.querySelector("#productHandling");
      productHandling.addEventListener("click", () => {
        window.location.href = "machineInfo/productHandling.html";
      });

      const sinterMachine = card.querySelector("#sinterMachine");
      sinterMachine.addEventListener("click", () => {
        window.location.href = "machineInfo/sinterMachine.html";
      });

      const sinterCooler = card.querySelector("#sinterCooler");
      sinterCooler.addEventListener("click", () => {
        window.location.href = "machineInfo/sinterCooler.html";
      });

      const dosing = card.querySelector("#dosing");
      dosing.addEventListener("click", () => {
        window.location.href = "machineInfo/dosing.html";
      });

      const gasDedusting = card.querySelector("#gasDedusting");
      gasDedusting.addEventListener("click", () => {
        window.location.href = "machineInfo/gasDedusting.html";
      });

      const fanDucts = card.querySelector("#fanDucts");
      fanDucts.addEventListener("click", () => {
        window.location.href = "machineInfo/fanDucts.html";
      });

      const dedusting = card.querySelector("#dedusting");
      dedusting.addEventListener("click", () => {
        window.location.href = "machineInfo/dedusting.html";
      });

      const mixing = card.querySelector("#mixing");
      mixing.addEventListener("click", () => {
        window.location.href = "machineInfo/mixing.html";
      });

      const chilled = card.querySelector("#chilled");
      chilled.addEventListener("click", () => {
        window.location.href = "machineInfo/chilled.html";
      });

      const ignition = card.querySelector("#ignition");
      ignition.addEventListener("click", () => {
        window.location.href = "machineInfo/ignition.html";
      });

      const health = card.querySelector("#health");
      health.addEventListener("click", () => {
        window.location.href = "machineInfo/health.html";
      });

      // Append the card to the data container
      dataContainer.appendChild(card);
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
});

// const button1 = document.getElementById('button1');

// button1.addEventListener('click', () => {

// window.location.href = 'machineInfo/raw.html';
// });
// const button2 = document.getElementById('button2');

// button2.addEventListener('click', () => {

// window.location.href = 'machineInfo/dosing.html';
// });

// document.addEventListener('DOMContentLoaded', () => {
// const dataContainer = document.getElementById('data-container');

// // Fetch data from Flask API
// fetch('http://localhost:5000/api/get_Division') // Replace with your actual API endpoint
// .then(response => response.json())
// .then(data => {
// // Loop through the data and create individual cards
// for (const key in data) {
// if (data.hasOwnProperty(key)) {
// const value = data[key];
// const card = document.createElement('div');
// card.classList.add('card');
// card.innerHTML = `
// <p class="key">${key}</p>
// <p class="value">${value} alerts</p>

// `;
// dataContainer.appendChild(card);
// }
// }
// console.log("print", data.Raw_Material_Transport)

// })
// .catch(error => {
// console.error('Error fetching data:', error);
// });
// });
