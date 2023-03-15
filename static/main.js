// Fetch data from endpoint
fetch('/data')
  .then(response => response.json())
  .then(data => {
    // Data points
    const chartData = {
      labels: data.labels,
      datasets: [{
        label: 'Website visitors',
        data: data.values,
        backgroundColor: 'rgba(76, 175, 80, 0.2)', // Green color value from logo
        borderColor: 'rgba(76, 175, 80, 1)', // Use the same color for the border
        borderWidth: 1
      }]
    };

    // Chart options
    const options = {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    };

    // Render the chart
    const ctx = document.getElementById('myChart').getContext('2d');
    const myChart = new Chart(ctx, {
      type: 'bar',
      data: chartData,
      options: options
    });


    const descriptions = data.descriptions;

    // Create the list of descriptions as HTML
    const ul = document.createElement('ul');
    ul.classList.add('list-group');
    for (let i = 0; i < descriptions.length; i++) {
      const li = document.createElement('li');
      li.textContent = descriptions[i];
      li.classList.add('list-group-item');
      
      // Create a card for the list item
      const card = document.createElement('div');
      card.classList.add('card');
      const cardBody = document.createElement('div');
      cardBody.classList.add('card-body');
      //cardBody.appendChild(li);
      card.appendChild(cardBody);

      // Append the card to the list item
      li.appendChild(card);
      ul.appendChild(li);
    }

    document.getElementById('description').appendChild(ul);

  })
  .catch(error => console.error(error));