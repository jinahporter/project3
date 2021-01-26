// //RENDER MAPS WITH DB DATA NOT CUSTOMIZED

d3.json("/revenue").then(function (data) {
    var revenueTrace = {
        x: data.country,
        y: data.revenue.map(d => +d),
        type: 'bar'
    }

    var data = [revenueTrace];

    var revenueLayout = {
        title: "Gaming Revenue by Country",
        xaxis: {
            title: "Country",
            automargin: true
        },
        yaxis: {
            title: "Revenue (USD)"
        },
        plot_bgcolor: "black",
        paper_bgcolor: "black",
        font: {
            color: "white"
        }
    };

    Plotly.newPlot("plot3", data, revenueLayout)

})

d3.json("/hours").then(function (data) {

    var hoursTrace = {
        x: data.country,
        y: data.avg_hours.map(d => +d),
        type: 'bar'
    }

    var data = [hoursTrace];

    var hoursLayout = {
        title: "Average Weekly Hours Played by Country",
        xaxis: {
            title: "Country",
            tickangle: 45
        },
        yaxis: {
            title: "Average Weekly Hours Played"
        },
        plot_bgcolor: "black",
        paper_bgcolor: "black",
        font: {
            color: "white"
        }
    };

    Plotly.newPlot("plot2", data, hoursLayout)

});

d3.json("/age").then(function (data) {

    var ageTrace = {
        x: data.age,
        y: data.avg_hours.map(d => +d),
        type: 'bar'
    }

    var data = [ageTrace];

    var ageLayout = {
        title: "Average Weekly Hours Played by Age Group",
        xaxis: { title: "Country" },
        yaxis: { title: "Average Weekly Hours Played" },
        plot_bgcolor: "black",
        paper_bgcolor: "black",
        font: {
            color: "white"
        }
    };

    Plotly.newPlot("plot", data, ageLayout)

});

/////######THIS CODE WILL NOT WORK UNTIL WE HAVE THE LATLONG FOR COUNTRY,
///// ADD COLUMN IN POSTGRES AND IN JUPYTER NOTEBOOK FOR LOADING DATA
/////THE WE CAN CALL THE COORDS
// var queryUrl = "/mapChart"


// //   // Define a function we want to run once for each feature in the features array
// function addPopup(data, layer) {
//     //     // Give each feature a popup describing the place and time of the countries
//     return layer.bindPopup(`<h3> ${data.countryHours.country} </h3>`);
// }

// // function to receive a layer of markers and plot them on a map.
// function createMap(countryHours) {

//     // Define streetmap and darkmap layers
//     var streetmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
//         maxZoom: 18,
//         id: "streets-v11",
//         accessToken: API_KEY
//     });

//     var darkmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
//         maxZoom: 18,
//         id: "dark-v10",
//         accessToken: API_KEY
//     });

//     // Define a baseMaps object to hold our base layers
//     var baseMaps = {
//         "Street Map": streetmap,
//         "Dark Map": darkmap
//     };

//     // Create overlay object to hold our overlay layer
//     var overlayMaps = {
//         "countryHours": countryHours
//     };

//     // Create our map, giving it the streetmap and country hours layers to display on load
//     var myMap = L.map("map", {
//         center: [37.09, -95.71],
//         zoom: 5,
//         layers: [streetmap, countryHours]
//     });

//     // Create a layer control
//     // Pass in our baseMaps and overlayMaps
//     // Add the layer control to the map
//     L.control.layers(baseMaps, overlayMaps, {
//         collapsed: false
//     }).addTo(myMap);


// }

// Creating our initial map object
// L.map accepts 2 arguments: id of the HTML element to insert the map, and an object containing the initial options for the new map
var myMap = L.map('map', {
    center: [29.76, -95.37],
    zoom: 11
});
// // Adding a tile layer (the background map image) to our map.
// // Leaflet doesn't have out-of-the-box tile layers, but it allows us to usetile layer APIs. Here, we're using mapbox.
// // We use the addTo method to add objects to our map
// // Documentation for tileLayer:https://leafletjs.com/reference-1.6.0.html#tilelayer
L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "streets-v11",
    accessToken: API_KEY
}).addTo(myMap);

//select html panel element 
var panel = d3.select("#panel-info")
// remove any data from the table
panel.html("");

