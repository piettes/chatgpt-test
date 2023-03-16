// Fetch data from endpoint
// fetch('/data')
//   .then(response => response.json())
//   .then(data => {
//     // Data points
//     const chartData = {
//       labels: data.labels,
//       datasets: [{
//         label: 'Website visitors',
//         data: data.values,
//         backgroundColor: 'rgba(76, 175, 80, 0.2)', // Green color value from logo
//         borderColor: 'rgba(76, 175, 80, 1)', // Use the same color for the border
//         borderWidth: 1
//       }]
//     };
//
//     // Chart options
//     const options = {
//       scales: {
//         y: {
//           beginAtZero: true
//         }
//       }
//     };
//
//     // Render the chart
//     const ctx = document.getElementById('myChart').getContext('2d');
//     const myChart = new Chart(ctx, {
//       type: 'bar',
//       data: chartData,
//       options: options
//     });
//

fetch('/points')
  .then(response => response.json())
  .then(data => {
    // extract the labels and values from the data
    const labels = data.data.map(point => point.label);
    const values = data.data.map(point => point.value);

    // create the chart
    const ctx = document.getElementById('myChart').getContext('2d');
    const chart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: 'Values',
          data: values,
          backgroundColor: 'rgba(54, 162, 235, 0.5)',
          borderColor: 'rgba(54, 162, 235, 1)',
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          yAxes: [{
            ticks: {
              beginAtZero: true
            }
          }]
        },
        tooltips: {
          callbacks: {
            label: function (tooltipItem, data) {
              const point = data.datasets[tooltipItem.datasetIndex].data[tooltipItem.index];
              return data.datasets[tooltipItem.datasetIndex].label + ': ' + point + '\nShort description: ' + data.data[tooltipItem.index].short_desc + '\nLong description: ' + data.data[tooltipItem.index].long_desc;
            }
          }
        }
      }
    });

    const descriptions = data.data;

    // data.data.forEach(point => {
    //   const card = document.createElement('div');
    //   card.classList.add('card', 'm-2');
    //
    //   const cardImg = document.createElement('img');
    //   cardImg.src = `https://via.placeholder.com/150x${point.value}/000000/FFFFFF/?text=${point.label}`;
    //   cardImg.alt = point.label;
    //   cardImg.classList.add('card-img-top');
    //
    //   const cardBody = document.createElement('div');
    //   cardBody.classList.add('card-body');
    //
    //   const cardTitle = document.createElement('h5');
    //   cardTitle.classList.add('card-title');
    //   cardTitle.textContent = point.label;
    //
    //   const cardText = document.createElement('p');
    //   cardText.classList.add('card-text');
    //   cardText.textContent = point.short_desc;
    //
    //   cardBody.appendChild(cardTitle);
    //   cardBody.appendChild(cardText);
    //   card.appendChild(cardImg);
    //   card.appendChild(cardBody);
    //
    //   document.getElementById('description').appendChild(card);
    //   // cardsContainer.appendChild(card);
    // });


    const row = document.createElement('div');
    row.classList.add('row');
    data.data.forEach(point => {
      const col = document.createElement('div');
      col.classList.add('col-md-3', 'mb-4');

      const card = document.createElement('div');
      card.classList.add('card');

      const cardImg = document.createElement('img');
      cardImg.src = `https://via.placeholder.com/200x200/000000/FFFFFF/?text=${point.label}`;
      cardImg.alt = point.label;
      cardImg.classList.add('card-img-top');
      cardImg.style.height = '200px';
      cardImg.style.width = '200px';

      const cardBody = document.createElement('div');
      cardBody.classList.add('card-body');

      const cardTitle = document.createElement('h5');
      cardTitle.classList.add('card-title');
      cardTitle.textContent = point.label;

      const cardText = document.createElement('p');
      cardText.classList.add('card-text');
      cardText.textContent = point.short_desc;

      cardBody.appendChild(cardTitle);
      cardBody.appendChild(cardText);
      card.appendChild(cardImg);
      card.appendChild(cardBody);
      col.appendChild(card);
      row.appendChild(col);
    });
    document.getElementById('description').appendChild(row);



    // // Create the list of descriptions as HTML
    // const ul = document.createElement('ul');
    // ul.classList.add('list-group');
    // for (let i = 0; i < descriptions.length; i++) {
    //   const li = document.createElement('li');
    //   li.textContent = descriptions[i].label;
    //   li.classList.add('list-group-item');
    //
    //   // Create a card for the list item
    //   const card = document.createElement('div');
    //   card.classList.add('card');
    //   const cardBody = document.createElement('div');
    //   cardBody.classList.add('card-body');
    //   cardBody.textContent = descriptions[i].long_desc;
    //   //cardBody.appendChild(li);
    //   card.appendChild(cardBody);
    //
    //   // Append the card to the list item
    //   li.appendChild(card);
    //   ul.appendChild(li);
    // }

    // document.getElementById('description').appendChild(ul);

  })
  .catch(error => console.error(error));