d3.select('#button').on('click', function () {
    d3.event.preventDefault()
    d3.json('http://api.ipstack.com/check?access_key=a8658fb86540d316778f17b3e00f1463&format=1').then(function (countryData) {
        var country = countryData.country_name
        console.log(country)
        var coordinates = [countryData.latitude, countryData.longitude]
        console.log(coordinates)
        var selectedId = d3.select('#selDataset').attr('value', country)

        d3.json("/revenue").then(function (data) {
            console.log(data.country.map(d => d == country ? 'rgba(193,66,66,1)' : 'rgba(66,66,191,1)'))
            var revenueTrace = {
                x: data.country,
                y: data.revenue.map(d => +d),
                marker: {
                    color: data.country.map(d => d == country ? 'rgba(193,66,66,1)' : 'rgba(66,66,191,1)')
                },
                type: 'bar'
            }

            var data = [revenueTrace];

            var revenueLayout = {
                title: "Gaming Revenue by Country",
                xaxis: { title: "Country" },
                yaxis: { title: "Revenue (USD)" },
                plot_bgcolor: "black",
                paper_bgcolor: "black",
                font: {
                    color: "white"
                }
            };

            Plotly.newPlot("plot3", data, revenueLayout)

        })


        d3.json("/hours").then(function (data) {

            var hoursTrace = {
                x: data.country,
                y: data.avg_hours.map(d => +d),
                marker: {
                    color: data.country.map(d => d == country ? 'rgba(193,66,66,1)' : 'rgba(66,66,191,1)')
                },
                type: 'bar'
            }

            var data = [hoursTrace];

            var hoursLayout = {
                title: "Average Weekly Hours Played by Country",
                xaxis: { title: "Country" },
                yaxis: { title: "Average Weekly Hours Played" },
                plot_bgcolor: "black",
                paper_bgcolor: "black",
                font: {
                    color: "white"
                }
            };

            Plotly.newPlot("plot2", data, hoursLayout)

        })

        d3.json("/age").then(function (data) {
            var ageEntry = d3.select("#ageSelect").node().value;
            console.log(ageEntry);

            var ageTrace = {
                x: data.age,
                y: data.avg_hours.map(d => +d),
                marker: {
                    color: data.age.map(d => d == ageEntry ? 'rgba(193,66,66,1)' : 'rgba(66,66,191,1)')
                },
                type: 'bar'
            }

            var data = [ageTrace];

            var ageLayout = {
                title: "Average Weekly Hours Played by Age Group",
                xaxis: { title: "Age Group" },
                yaxis: { title: "Average Weekly Hours Played" },
                plot_bgcolor: "black",
                paper_bgcolor: "black",
                font: {
                    color: "white"
                }
            };

            Plotly.newPlot("plot", data, ageLayout)
        });
    });
});

// Define SVG area dimensions
var svgWidth = 960;
var svgHeight = 500;

// Define the chart's margins as an object
var margin = {
    top: 60,
    right: 60,
    bottom: 60,
    left: 60
};

// Define dimensions of the chart area
var chartWidth = svgWidth - margin.left - margin.right;
var chartHeight = svgHeight - margin.top - margin.bottom;

// Select body, append SVG area to it, and set its dimensions
var svg = d3.select("#plot4")
    .append("svg")
    .attr("width", svgWidth)
    .attr("height", svgHeight);

// Append a group area, then set its margins
var chartGroup = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Configure a parseTime function which will return a new Date object from a string
var parseTime = d3.isoParse("%b-%d-%Y%H:%M:%S GMT");


// Load data from json url
d3.json("/top_ten").then(function (topTen) {

    console.log(topTen)
    // Format the date and cast the force value to a number
    topTen.forEach(function (data) {
        data.date = data.date
    });
    console.log(topTen)


    // Configure a time scale
    // d3.extent returns the an array containing the min and max values for the property specified
    var xTimeScale = d3.scaleTime()
        .domain(d3.extent(topTen, data => data.date))
        .range([0, chartWidth]);

    // Configure a linear scale with a range between the chartHeight and 0
    var yLinearScale = d3.scaleLinear()
        .domain([0, d3.max(topTen, data => data.dota_2)])
        .range([chartHeight, 0]);

    // Create two new functions passing the scales in as arguments
    // These will be used to create the chart's axes
    var bottomAxis = d3.axisBottom(xTimeScale);
    var leftAxis = d3.axisLeft(yLinearScale);

    // Configure a line function which will plot the x and y coordinates using our scales
    var drawLine = d3.line()
        .x(data => xTimeScale(data.date))
        .y(data => yLinearScale(data.dota_2));

    // Append an SVG path and plot its points using the line function
    chartGroup.append("path")
        // The drawLine function returns the instructions for creating the line for gta data
        .attr("d", drawLine(topTen))
        .classed("line", true);

    // Append an SVG group element to the chartGroup, create the left axis inside of it
    chartGroup.append("g")
        .classed("axis", true)
        .call(leftAxis);

    // Append an SVG group element to the chartGroup, create the bottom axis inside of it
    // Translate the bottom axis to the bottom of the page
    chartGroup.append("g")
        .classed("axis", true)
        .attr("transform", `translate(0, ${chartHeight})`)
        .call(bottomAxis);
}).catch(function (error) {
    console.log(error)
    console.log("there is an error")
});